from django.urls import path

from . import views


app_name = 'project'


urlpatterns = [
    path('', views.projects, name='projects'),
    path('add/', views.add, name='add'),
    path('<uuid:pk>/', views.project, name='project'),
    path('<uuid:pk>/edit/', views.edit, name='edit'),
    path('<uuid:pk>/delete/', views.delete, name='delete'),
    path('<uuid:project_id>/files/upload/', views.upload_file, name='upload_file'),
    path('<uuid:project_id>/files/<uuid:pk>/delete/', views.delete_file, name='delete_file'),
    path('<uuid:project_id>/notes/add/', views.add_note, name='add_note'),
    path('<uuid:project_id>/notes/<uuid:pk>/', views.note_detail, name='note_detail'),
    path('<uuid:project_id>/notes/<uuid:pk>/edit/', views.note_edit, name='note_edit'),
    path('<uuid:project_id>/notes/<uuid:pk>/delete/', views.note_delete, name='note_delete'),
]