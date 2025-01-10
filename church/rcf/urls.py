from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('logout/', views.logout_view, name='logout'),
    path('market/', views.market, name='market'),
    path('response/', views.response, name='response'), 
     path('index/',views.index,name='index'),
      path('profile/',views.profile_view,name='profile'),
       path('settings/', views.settings_view, name='settings'),  # Add this path for the response view
]
