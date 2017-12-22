"""Resource User."""
from pyramid.view import view_config, view_defaults

from subion_api.decorator import login_required, validate
from subion_api.services import UserService
from subion_api.validator import CREATE_USER, MODIFY_USER
from subion_api.views.base import Res
from subion_api.utils.exception import AlreadyExist


@view_defaults(route_name='users', renderer='json')
class User(Res):
    """Resource User."""

    @view_config(route_name='user', request_method='GET')
    @login_required
    def get_current_user(self):
        """Get current user."""
        return self.user.to_dict()

    @view_config(route_name='user', request_method='PATCH')
    @login_required
    @validate(MODIFY_USER)
    def patch(self):
        """Modify user."""
        username = self.data.get('username')
        email = self.data.get('email')
        password = self.data.get('password')
        if username:
            user = UserService.find_user_from_username(username)
            if not user:
                self.user.username = username
            else:
                raise AlreadyExist()
        if email:
            user = UserService.find_user_from_email(email)
            if not user:
                self.user.email = email
            else:
                raise AlreadyExist()
        if password:
            self.user.password = password
        self.user.save()
        return self.user.to_dict()

    @view_config(request_method='POST')
    @validate(CREATE_USER)
    def post(self):
        """Create user."""
        user = UserService.create_user(self.data)
        return user.to_dict()
