"""Jsonschema validator for input data."""
from subion_api.validators.definitions import (EMAIL, USERNAME, CREDENTIAL,
                                               PASSWORD)

GET_TOKEN = {
    'type': 'object',
    'properties': {
        'credential': CREDENTIAL,
        'password': PASSWORD,
    },
    'additionalProperties': False,
    'required': ['credential', 'password']
}

CREATE_USER = {
    'type': 'object',
    'properties': {
        'username': USERNAME,
        'email': EMAIL,
        'password': PASSWORD,
    },
    'additionalProperties': False,
    'required': ['username', 'password', 'email']
}

MODIFY_USER = {
    'type': 'object',
    'properties': {
        'username': USERNAME,
        'email': EMAIL,
        'password': PASSWORD,
    },
    "additionalProperties": False,
    "minProperties": 1
}
