from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.exceptions import ValidationError
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views.generic import FormView, TemplateView

from accounts.backends import EmailBackend
from accounts.forms import (
    LogInForm,
    PasswordChangeForm,
    PasswordResetRequestForm,
    PasswordResetForm,
    SignUpForm,
)
from accounts.models import User


class LogInView(FormView):
    form_class = LogInForm
    template_name = "registration/login.html"
    success_url = reverse_lazy("profile")
    backend = EmailBackend()

    def form_valid(self, form):
        email = form.cleaned_data["email"]
        password = form.cleaned_data["password"]
        user = self.backend.authenticate(self, email=email, password=password)
        if user and user.is_active:
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


class PasswordResetView(FormView):
    form_class = PasswordResetRequestForm
    template_name = "registration/password_reset_form.html"
    success_url = reverse_lazy("password_reset_done")
    email_template_name = "registration/password_reset_email.html"
    from_email = "admin@ums.io"
    token_generator = default_token_generator

    def form_valid(self, form):
        email = form.cleaned_data["email"]
        try:
            user = User.objects.get(email=email)
        except User.ObjectDoesNotExist:
            return redirect(reverse_lazy("password_reset"))
        else:
            current_site = get_current_site(self.request)
            subject = "[UMS] Password Reset Request"
            context = {
                "email": email,
                "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                "domain": current_site.domain,
                "user": user,
                "token": self.token_generator.make_token(user),
            }

            body = render_to_string(self.email_template_name, context)
            email_message = EmailMessage(
                subject, body, self.from_email, [email]
            )
            email_message.send()
        return super().form_valid(form)


class PasswordResetConfirmView(FormView):
    form_class = PasswordResetForm
    template_name = "registration/password_reset_confirm.html"
    success_url = reverse_lazy("password_reset_complete")
    token_generator = default_token_generator

    def dispatch(self, *args, **kwargs):
        self.validlink = False
        try:
            uidb64 = kwargs["uidb64"]
            token = kwargs["token"]
        except KeyError:
            self.user = None

        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            self.user = User.objects.get(pk=uid)
        except (
            TypeError,
            ValueError,
            OverflowError,
            User.ObjectDoesNotExist,
            ValidationError,
        ):
            self.user = None

        if self.user is not None:
            if self.token_generator.check_token(self.user, token):
                self.validlink = True
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.validlink:
            context["validlink"] = True
        else:
            context["form"] = None
            context["validlink"] = False
        return context

    def form_valid(self, form):
        password = form.cleaned_data["password1"]
        self.user.set_password(password)
        self.user.save()
        return super().form_valid(form)


class SignUpView(FormView):
    form_class = SignUpForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("signup_done")
    email_template_name = "registration/signup_email.html"
    from_email = "admin@ums.io"
    token_generator = default_token_generator

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data["password1"])
        user.save()

        email = form.cleaned_data["email"]
        current_site = get_current_site(self.request)
        context = {
            "email": email,
            "domain": current_site.domain,
            "uid": urlsafe_base64_encode(force_bytes(user.pk)),
            "user": user,
            "token": self.token_generator.make_token(user),
        }
        subject = "[UMS] Account Confirmation"
        body = render_to_string(self.email_template_name, context)

        email_message = EmailMessage(subject, body, self.from_email, [email])
        email_message.send()
        return super().form_valid(form)


class SignUpCompleteView(TemplateView):
    template_name = "registration/signup_complete.html"
    token_generator = default_token_generator

    def dispatch(self, *args, **kwargs):
        self.validlink = False
        try:
            uidb64 = kwargs["uidb64"]
            token = kwargs["token"]
        except KeyError:
            self.user = None

        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            self.user = User.objects.get(pk=uid)
        except (
            TypeError,
            ValueError,
            OverflowError,
            ValidationError,
            User.ObjectDoesNotExist,
        ):
            self.user = None

        if self.user is not None:
            if self.token_generator.check_token(self.user, token):
                self.user.is_active = True
                self.user.save()
                self.validlink = True

        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["validlink"] = self.validlink
        return context


class SignUpTokenRequestView(FormView):
    form_class = PasswordResetRequestForm
    template_name = "registration/signup_token_request.html"
    success_url = reverse_lazy("signup_done")
    email_template_name = "registration/signup_email.html"
    from_email = "admin@ums.io"
    token_generator = default_token_generator

    def form_valid(self, form):
        email = form.cleaned_data["email"]
        try:
            user = User.objects.get(email=email)
        except User.ObjectDoesNotExist:
            user = None
            return redirect(reverse_lazy("signup_token_request"))
        else:
            if user and user.is_active:
                return redirect(reverse_lazy("login"))
            current_site = get_current_site(self.request)
            context = {
                "email": email,
                "domain": current_site.domain,
                "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                "token": self.token_generator.make_token(user),
            }

            subject = "[UMS] Account Confirmation"
            body = render_to_string(self.email_template_name, context)
            email_message = EmailMessage(
                subject, body, self.from_email, [email]
            )
            email_message.send()
        return super().form_valid(form)
