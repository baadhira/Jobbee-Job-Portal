from django.urls import path
from .import views

urlpatterns =[
    path('register/',views.register,name='register'),
    path('me/',views.currentUser,name='currentUser'),
    path('me/update/',views.updateUser,name='updateUser'),
    path('upload/resume/',views.uploadResume,name='uploadResume'),
 
]