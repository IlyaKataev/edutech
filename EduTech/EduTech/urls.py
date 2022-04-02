"""EduTech URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.views.generic import TemplateView
from edutech_app.views import Register
from edutech_app.views import show_stream
from edutech_app.views import show_main
from edutech_app.views import show_info
from edutech_app.views import show_teachers
from edutech_app.views import show_courses

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='base.html'), name='home'),
    path('users/', include('django.contrib.auth.urls')),
    path('users/register/', Register.as_view(), name='register'),
    path('stream/', show_stream),
    path('courses/', show_courses),
    path('info/', show_info),
    path('main/', show_main),
    path('teachers/', show_teachers),

]
