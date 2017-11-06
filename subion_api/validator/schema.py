"""Jsonschema validator for input data."""
from subion_api.validator.regex import RE_USERNAME, RE_PASSWORD

GET_TOKEN = {
    'type': 'object',
    'properties': {
        'credential': {
            'type': 'string',
            'oneOf': [{
                'format': 'mongo_email'
            }, {
                'pattern': RE_USERNAME
            }]
        },
        'password': {
            'type': 'string',
            'pattern': RE_PASSWORD
        }
    },
    'additionalProperties': False,
    'required': ['credential', 'password']
}

CREATE_USER = {
    'type': 'object',
    'properties': {
        'username': {
            'type': 'string',
            'pattern': RE_USERNAME
        },
        'email': {
            'type': 'string',
            'format': 'mongo_email'
        },
        'password': {
            'type': 'string',
            'pattern': RE_PASSWORD
        }
    },
    'additionalProperties': False,
    'required': ['username', 'password', 'email']
}
