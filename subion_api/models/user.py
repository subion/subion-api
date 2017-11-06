"""User model."""
from mongoengine import EmailField, StringField

from subion_api.models.base import BaseDocument, PasswordMixin
from subion_api.validator import RE_USERNAME


class User(BaseDocument, PasswordMixin):
    """User model."""

    username = StringField(
        required=True, unique=True, null=False, regex=RE_USERNAME)
    email = EmailField(unique=True, null=False, required=True)

    meta = {'collection': 'user'}

    def to_dict(self) -> dict:
        """Return model to a python dict."""
        return {
            'username': self.username,
            'email': self.email,
            'created_at': self.created_at.timestamp(),
        }
