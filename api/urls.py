from django.urls import path
from . import views

urlpatterns = [
    path('api/task-list/', views.task_list,name="task-list"),
    path('api/task-detail/<str:pk>/', views.task_detail, name="task-detail"),
    path('api/task-create/', views.task_create, name="task-create"),
    path('api/task-update/<str:pk>', views.task_update, name="task-update"),
    path('api/task-delete/<str:pk>', views.task_delete, name="task-delete"),
]
