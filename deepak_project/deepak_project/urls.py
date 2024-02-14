"""
URL configuration for deepak_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from deepak_app import views
from django.conf.urls.static import static
from deepak_project import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.login,name='login'),
    path('login/',views.login,name='login'),
    path('register/',views.registration_view,name='register'),
    path('home/',views.home,name='home'),
    path('book_details/',views.book_details_view,name='book_details'),
    path('book_submit/',views.book_submit,name='book_submit'),
    path('book_submit_admin/',views.book_submit_admin,name='book_submit_admin'),
    path('delete_book/(?P<id>\d+)$',views.delete_book,name="delete_book"),
    path('my_details/',views.my_details,name='my_details'),
    path('edit_details/',views.edit_details,name='edit_details'),
    path('change_password/',views.change_password,name='change_password')
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
