"""Useful decorator."""
from functools import wraps

from jsonschema import Draft4Validator, FormatChecker

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
                self.data = data
            else:
                validator.validate(self.request.json)
                self.data = self.request.json
            return fn(self, *args, **kwargs)

        return decorator

    return decorator_maker


def login_required(fn):
    """Validate user log in or not."""

    @wraps(fn)
    def decorator(self, *args, **kwargs):
        # TODO
        pass
