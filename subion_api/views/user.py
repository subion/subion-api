"""Resource User."""
from pyramid.view import view_config, view_defaults
from venusian import lift

from subion_api.services import UserService
from subion_api.validator import CREATE_USER, validate
from subion_api.views.base import Res


@view_defaults(route_name='user', renderer='json')
@lift()
class User(Res):
    """Resource User."""

    @view_config(request_method='POST')
    @validate(CREATE_USER)
    def post(self):
        """Create user."""
        user = UserService.create_user(self.data)
        return user.to_dict()
