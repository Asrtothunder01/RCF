from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('home', views.home, name='home'),
    path('logout/', views.logout_view, name='logout'),
    path('market.html', views.market, name='market'),
]
