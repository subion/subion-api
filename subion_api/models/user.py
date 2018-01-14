"""User model."""
import bcrypt
from mongoengine import BinaryField, EmailField, StringField

from subion_api.models.base import BaseDocument
from subion_api.validators.regex import RE_USERNAME


class User(BaseDocument):
    """User model."""

    meta = {'collection': 'user'}

    username = StringField(
        required=True, unique=True, null=False, regex=RE_USERNAME)
    email = EmailField(unique=True, null=False, required=True)
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

    def to_dict(self) -> dict:
        """Return model to a python dict."""
        return {
            'username': self.username,
            'email': self.email,
            'created_at': self.created_at.timestamp(),
            'updated_at': self.updated_at.timestamp(),
        }
