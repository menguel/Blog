from django.urls import path
from authentication.views import home, register, logIn, logOut, activate

urlpatterns = [
    path('register', register, name='register' ),
    path('', logIn, name='login'),
    path('logout', logOut, name='logout'),
    path('activate/<uidb64>/<token>', activate, name="activate" )
]