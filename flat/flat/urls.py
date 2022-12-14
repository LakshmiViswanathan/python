"""flat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="home"),
    path('contact', views.contact, name="contact"),
    path('handle_contact', views.handle_contact, name="handle_contact"),
    path('logout', views.mylogout, name="logout"),
    path('land-detail', views.detail, name="detail"),
    path('handle_add_booking', views.handle_add_booking, name="handle_add_booking"),
    path('delete_booking', views.delete_booking, name="delete_booking"),
    path('delete_booking_user', views.delete_booking_user, name="delete_booking_user"),
    path('edit_booking_user', views.edit_booking_user, name="edit_booking_user"),
    path('handle_edit_booking', views.handle_edit_booking, name="handle_edit_booking"),
    
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
