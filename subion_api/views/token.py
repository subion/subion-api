"""Resource Token."""
from pyramid.view import view_config, view_defaults
from venusian import lift

from subion_api.ext import jwt
from subion_api.services import UserService
from subion_api.validator import GET_TOKEN, validate
from subion_api.views.base import Res


@view_defaults(route_name='token', renderer='json')
@lift()
class Token(Res):
    """Resource Token."""

    @view_config(request_method='POST')
    @validate(GET_TOKEN)
    def post(self):
        """Generate a token."""
        user = UserService.verify_user(self.data)
        token = jwt.encode({'id': str(user.id)})
        return {'token': token}
