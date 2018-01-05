"""Basic Resource."""
from pyramid.request import Request


class Resource:
    """Basic Resource."""

    def __init__(self, request: Request) -> None:
        """Resource initialization."""
        self.request = request
