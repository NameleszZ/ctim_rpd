from django.urls import path
from . import views

urlpatterns = [

    path('me/', views.list_of_RPD, name='manage_rpd_list'),
    path('<slug>/', views.profile_view, name='profile'),
    path('<slug>/send/', views.message_send, name='send_message'),
    path('<slug>/edit/', views.file_send, name='course_edit'),
    path('<slug>/assignment/', views.assign_RPD, name='rpd_assigment_list'),
]