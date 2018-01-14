"""Resource Token."""
from pyramid.view import view_config, view_defaults

from subion_api.decorators import login_required, validate
from subion_api.validators import CREATE_PRODUCT

from subion_api.services import ProductService
from pyramid.request import Request


@view_defaults(route_name='products', renderer='json')
class Product:
    """Resource product."""

    def __init__(self, request: Request) -> None:
        """Initialize resource and service."""
        self.request = request
        self.service = ProductService(request)

    @view_config(request_method='POST')
    @login_required
    @validate(CREATE_PRODUCT)
    def post(self):
        """Create a product."""
        product = self.service.create_product(
            self.data['name'], self.data['web_site'], self.data['logo'])

        return product.to_dict()
