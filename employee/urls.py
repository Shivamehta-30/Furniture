from django.urls import path
from .views import *
urlpatterns=[
    path("new/", NewEmployee.as_view(), name="Employee-new"),
    path("view/", ViewEmployee.as_view(), name="Employee-view"),
    path("update/<int:pk>", UpdateEmployee.as_view(), name="Employee-update"),
    path("delete/<int:pk>", DeleteEmployee.as_view(), name="Employee-delete"),
    path("detail/<int:pk>",DetailEmployee.as_view(), name="Employee-detail")


]