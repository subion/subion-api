"""Basic Resource."""
from pyramid.request import Request


class Res:
    """Basic Resource."""

    def __init__(self, request: Request) -> None:
        """Resource initialization."""
        self.request = request
