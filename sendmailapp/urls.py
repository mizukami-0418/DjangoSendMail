from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('send_email/', views.send_test_email, name='send_email'),
]
