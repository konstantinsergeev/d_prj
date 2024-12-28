from django.contrib.admin.utils import model_ngettext
from django.shortcuts import render, get_object_or_404
from django.template.context_processors import request
from django.views import generic
from django.contrib.sites.shortcuts import get_current_site
from .models import Question
# Create your views here.


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"
    current_site = get_current_site(request)
    def get_queryset(self):
        return Question.objects.order_by("-pub_date")[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"
