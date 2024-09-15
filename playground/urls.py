from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello, name='hello'),   # URL for 'hello' view
    path('', views.index, name='index'),         # URL for the form (index page)
    path('get_info/', views.get_info, name='get_info'),  # URL for processing the form
]
