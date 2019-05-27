from django.contrib.auth import login, logout, update_session_auth_hash
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView

from accounts.backends import EmailBackend
from accounts.forms import LogInForm, PasswordChangeForm


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


class PasswordChangeView(FormView):
    form_class = PasswordChangeForm
    template_name = "registration/password_change_form.html"
    success_url = reverse_lazy("password_change_done")

    def form_valid(self, form):
        new_password = form.cleaned_data["password1"]
        old_password = form.cleaned_data["old_password"]
        user = self.request.user
        if user.check_password(old_password):
            user.set_password(new_password)
            user.save()
            update_session_auth_hash(self.request, user)
            return super().form_valid(form)
        else:
            return redirect(reverse_lazy("password_change"))
