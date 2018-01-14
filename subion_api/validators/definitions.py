"""Constant schema difinitions."""

PASSWORD = {
    'type': 'string',
    'minLength': 6,
    'maxLength': 20,
    'format': 'password',
}
USERNAME = {
    'type': 'string',
    'minLength': 3,
    'maxLength': 16,
    'format': 'username',
}

EMAIL = {
    'type': 'string',
    'format': 'email',
}

PRODUCT_NAME = {
    'type': 'string',
    'minLength': 1,
    'maxLength': 256,
}

URL = {
    'type': 'string',
    'format': 'url',
}

EMPTY_STRING = {
    'type': 'string',
    'minLength': 0,
    'maxLength': 0,
}

COST = {
    'type': 'integer',
    'minimum': 0,
}

EXPIRATION = {
    'type': 'integer',
    'minimum': 0,
}
