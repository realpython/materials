from shop_di.controllers.shop_controller import ShopController
from shop_di.services.shop_service import ShopService

if __name__ == "__main__":
    service = ShopService()
    controller = ShopController(service)
    controller.handle_request()