from django.urls import path
from .views import comments,check_spam,delete_comment,login_view,logout_view,create_comment,register

urlpatterns = [
    path('',comments,name='comments'),
    path('check_spam',check_spam,name='check_spam'),
    path('comment/<int:pk>/',delete_comment,name='delete_comment'),
    path('login/', login_view, name='login'),
    path('logout/',logout_view, name='logout'),
    path('create-comment/',create_comment, name='create_comment'),
    path('register/', register, name='register'),
]