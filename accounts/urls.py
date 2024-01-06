from django.urls import path
from .views import UserSignupView, UserLoginView, AcceptUserView, ProfileView, ProfileEditView \
    ,PasswordResetV

app_name = 'accounts'
urlpatterns = [
    path('signup/', UserSignupView.as_view(), name='signup'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('accept_user/', AcceptUserView.as_view(), name='accept_user'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('profile/edit/<int:pk>/', ProfileEditView.as_view(), name='profile_edit'),
    path('password_reset_view/', PasswordResetV.as_view(), name='password_reset_view'),
]
