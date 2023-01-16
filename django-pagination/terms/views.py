from django.views.generic import ListView
from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import JsonResponse

from terms.models import Keyword


class AllKeywordsView(ListView):
    model = Keyword
    template_name = "terms/base.html"


class KeywordListView(ListView):
    paginate_by = 5
    model = Keyword


def listing(request, page):
    keywords = Keyword.objects.all().order_by("name")
    paginator = Paginator(keywords, 2)
    page_object = paginator.get_page(page)
    page_object.adjusted_elided_pages = paginator.get_elided_page_range(page)
    context = {"page_obj": page_object}
    return render(request, "terms/keyword_list.html", context)


def listing_api(request):
    page_number = request.GET.get("page", 1)
    per_page = request.GET.get("per_page", 2)
    startswith = request.GET.get("startswith", "")
    keywords = Keyword.objects.filter(name__startswith=startswith)
    paginator = Paginator(keywords, per_page)
    page_obj = paginator.get_page(page_number)
    data = [{"name": kw.name} for kw in page_obj.object_list]

    payload = {
        "page": {
            "current": page_obj.number,
            "has_next": page_obj.has_next(),
            "has_previous": page_obj.has_previous(),
        },
        "data": data,
    }
    return JsonResponse(payload)
