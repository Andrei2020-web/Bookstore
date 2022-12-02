from django.urls import path
from .views import HomePageView, AboutPageView

urlpatterns = [
    # добавлен url домашней страницы
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
]