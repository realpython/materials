from django.views.generic import ListView
from terms.models import Keyword


class AllKeywordsView(ListView):
    model = Keyword
