"""Define common exception response."""
from pyramid.httpexceptions import HTTPError, exception_response
from mongoengine.errors import NotUniqueError, DoesNotExist


class ExceptionResponse(HTTPError):
    """Return jsonify exception response."""

    def __new__(cls, status_code: int = 422, body: dict = None):
        """Use `exception_response` to take over response."""
        r = exception_response(status_code)
        if body is None:
            body = {'message': r.title}
        r.json_body = body
        r.content_type = 'application/json'
        return r

    def __init__(self, status_code: int = 422, body: dict = None) -> None:
        """Never used. Lint for init."""
        pass


class Missing(DoesNotExist):
    pass


class AlreadyExist(NotUniqueError):
    pass
