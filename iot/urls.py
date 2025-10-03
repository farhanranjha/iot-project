from django.contrib import admin
from django.urls import path
from iot.views import PingReciever
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'iot', PingReciever, basename='iot')
urlpatterns = [
    path('admin/', admin.site.urls),
    *router.urls,
]
