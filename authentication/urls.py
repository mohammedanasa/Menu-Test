from django.urls import path
from . import views
from .views import dashboard,login_user, logout_user, register_user
from django.contrib.auth.views import LogoutView


urlpatterns = [

    path('', views.dashboard, name="dashboard"),
	path('login/',views.login_user, name="login"),
	path('logout/', views.logout_user, name="logout"),
	path('signup/', views.register_user, name="signup"),
]