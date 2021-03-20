from django.db.models import Q
from django.views.generic import CreateView, DeleteView, ListView

from .forms import LetterForm
from .models import Letter


class HomeView(ListView):
    model = Letter
    template_name = "home.html"
    ordering = ["-letter_date"]


class LetterDetailView(DeleteView):
    model = Letter
    template_name = 'letter_details.html'


class AddLetterView(CreateView):
    model = Letter
    form_class = LetterForm
    template_name = 'add_letter.html'
    # fields = '__all__'


class SearchResultsView(ListView):
    model = Letter
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Letter.objects.filter(Q(name__contains=query))
        return object_list
    # queryset = Letter.objects.filter(name__contains='allythy')
