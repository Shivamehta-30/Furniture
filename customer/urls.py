from django.urls import path
from .views import *
urlpatterns=[
    path("new/", NewCustomer.as_view(), name="Customer-new"),
    path("view/", ViewCustomer.as_view(), name="Customer-view"),
    path("update/<int:pk>", UpdateCustomer.as_view(), name="Customer-update"),
    path("delete/<int:pk>", DeleteCustomer.as_view(), name="Customer-delete")

]