"""User service."""
from mongoengine.queryset.visitor import Q
from pyramid.httpexceptions import HTTPUnauthorized

from subion_api.models import User
from subion_api.services.base import Service
from subion_api.utils.exception import AlreadyExist, Missing


class UserService(Service):
    """User service."""

    def create_user(self, username: str, email: str, password: str) -> User:
        """Create user.

        Why so weird?
        Because I can't find the way to overwrite models.User.__init__
        """
        user_exists = User.objects(Q(username=username) |
                                   Q(email=email)).active.get_or_none()
        if user_exists:
            raise AlreadyExist()
        user = User(username=username, email=email)
        user.password = password
        user.save()
        return user

    def verify_user(self, credential: str, password: str) -> User:
        """Verify user from login data."""
        user: User = User.objects(Q(username=credential) |
                                  Q(email=credential)).active.get_or_none()
        if not user:
            raise Missing()
        if not user.check_password(password):
            raise HTTPUnauthorized()
        return user

    def find_user_by_email(self, email: str) -> User:
        """Find user by username or email."""
        return User.objects(email=email).active.get_or_none()

    def find_user_by_username(self, username: str) -> User:
        """Find user by username or email."""
        return User.objects(username=username).active.get_or_none()

    def modify_user(self, username: str, email: str, password: str) -> User:
        """Modify user's data."""
        if username:
            user = self.find_user_by_username(username)
            if not user:
                self.request.current_user.username = username
            else:
                raise AlreadyExist()
        if email:
            user = self.find_user_by_email(email)
            if not user:
                self.request.current_user.email = email
            else:
                raise AlreadyExist()
        if password:
            self.request.current_user.password = password
        self.request.current_user.save()
        return self.request.current_user
