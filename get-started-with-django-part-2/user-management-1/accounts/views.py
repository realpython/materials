from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class EditProfileView(UpdateView):
    model = User
    fields = ["username", "first_name"]
    success_url = reverse_lazy("profile")
    template_name = "registration/edit_profile_form.html"

    def get_object(self):
        return self.request.user
