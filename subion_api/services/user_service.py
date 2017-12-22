"""User service."""
from mongoengine.queryset.visitor import Q
from pyramid.httpexceptions import HTTPUnauthorized

from subion_api.models import User


class UserService:
    """User service."""

    @classmethod
    def create_user(cls, data: dict) -> User:
        """Create user from `data`.

        Why so weird?
        Because I can't find the way to overwrite models.User.__init__
        """
        password = data.pop('password')
        user = User(**data)
        user.password = password
        user.save()
        return user

    @classmethod
    def verify_user(cls, data: dict) -> User:
        """Verify user from login data."""
        user: User = User.objects(
            Q(username=data['credential']) | Q(email=data['credential'])).get()
        if not user.check_password(data['password']):
            raise HTTPUnauthorized()
        return user

    @classmethod
    def find_user_from_email(cls, email: str) -> User:
        """Find user from username or email."""
        return User.objects(email=email).get_or_none()

    @classmethod
    def find_user_from_username(cls, username: str) -> User:
        """Find user from username or email."""
        return User.objects(username=username).get_or_none()
