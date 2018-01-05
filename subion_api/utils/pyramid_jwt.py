"""Encode and decode Json Web Token."""
import os
from datetime import datetime, timedelta
from typing import Any, Dict, cast

import jwt
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from pyramid.decorator import reify

from subion_api import settings


class JWT:
    """Utility class for encoding and decoding Json Web Token.

    >>> jwt = JWT()
    >>> token = jwt.encode({'id': 1})
    >>> data = jwt.decode(token)
    >>> data
    {'id': 1}
    """

    def __init__(self):
        """Initialize JWT:iss & JWT:aud from settings.py."""
        self.iss = settings.ISSUER
        self.aud = settings.AUDIENCE
        self.key_path = settings.KEY_DIR

    @reify
    def _private_key(self):
        """Return a private encrypted RSA key."""
        with open(os.path.join(self.key_path, 'password.pem'), 'rb') as f:
            password = f.read().strip()

        with open(os.path.join(self.key_path, 'private.pem'), 'rb') as f:
            return serialization.load_pem_private_key(
                f.read(), password=password, backend=default_backend())

    @reify
    def _public_key(self):
        """Return a public encrypted RSA key."""
        with open(os.path.join(self.key_path, 'public.pem'), 'rb') as f:
            return serialization.load_pem_public_key(
                f.read(), backend=default_backend())

    @property
    def _claim(self):
        """Return default claims in JWT."""
        now = datetime.utcnow()
        return {
            'iss': self.iss,
            'aud': self.aud,
            'iat': now,
            'nbf': now,
            'exp': now,
        }

    def encode(self, data: Dict[str, Any],
               exp: timedelta = timedelta(days=1)) -> str:
        """Encode `data` to JWT that will be expired in `exp`."""
        for k, v in self._claim.items():
            data.setdefault(k, v)
        data['exp'] += exp
        return jwt.encode(
            data, self._private_key, algorithm='RS256').decode('utf-8')

    def decode(self, token: str, silent: bool = False) -> Dict[str, Any]:
        """Decode `token` to data."""
        try:
            data = cast(Dict[str, Any],
                        jwt.decode(
                            token,
                            issuer=self.iss,
                            audience=self.aud,
                            key=self._public_key))
            for k in self._claim:
                data.pop(k)
        except jwt.InvalidTokenError as e:
            if silent:
                data = dict()
            else:
                raise e
        return data


if __name__ == '__main__':
    import doctest
    doctest.testmod()
