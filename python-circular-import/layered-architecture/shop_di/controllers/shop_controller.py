class ShopController:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self, service):
        if not hasattr(self, 'service'):
            self.service = service

    def handle_request(self):
        print("Handling request")
        self.service.perform_service_task()