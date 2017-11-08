"""Resource User."""
from pyramid.view import view_config, view_defaults

from subion_api.decorator import login_required, validate
from subion_api.services import UserService
from subion_api.validator import CREATE_USER
from subion_api.views.base import Res


@view_defaults(route_name='users', renderer='json')
class User(Res):
    """Resource User."""

    @view_config(route_name='user', request_method='GET')
    @login_required
    def get_current_user(self):
        """Get current user."""
        return self.user.to_dict()

    @view_config(request_method='POST')
    @validate(CREATE_USER)
    def post(self):
        """Create user."""
        user = UserService.create_user(self.data)
        return user.to_dict()
