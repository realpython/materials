# from shop_import_recursion.controllers import shop_controller
import shop_import_recursion


class ShopService:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(ShopService, cls).__new__(
                cls, *args, **kwargs
            )
        return cls._instance

    def __init__(self):
        if not hasattr(self, "controller"):
            # self.controller = shop_controller.ShopController()
            self.controller = (
                shop_import_recursion.controllers.shop_controller.ShopController()
            )

    def perform_service_task(self):
        print("Service task performed")
        self.controller.handle_request()
