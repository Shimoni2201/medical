"""medical URL Configuration

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
from django.urls import path, include
from django.contrib.auth.views import LogoutView, LoginView
from django .conf import settings
from django.conf.urls.static import static
from users.views import dashboard,get_total_sales_by_month, loss_by_month

urlpatterns = [
    path("",LoginView.as_view(template_name='users/login.html'),name="login"),
    path("logout",LogoutView.as_view(template_name='users/logout.html'),name="logout"),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('product/', include('product.urls')),
    path('customer/', include('customer.urls')),
    path('supplier/', include('supplier.urls')),
    path('employee/', include('employee.urls')),
    path('prodinward/', include('prodinward.urls')),
    path('inward_purchase/', include('inward_purchase.urls')),
    path('prodoutward/', include('prodoutward.urls')),
    path('outward_purchase/', include('outward_purchase.urls')),
    path("loss/", include("loss.urls")),
    path("dashboard/", dashboard, name="dashboard"),
    path("total_sales_by_month/", get_total_sales_by_month, name="total_sale_by_month"),
    path("loss_by_month/", loss_by_month, name="loss_by_month")
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)