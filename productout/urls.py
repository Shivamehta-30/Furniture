from django.urls import path
from .views import *
urlpatterns=[
    path("new/", Newproductout.as_view(), name="prodoutward-new"),
    path("view/", Viewproductout.as_view(), name="prodoutward-view"),
    path("update/<int:pk>", Updateproductout.as_view(), name="prodoutward-update"),
    path("delete/<int:pk>", Deleteproductout.as_view(), name="prodoutward-delete")
]