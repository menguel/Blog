from django.urls import path
from Article.views import home

urlpatterns = [
    path('', home, name="home")
]
