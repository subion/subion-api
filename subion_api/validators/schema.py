"""Jsonschema validator for input data."""
from subion_api.validators.definitions import (EMAIL, USERNAME, PASSWORD,
                                               PRODUCT_NAME, URL, EMPTY_STRING, COST, EXPIRATION)

GET_TOKEN = {
    'type': 'object',
    'properties': {
        'credential': {
            'oneOf': [
                EMAIL,
                USERNAME,
            ]
        },
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

CREATE_PRODUCT = {
    'type': 'object',
    'properties': {
        'name': PRODUCT_NAME,
        'web_site': {
            'oneOf': [
                URL,
                EMPTY_STRING,
            ]
        },
        'logo': {
            'oneOf': [
                URL,
                EMPTY_STRING,
            ]
        },
    },
    'additionalProperties': False,
    'required': ['name', 'web_site', 'logo']
}


SUBSCRIBE_PRODUCT = {
    'type': 'object',
    'properties': {
        'product_name': PRODUCT_NAME,
        'cost': COST,
        'expiration': EXPIRATION,
    },
    'additionalProperties': False,
    'required': ['product_name', 'cost', 'expiration']
}
