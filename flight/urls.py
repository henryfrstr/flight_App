from django.urls import path
from .views import FlightView, ResevationView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('flights', FlightView)
router.register('resv', ResevationView)

urlpatterns = [

]

urlpatterns += router.urls
