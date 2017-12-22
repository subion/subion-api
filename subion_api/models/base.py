"""Basic utilities for document."""
from datetime import datetime
from typing import Any, Dict

import bcrypt
from mongoengine import BinaryField, DateTimeField, Document, QuerySet, signals
from mongoengine.errors import MultipleObjectsReturned


class Signal:
    """Mongoengine's signals."""

    @staticmethod
    def update_updated_at(sender, document):
        """Update updated_at."""
        document.updated_at = datetime.utcnow()


signals.pre_save.connect(Signal.update_updated_at)


class ActiveSet(QuerySet):
    """Add filter for finding active or deleted documents."""

    @property
    def active(self):
        """Return active documents."""
        return self.filter(deleted_at__exists=False)

    @property
    def deleted(self):
        """Return deleted documents."""
        return self.filter(deleted_at__exists=True)

    def get_or_none(self):
        count = self.count()
        if count == 1:
            return self.get()
        elif count == 0:
            return None
        else:
            raise MultipleObjectsReturned()


class BaseDocument(Document):
    """Basic fields for every document."""

    created_at = DateTimeField(default=datetime.utcnow, null=False)
    deleted_at = DateTimeField(null=True)
    updated_at = DateTimeField(null=True)

    meta: Dict[Any, Any] = {'abstract': True, 'queryset_class': ActiveSet}

    def to_dict(self):
        """Return model to a python dict."""
        return NotImplemented

    def __repr__(self):
        """Print object_id of model."""
        return f'<{self.__class__.__name__}: {str(self.id)}>'


class PasswordMixin:
    """Add password fields for document."""

    _password = BinaryField(required=True, max_bytes=128, null=False)

    @property
    def password(self):
        """Property password is non-accessible, but can be rewrote."""
        raise ValueError('non-accessible property.')

    @password.setter
    def password(self, value: str) -> None:
        self._password = bcrypt.hashpw(value.encode('utf-8'), bcrypt.gensalt())

    def check_password(self, value: str) -> bool:
        """Check password validity."""
        return bcrypt.checkpw(value.encode('utf-8'), self._password)
