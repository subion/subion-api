"""Place default config."""
import os

ISSUER = 'subion'
AUDIENCE = 'subion:api'
KEY_DIR = os.path.join(os.path.dirname(__file__), '..', 'certificate')
