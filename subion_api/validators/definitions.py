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
CREDENTIAL = {
    'oneOf': [
        EMAIL,
        USERNAME,
    ]
}
