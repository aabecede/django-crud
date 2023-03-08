from django.urls import path

from .views import index, createView, show, updateView, delete

app_name = "todo"
urlpatterns = [
    path('', index, name="index"),
    path('<int:task_id>', show, name="show"),
    path('<int:task_id>/update', updateView, name="update"),
    path('<int:task_id>/delete', delete, name="delete"),
    path('create', createView, name="create")
]