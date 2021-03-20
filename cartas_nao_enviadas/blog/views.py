from django.views.generic import ListView, DeleteView, CreateView
from .models import Letter
from .forms import LetterForm


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
