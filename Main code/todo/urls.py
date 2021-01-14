from django.contrib import admin
from django.urls import path, include
from .import views
app_name='todo'

urlpatterns = [
    path('',views.TaskListView,name='task-list'),
    path('add/task/',views.AddTaskView,name='add-task'),
    path('edit/task/<int:id>',views.EditTaskView,name='edit-task'),
    path('delete/task/<int:id>',views.DeleteTaskView,name='delete-task'),
    path('login/',views.LoginView,name='login'),
    path('register/',views.RegisterView,name='register'),
    path('logout/',views.LogoutView,name="logout"), 
    path('rep/',views.RepView,name="rep"), 
    path('profile/',views.ProfileView,name="profile"), 
    path('topusers/',views.HallOfFame,name="topusers"), 

]
