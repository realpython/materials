from shop.services.shop_service import ShopService


class ShopController:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(ShopController, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'service'):
            self.service = ShopService()

    def handle_request(self):
        print("Handling request")
        self.service.perform_service_task()