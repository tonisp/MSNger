from django.urls import path
from . import views
from django.urls import include

urlpatterns = [
    path('', views.home, name='home'),
    path('room/<str:room>/', views.room, name='room'),
    path('checkview', views.checkview, name='checkview'),
    path('send', views.send, name='send'),
    path('getMessages/<int:room_id>/', views.getMessages, name='getMessages'),
    path('login_user', views.login_user, name='login_user'),
    path('registered', views.room, name='registered_room'),
    path('users', views.users, name='users'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('profile/<int:pk>', views.room,  name='registered'),
]
