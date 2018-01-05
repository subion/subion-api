"""Useful decorator."""
from functools import wraps

from jsonschema import Draft4Validator
from jwt import InvalidTokenError
from pyramid.httpexceptions import HTTPForbidden, HTTPUnauthorized
from subion_api.utils.exception import Missing

from subion_api.ext import jwt
from subion_api.models import User
from subion_api.validators import subion_checker


def validate(schema):
    """Validate user input with jsonschema."""

    def decorator_maker(fn):

        @wraps(fn)
        def decorator(self, *args, **kwargs):
            validator = Draft4Validator(schema, format_checker=subion_checker)
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
    """Ensure user has logged in."""

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
            user = User.objects(id=data['id']).get_or_none()
            if not user:
                raise Missing()
            self.request.current_user = user
            return fn(self, *args, **kwargs)

    return decorator
