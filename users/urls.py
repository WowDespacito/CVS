from django.urls import path

from users.views import UserView, LoginView

urlpatterns=[
    path('user/', UserView.as_view(), name='user'),
    path('login/', LoginView.as_view(), name='login'),
]