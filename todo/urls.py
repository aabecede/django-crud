from django.urls import path

from .views import index, createView, show

app_name = "todo"
urlpatterns = [
    path('', index, name="index"),
    path('<int:task_id>', show, name="show"),
    path('create', createView, name="create")
]