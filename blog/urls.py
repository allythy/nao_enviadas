from django.urls import path

from .views import AddLetterView, HomeView, LetterDetailView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path('letter/<int:pk>', LetterDetailView.as_view(), name='letter-datail'), 
    path('add_letter/', AddLetterView.as_view(), name='add-letter'),
]
