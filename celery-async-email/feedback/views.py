from feedback.forms import FeedbackForm
from django.views.generic.edit import FormView


# Create your views here.
class FeedbackFormView(FormView):
    template_name = "feedback/feedback.html"
    form_class = FeedbackForm
    success_url = "/"

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)
