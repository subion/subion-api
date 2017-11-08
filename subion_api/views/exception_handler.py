"""Handle exceptions."""
from json import JSONDecodeError

from jsonschema.exceptions import ValidationError
from mongoengine.errors import DoesNotExist, NotUniqueError
from pyramid.exceptions import PredicateMismatch
from pyramid.httpexceptions import HTTPError
from pyramid.request import Request
from pyramid.view import exception_view_config

from subion_api.utils import ExceptionResponse


@exception_view_config(HTTPError)
def http_error(exc: HTTPError, request: Request):
    """Jsonify http error."""
    return ExceptionResponse(exc.status_code)


@exception_view_config(PredicateMismatch)
def method_not_allowed(exc: PredicateMismatch, request: Request):
    """`PredicateMismatch` mains method not allowed."""
    return ExceptionResponse(405)


@exception_view_config(JSONDecodeError)
def parse_body_error(exc: JSONDecodeError, request: Request):
    """Invalid request format."""
    return ExceptionResponse(400, {'message': 'Body should be a JSON object'})


@exception_view_config(ValidationError)
def validation_error(exc: ValidationError, request: Request):
    """Input not validated."""
    return ExceptionResponse(body={
        'message': exc.message,
        'error': {
            'resource': request.matched_route.name,
            'code': 'invalid'
        },
    })


@exception_view_config(NotUniqueError)
def already_exists(exc: NotUniqueError, request: Request):
    """Rsource already exists."""
    return ExceptionResponse(body={
        'message': 'Validation Failed',
        'error': {
            'resource': request.matched_route.name,
            'code': 'already_exists'
        },
    })


@exception_view_config(DoesNotExist)
def does_not_exist(exc: DoesNotExist, request: Request):
    """Rsource does not exists."""
    return ExceptionResponse(body={
        'message': 'Validation Failed',
        'error': {
            'resource': request.matched_route.name,
            'code': 'missing'
        },
    })
