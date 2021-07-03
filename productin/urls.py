from django.urls import path
from .views import *
urlpatterns=[
    path("new/", Newproductin.as_view(), name="prodinward-new"),
    path("view/", Viewproductin.as_view(), name="prodinward-view"),
    path("update/<int:pk>", Updateproductin.as_view(), name="prodinward-update"),
    path("delete/<int:pk>", Deleteproductin.as_view(), name="prodinward-delete")
]