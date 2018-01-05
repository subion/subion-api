"""User service."""
from mongoengine.queryset.visitor import Q
from pyramid.httpexceptions import HTTPUnauthorized
from pyramid.threadlocal import get_current_request
from subion_api.models import User
from subion_api.utils.exception import AlreadyExist, Missing


class UserService:
    """User service."""

    @classmethod
    def create_user(cls, username: str, email: str, password: str) -> User:
        """Create user.

        Why so weird?
        Because I can't find the way to overwrite models.User.__init__
        """
        user_exists = User.objects(Q(username=username)
                                   | Q(email=email)).active.get_or_none()
        if user_exists:
            raise AlreadyExist()
        user = User(username=username, email=email)
        user.password = password
        user.save()
        return user

    @classmethod
    def verify_user(cls, credential: str, password: str) -> User:
        """Verify user from login data."""
        user: User = User.objects(Q(username=credential)
                                  | Q(email=credential)).active.get_or_none()
        if not user:
            raise Missing()
        if not user.check_password(password):
            raise HTTPUnauthorized()
        return user

    @classmethod
    def find_user_by_email(cls, email: str) -> User:
        """Find user by username or email."""
        return User.objects(email=email).active.get_or_none()

    @classmethod
    def find_user_by_username(cls, username: str) -> User:
        """Find user by username or email."""
        return User.objects(username=username).active.get_or_none()

    @classmethod
    def modify_user(cls, username: str, email: str, password: str) -> User:
        """Modify user's data."""
        request = get_current_request()
        if username:
            user = UserService.find_user_by_username(username)
            if not user:
                request.current_user.username = username
            else:
                raise AlreadyExist()
        if email:
            user = UserService.find_user_by_email(email)
            if not user:
                request.current_user.email = email
            else:
                raise AlreadyExist()
        if password:
            request.current_user.password = password
        request.current_user.save()
        return request.current_user
