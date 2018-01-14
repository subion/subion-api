"""Common regular expression."""
import re

# 3 ~ 16 digit, include alphanumeric.
RE_USERNAME = r'^[a-zA-Z0-9-_]{3,16}$'
# 6 ~ 20 digit.
RE_PASSWORD = r"^[-!#$%&'\"*+/=?^_`{}|~0-9A-Za-z\[\]]{6,20}$"

# from mongoengine, for email validating.
_USER_REGEX = re.compile(
    # `dot-atom` defined in RFC 5322 Section 3.2.3.
    r"(^[-!#$%&'*+/=?^_`{}|~0-9A-Z]+(\.[-!#$%&'*+/=?^_`{}|~0-9A-Z]+)*\Z"
    # `quoted-string` defined in RFC 5322 Section 3.2.4.
    r'|^"([\001-\010\013\014\016-\037!#-\[\]-\177]|\\[\001-\011\013\014\016-\177])*"\Z)',
    re.IGNORECASE)
_DOMAIN_REGEX = re.compile(
    r'((?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+)(?:[A-Z0-9-]{2,63}(?<!-))\Z',
    re.IGNORECASE)

# from mongoengine, for url validating.
_URL_REGEX = re.compile(
    r'^(?:[a-z0-9\.\-]*)://'  # scheme is validated separately
    r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}(?<!-)\.?)|'  # domain...
    r'localhost|'  # localhost...
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|'  # ...or ipv4
    r'\[?[A-F0-9]*:[A-F0-9:]+\]?)'  # ...or ipv6
    r'(?::\d+)?'  # optional port
    r'(?:/?|[/?]\S+)$',
    re.IGNORECASE)
_URL_SCHEMES = {'http', 'https', 'ftp', 'ftps'}
