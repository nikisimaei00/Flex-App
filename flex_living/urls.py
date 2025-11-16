from django.contrib import admin
from django.urls import path, include
from reviews import views as review_views

urlpatterns = [
    path("", review_views.home, name="home"),
    path("admin/", admin.site.urls),
    path("reviews/", include("reviews.urls")),
]
