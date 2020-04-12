from django.urls import path
from . import views

urlpatterns = [

    path('me/', views.list_of_RPD, name='manage_rpd_list'),
    #path('create/', views.RpdCreateView, name='course_create'),
    path('<slug>/send/', views.message_send, name='send_message'),
    path('<slug>/edit/', views.file_send, name='course_edit'),
    #path('<pk>/edit/', views.RpdUpdateView.as_view(), name='course_edit'),
    #path('<slug>/delete/', views.RpdDeleteView.as_view(), name='course_delete'),
    path('<slug>/assignment/', views.assign_RPD, name='rpd_assigment_list'),
]