from django.urls import path
from todolist import views

urlpatterns = [
    path('', views.TodoListView.as_view(), name='todo_list_view'),
    path('<int:todo_id>/', views.TodoDetailView.as_view(),
         name='todo_detail_view'),
]
