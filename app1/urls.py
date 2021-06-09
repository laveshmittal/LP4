from . import views
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [path("a", views.app1homepage),
               path('', views.loginview),
               path("dashboard", views.dashboard),

               path("predictfunc", views.predictfunc),
               path('lavesh/', admin.site.urls),
               path("predictcount", views.predictcount)


               ]
