from django.urls import path
from .views import register_request, home_page, login_request, logout_request, profile
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('register/', register_request, name="register"),
    path('login/', login_request, name="login"),
    # path('logout/', logout_request, name="logout"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', home_page, name="homepage"),
    path('profile/', profile, name="profile"),
]
