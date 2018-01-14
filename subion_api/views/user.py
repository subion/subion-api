"""Resource User."""
from pyramid.view import view_config, view_defaults

from subion_api.decorators import login_required, validate
from subion_api.services import UserService
from subion_api.validators import CREATE_USER, MODIFY_USER
from pyramid.request import Request


@view_defaults(route_name='users', renderer='json')
class User:
    """Resource User."""

    def __init__(self, request: Request) -> None:
        """Initialize resource and service."""
        self.request = request
        self.service = UserService(request)

    @view_config(route_name='user', request_method='GET')
    @login_required
    def get(self):
        """Get current user."""
        return self.request.current_user.to_dict()

    @view_config(route_name='user', request_method='PATCH')
    @login_required
    @validate(MODIFY_USER)
    def patch(self):
        """Modify user."""
        user = self.service.modify_user(
            self.data.get('username'), self.data.get('email'),
            self.data.get('password'))
        return user.to_dict()

    @view_config(request_method='POST')
    @validate(CREATE_USER)
    def post(self):
        """Create user."""
        user = self.service.create_user(
            self.data['username'], self.data['email'], self.data['password'])
        return user.to_dict()
