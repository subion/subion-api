"""The custom jsonschema format checker."""
import re
from jsonschema import FormatChecker
from subion_api.validators.regex import (_DOMAIN_REGEX, _USER_REGEX,
                                         RE_PASSWORD, RE_USERNAME)

subion_checker = FormatChecker()

USERNAME_REGEX = re.compile(RE_USERNAME)
PASSWORD_REGEX = re.compile(RE_PASSWORD)


@subion_checker.checks('email')
def email_check(value: str) -> bool:
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


@subion_checker.checks('password')
def password_check(value: str) -> bool:
    """Password format checker."""
    if not PASSWORD_REGEX.match(value):
        return False
    else:
        return True


@subion_checker.checks('username')
def username_check(value: str) -> bool:
    """Username format checker."""
    if not USERNAME_REGEX.match(value):
        return False
    else:
        return True
