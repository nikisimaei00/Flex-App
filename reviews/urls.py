from django.urls import path
from . import views

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path("api/hostaway/", views.hostaway_reviews_api, name="hostaway_api"),
    path("import-hostaway/", views.import_hostaway_to_db, name="import_hostaway"),
    path("api/google-demo/", views.google_reviews_demo, name="google_reviews_demo"),
]
