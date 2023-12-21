from django.urls import path
from .views import *
urlpatterns = [
    path('', Home,name='Home'),
    path('sigup/', signUp,name='signup'),
    path('sigin/', signIn,name='signin'),
    path('profile/', userProfile,name='profile'),
    path('friend-req/', friendRequest,name='friendRequest'),
    path('inbox/', chatlist,name='inbox'),
    path('message/', message,name='message'),
    path('forgot-Password/', forgotPassword,name='forgotPassword'),
    path('logout/',user_logout, name='logout'),
]