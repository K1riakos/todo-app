from django.urls import path
from .views import Index, EditTodo, DeleteTodo

urlpatterns = [
    path("", Index.as_view(), name="home"),
    path("create/", Index.as_view(), name="create"),
    path("update/", EditTodo.as_view(), name="update"),
    path("delete/<id>/", DeleteTodo.as_view(), name="delete"),
]
