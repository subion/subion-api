"""Subscription model."""

from mongoengine import IntField, ReferenceField

from subion_api.models.base import BaseDocument
from subion_api.models.product import Product
from subion_api.models.user import User


class Expiration:
    """Expiration constant."""

    SEVEN_DAYS = 7
    ONE_MONTH = 30
    THREE_MONTHS = 120
    HALF_YEAR = 180
    ONE_YEAR = 365


class Subscription(BaseDocument):
    """Subscription model."""

    meta = {'collection': 'subscription'}

    user = ReferenceField(User)
    product = ReferenceField(Product)
    cost = IntField(min_value=0, required=True, null=False, default=0)
    expiration = IntField(
        min_value=0, required=True, null=False, default=Expiration.ONE_MONTH)

    def to_dict(self) -> dict:
        """Return model to a python dict."""
        return {
            'cost': self.cost,
            'expiration': self.expiration,
            'product': self.product.to_dict(),
        }
