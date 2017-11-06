"""Basic Resource."""
from pyramid.request import Request
from pyramid.httpexceptions import HTTPMethodNotAllowed
from pyramid.view import view_config


class Res:
    """Basic Resource."""

    def __init__(self, request: Request) -> None:
        """Resource initialization."""
        self.request = request

    @view_config(request_method='GET')
    def get(self):
        """Initialize default method GET."""
        raise HTTPMethodNotAllowed()

    @view_config(request_method='POST')
    def post(self):
        """Initialize default method POST."""
        raise HTTPMethodNotAllowed()

    @view_config(request_method='PUT')
    def put(self):
        """Initialize default method PUT."""
        raise HTTPMethodNotAllowed()

    @view_config(request_method='PATCH')
    def patch(self):
        """Initialize default method PATCH."""
        raise HTTPMethodNotAllowed()

    @view_config(request_method='DELETE')
    def delete(self):
        """Initialize default method DELETE."""
        raise HTTPMethodNotAllowed()
