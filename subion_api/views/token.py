"""Resource Token."""
from pyramid.view import view_config, view_defaults

from subion_api.decorators import validate
from subion_api.ext import jwt
from subion_api.services import UserService
from subion_api.validators import GET_TOKEN
from pyramid.request import Request


@view_defaults(route_name='token', renderer='json')
class Token:
    """Resource Token."""

    def __init__(self, request: Request) -> None:
        """Initialize resource and service."""
        self.request = request
        self.service = UserService(request)

    @view_config(request_method='POST')
    @validate(GET_TOKEN)
    def post(self):
        """Generate a token."""
        user = self.service.verify_user(self.data['credential'],
                                        self.data['password'])
        token = jwt.encode({'id': str(user.id)})
        return {'token': token}
