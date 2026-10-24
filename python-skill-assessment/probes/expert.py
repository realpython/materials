class BaseView:
    def handle(self):
        return ["base"]


class AuthMixin(BaseView):
    def handle(self):
        return ["auth"] + super().handle()


class CacheMixin(BaseView):
    def handle(self):
        return ["cache"] + super().handle()


class ReportView(AuthMixin, CacheMixin):
    def handle(self):
        return ["report"] + super().handle()


print(ReportView().handle())
print([cls.__name__ for cls in ReportView.__mro__])
