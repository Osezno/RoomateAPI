"""composeexample URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from post import views as post_views
from usr import userviews as user_views
from usr import sessionviews as session_views


urlpatterns = [

    path('admin/', admin.site.urls),
    path('create_post/', post_views.create_post),
    # ABC DE USUARIOS
    path('api/v1/nuevo_usuario/', user_views.nuevo_usuario),
    path('api/v1/eliminar_usuario/', user_views.eliminar_usuario),
    path('api/v1/editar_usuario/', user_views.editar_usuario),
    path('api/v1/ver_usuario/', user_views.ver_usuario),
    path('api/v1/ver_usuarios/', user_views.ver_usuarios),
    # MANEJO DE SESIONES
    path('api/v1/login/', session_views.login),
    path('api/v1/logout/', session_views.logout),
    # path('api/v1/forgot_password/', session_views.forgot_password),

]
