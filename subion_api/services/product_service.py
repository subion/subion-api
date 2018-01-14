"""Product service."""
from subion_api.models import Product
from subion_api.services.base import Service


class ProductService(Service):
    """Product service."""

    def create_product(self, name: str, web_site: str, logo: str) -> Product:
        """Create product."""
        if web_site == '':
            web_site = None
        if logo == '':
            logo = None
        product = Product(name=name, web_site=web_site, logo=logo)
        product.save()
        return product
