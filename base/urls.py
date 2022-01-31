from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),


    path('friends/', views.friends,name='friends'),
    path('add-friend/<str:pk>', views.addfriend, name='add-friend'),
    path('friends/removefriend/', views.removefriend,name='removefriend'),

    path('friends/checkview/', views.checkview, name='checkview'),
    path('', views.home, name="home"),
    path('profile/<str:pk>/',views.userProfile, name="user-profile"),
    
    path('chat', views.chat, name='chat'),
    path('chat/<str:room_name>/', views.room, name='room'),

    # path('add-friend/<int:id>/',views.send_request, name='add-friend'),
    path('accept/<int:pk>/',views.accept_request, name='accept'),


]