
from django.urls import path
from .views import my_media, index, logout_session, register, remove_file

urlpatterns = [
    path('', index),
    path('docdrive/logout', logout_session, name="logout"),
    path('docdrive/account/register', register, name="register"),
    path('docdrive/media', my_media, name='my_media'),    
    path('docdrive/media/remove', remove_file, name='remove_file'),    
]
