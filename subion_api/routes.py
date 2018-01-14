"""Initialize pyramid routes."""


def includeme(config):
    """Include in config."""
    config.add_route('token', '/token')
    config.add_route('users', '/users')
    config.add_route('user', '/user')
    config.add_route('subscriptions', '/user/subscriptions')
    config.add_route('products', '/products')
