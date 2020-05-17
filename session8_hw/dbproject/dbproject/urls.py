"""dbproject URL Configuration

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
from dbapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_defined_in_view, name="index_i_will_use_in_html"),
    path('new', views.new_defined_in_view, name="new_i_will_use_in_html"),
    path('detail/<int:pk_clicked>', views.detail_defined_in_view, name="detail_i_will_use_in_html"),
    path('movie',views.movie_defined_in_view, name="movie_i_will_use_in_html"),
    path('drama', views.drama_defined_in_view, name="drama_i_will_use_in_html"),
    path('entertain', views.entertain_defined_in_view, name="entertain_i_will_use_in_html"),
]
