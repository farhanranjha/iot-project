from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter

from iot.views import PingReciever

router = DefaultRouter()
router.register(r"iot", PingReciever, basename="iot")
urlpatterns = [
    path("admin/", admin.site.urls),
    *router.urls,
]
