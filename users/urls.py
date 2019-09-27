from django.conf.urls import url
from django.urls import path, include

from .views import *


urlpatterns = [
    path('<int:pk>/', SingleProfileView.as_view()),
    path('', ProfileView.as_view()),
    # path('users/<int:pk>/', ProfileEditDeleteRetrieveView.as_view()),
    # path('users/', ProfileListCreateView.as_view()),
]
