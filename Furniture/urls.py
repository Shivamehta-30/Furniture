"""Furniture URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth.views import LoginView,LogoutView
from django.conf import settings
from django.conf.urls.static import static
from users.views import dashboard
urlpatterns = [
    path("",LoginView.as_view(template_name='users/login.html'),name="login"),
    path("logout",LogoutView.as_view(template_name='users/logout.html'),name="logout"),
    path('admin/', admin.site.urls),
    path('users/',include('users.urls')),
    path('category/',include('category.urls')),
    path('material/',include('material.urls')),
    path('OwnerPayment/',include('OwnerPayment.urls')),
    path('supplier/',include('supplier.urls')),
    path('customer/',include('customer.urls')),
    path('Employee/',include('employee.urls')),
    path('subcategory/',include('subcategory.urls')),
    path('customerpayment/',include('customerpayment.urls')),
    path('Supplierpayment/', include('Supplierpayment.urls')),
    path('product/',include('product.urls')),
    path('productin/',include('productin.urls')),
    path('productout/',include('productout.urls')),
    path('inward_purchase/', include('inward_purchase.urls')),
    path('outward_purchase/', include('outward_purchase.urls')),
    path('loss/', include('loss.urls')),
    path("dashboard/",dashboard,name="dashboard")

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
