from django.urls import path
from .views import HomePageView

urlpatterns = [
    # добавлен url домашней страницы
    path('', HomePageView.as_view(), name='home')
]