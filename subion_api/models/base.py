"""Basic utilities for document."""
from datetime import datetime
from typing import Any, Dict

from mongoengine import DateTimeField, Document, QuerySet, signals
from mongoengine.errors import MultipleObjectsReturned


class Signal:
    """Mongoengine's signals."""

    @staticmethod
    def update_updated_at(sender, document):
        """Update updated_at."""
        document.updated_at = datetime.utcnow()


signals.pre_save.connect(Signal.update_updated_at)


class BaseSet(QuerySet):
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
        """Return instance or None."""
        count = len(self)
        if count == 1:
            return self[0]
        elif count == 0:
            return None
        else:
            raise MultipleObjectsReturned()


class BaseDocument(Document):
    """Basic fields for document."""

    created_at = DateTimeField(default=datetime.utcnow, null=False)
    deleted_at = DateTimeField(null=True)
    updated_at = DateTimeField(null=True)

    meta: Dict[Any, Any] = {'abstract': True, 'queryset_class': BaseSet}

    def to_dict(self):
        """Return model to a python dict."""
        return NotImplemented

    def __repr__(self):
        """Print object_id of model."""
        return f'<{self.__class__.__name__}: {str(self.id)}>'
