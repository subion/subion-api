"""Define ODM."""
from mongoengine import connect
from subion_api.models.user import User
from subion_api.models.subscription import Subscription
from subion_api.models.product import Product

__all__ = ['User', 'Subscription', 'Product']


def includeme(config):
    connect(host=config.registry.settings['mongoengine.uri'])
