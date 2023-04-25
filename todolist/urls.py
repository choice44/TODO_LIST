from django.urls import path
from todolist import views

urlpatterns = [
    path('', views.TodoListView.as_view(), name='todo_list_view'),
    path('<int:todolist_id>/', views.TodoDetailView.as_view(),
         name='todo_list__detail_view'),
]
