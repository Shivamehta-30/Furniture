from django.urls import path
from .views import *
urlpatterns=[
    path("new/", NewCustomerPayment.as_view(), name="Customerpayment-new"),
    path("view/", ViewCustomerPayment.as_view(), name="Customerpayment-view"),
    path("update/<int:pk>", UpdateCustomerPayment.as_view(), name="Customerpayment-update"),
    path("delete/<int:pk>", DeleteCustomerPayment.as_view(), name="Customerpayment-delete")

]