"""Resource Token."""
from pyramid.view import view_config, view_defaults

from subion_api.decorators import login_required, validate
from subion_api.validators import SUBSCRIBE_PRODUCT

from subion_api.services import SubscriptionService
from pyramid.request import Request


@view_defaults(route_name='subscriptions', renderer='json')
class Subscription:
    """Resource subscription."""

    def __init__(self, request: Request) -> None:
        """Initialize resource and service."""
        self.request = request
        self.service = SubscriptionService(request)

    @view_config(request_method='GET')
    @login_required
    def get(self):
        """Get subscription list."""
        subscriptions = self.service.get_subscriptions()
        return {'subscriptions': [s.to_dict() for s in subscriptions]}

    @view_config(request_method='POST')
    @login_required
    @validate(SUBSCRIBE_PRODUCT)
    def post(self):
        """Subscribe a product."""
        subscription = self.service.create_subscription(
            self.data['product_name'], self.data['cost'],
            self.data['expiration'])
        return subscription.to_dict()
