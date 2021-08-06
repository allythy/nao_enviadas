from django.db.models import Q
from django.views.generic import CreateView, DeleteView, ListView
from django.urls import reverse_lazy

from .forms import LetterForm
from .models import Letter


class HomeView(ListView):
    model = Letter
    template_name = "home.html"
    ordering = ["-letter_date"]
    paginate_by = 9

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get("busca")
        if query:
            qs = qs.filter(Q(name__contains=query) | Q(message__contains=query))
        return qs

    def get_context_data(self):
        context = super().get_context_data()
        return {**context, "busca": self.request.GET.get("busca", "")}


class LetterDetailView(DeleteView):
    model = Letter
    template_name = "letter_details.html"


class AddLetterView(CreateView):
    model = Letter
    form_class = LetterForm
    template_name = "add_letter.html"
    success_url = reverse_lazy("home")
