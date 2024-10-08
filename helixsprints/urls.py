from django.contrib import admin
from django.urls import include, path
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("scrum/", include("scrum.urls")),
    path("admin/", admin.site.urls),
]