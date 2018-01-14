"""Subscription service."""
from typing import List

from subion_api.models import Product, Subscription
from subion_api.services.base import Service
from subion_api.utils.exception import Missing


class SubscriptionService(Service):
    """Subscription service."""

    def get_subscriptions(self) -> List[Subscription]:
        """Get subscriptions list."""
        subscriptions = Subscription.objects(
            user=self.request.current_user).active.all()
        return subscriptions

    def create_subscription(self, product_name: str, cost: int,
                            expiration: int) -> Subscription:
        """Subscribe a product."""
        product = Product.objects(name=product_name).active.get_or_none()
        if not product:
            raise Missing()
        subscription = Subscription(
            user=self.request.current_user,
            product=product,
            cost=cost,
            expiration=expiration)
        subscription.save()
        return subscription
