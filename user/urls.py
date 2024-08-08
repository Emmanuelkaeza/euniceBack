from django.urls import path, include
from .views import UserRegisterView, UserLoginView, UserListView


urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='user-register'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('users/', UserListView.as_view(), name='user-list'),
]
