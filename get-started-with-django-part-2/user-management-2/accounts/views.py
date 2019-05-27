from django.contrib.auth import login, logout
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView

from accounts.backends import EmailBackend
from accounts.forms import LogInForm


class LogInView(FormView):
    form_class = LogInForm
    template_name = "registration/login.html"
    success_url = reverse_lazy("profile")
    backend = EmailBackend()

    def form_valid(self, form):
        email = form.cleaned_data["email"]
        password = form.cleaned_data["password"]
        user = self.backend.authenticate(self, email=email, password=password)
        if user:
            login(self.request, user)
            return super().form_valid(form)
        else:
            return redirect(reverse_lazy("login"))


class LogOutView(TemplateView):
    template_name = "registration/logged_out.html"

    def dispatch(self, request, *args, **kwargs):
        logout(request)
        return super().dispatch(request, *args, **kwargs)
