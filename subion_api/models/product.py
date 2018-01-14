"""Product model."""
from mongoengine import StringField, URLField

from subion_api.models.base import BaseDocument


class Product(BaseDocument):
    """Product model."""

    meta = {'collection': 'product'}

    name = StringField(
        required=True, unique=True, null=False, min_length=1, max_length=256)
    web_site = URLField(
        verify_exists=True, required=False, unique=True, sparse=True)
    logo = URLField(
        verify_exists=True, required=False, unique=True, sparse=True)

    def to_dict(self) -> dict:
        """Return model to a python dict."""
        return {'name': self.name, 'web_site': self.web_site, 'logo': self.logo}
