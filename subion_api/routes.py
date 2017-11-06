"""Initialize pyramid routes."""


def includeme(config):
    """Include in config."""
    config.add_route('token', '/token')
    config.add_route('user', '/users')
