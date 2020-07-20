"""practice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
import main.views
import comunity.views
import login.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main.views.main, name="main"),
    path('comunity/', comunity.views.main_comu, name="comunity"),
    path('no/', main.views.notyet, name="notyet"),
    path('comunity/write/', comunity.views.post, name="post"),
    path('comunity/create', comunity.views.create, name="create"),
    path('comunity/delete', comunity.views.delete, name="delete"),
    path('comunity/<int:post_id>/', comunity.views.detail, name="detail"),
    path('login/', login.views.login, name="login"),
    path('signup/', login.views.signup, name="signup"),
    path('logout/', login.views.logout, name="logout"),
    path('comunity/<int:post_id>/edit_page', comunity.views.edit_page, name="edit_page"),
    path('comunity/<int:post_id>/edit', comunity.views.edit, name="edit"),
] 
