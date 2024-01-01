from django.urls import path
from .views import UserSignupView, UserLoginView, AcceptUserView

app_name = 'accounts'
urlpatterns = [
    path('signup/', UserSignupView.as_view(), name='signup'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('accept_user/', AcceptUserView.as_view(), name='accept_user'),
]
