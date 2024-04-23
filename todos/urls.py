from django.urls import path
from todos import views

urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('add/', views.add_todo, name='add_todo'),
    path('<int:id>/delete/', views.delete_todo, name='delete_todo'),
    path('<int:id>/edit/', views.edit_todo, name='edit_todo'),
]
