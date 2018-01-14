"""Base service."""
from pyramid.request import Request


class Service:
    """Base service."""

    def __init__(self, request: Request) -> None:
        """Pass request object."""
        self.request = request
