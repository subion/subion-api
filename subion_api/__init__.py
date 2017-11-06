"""Entry of the project."""
from pyramid.config import Configurator


def main(global_config, **settings):
    """Initialize settings of the project and return a Pyramid WSGI application."""
    config = Configurator(settings=settings)
    config.include('pyramid_mako')
    config.include('subion_api.routes', route_prefix='/api')
    config.include('subion_api.models')
    config.scan()
    return config.make_wsgi_app()
