from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_index_page, name='show_index_page'),
]
