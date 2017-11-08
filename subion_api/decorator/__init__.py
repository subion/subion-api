"""Useful decorator."""
from functools import wraps

from jsonschema import Draft4Validator, FormatChecker
from jwt import InvalidTokenError
from pyramid.httpexceptions import HTTPForbidden, HTTPUnauthorized

from subion_api.ext import jwt
from subion_api.models import User
from subion_api.validator.regex import _DOMAIN_REGEX, _USER_REGEX


@FormatChecker.cls_checks('mongo_email')
def mongo_email_check(value: str) -> bool:
    """Use the same way as mongoengine to validate email."""
    if '@' not in value:
        return False

    user_part, domain_part = value.rsplit('@', 1)
    if not _USER_REGEX.match(user_part):
        return False
    if not _DOMAIN_REGEX.match(domain_part):
        return False
    try:
        domain_part = domain_part.encode('idna').decode('ascii')
    except UnicodeError:
        return False
    else:
        if not _DOMAIN_REGEX.match(domain_part):
            return False
    return True


def validate(schema):
    """Validate user input with jsonschema."""

    def decorator_maker(fn):

        @wraps(fn)
        def decorator(self, *args, **kwargs):
            validator = Draft4Validator(schema, format_checker=FormatChecker())
            if self.request.method == 'GET':
                data = dict(self.request.params)
                validator.validate(data)
            else:
                data = self.request.json
                validator.validate(data)
            self.data: dict = data
            return fn(self, *args, **kwargs)

        return decorator

    return decorator_maker


def login_required(fn):
    """Validate user log in or not."""

    @wraps(fn)
    def decorator(self, *args, **kwargs):
        if not self.request.authorization:
            raise HTTPUnauthorized()
        scheme, token = self.request.authorization
        if scheme != 'JWT':
            raise HTTPUnauthorized()
        try:
            data = jwt.decode(token)
        except InvalidTokenError as e:
            raise HTTPForbidden()
        else:
            self.user: User = User.objects(id=data['id']).get()
            return fn(self, *args, **kwargs)

    return decorator
