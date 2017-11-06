"""Define DRM."""
from mongoengine import connect
from subion_api.models.user import User

__all__ = ['User']


def includeme(config):
    connect(host=config.registry.settings['mongoengine.uri'])
