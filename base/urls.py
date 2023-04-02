from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('room/<str:room_id>', views.room, name='room'),
    path('create-room/', views.createRoom, name='create-room'),
    path('update-room/<str:room_id>', views.updateRoom, name='update-room'),
    path('delete-room/<str:room_id>', views.deleteRoom, name='delete-room'),
    path('login/', views.loginPage, name='login'),
    path('register/', views.registerPage, name='register'),
    path('logout/', views.logoutUser, name='logout'),
    path('delete-message/<str:message_id>', views.deleteMessage, name='delete-message'),
    path('profile/<str:user_id>', views.userProfile, name='user-profile'),
    path('update-user/', views.updateUser, name='update-user'),
    path('topics/', views.topicsPage, name='topics'),
    path('activity/', views.activityPage, name='activity'),

]
