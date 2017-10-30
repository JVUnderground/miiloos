from django.conf.urls import url, include
from rest_framework import routers
from graphs import views

router = routers.DefaultRouter()
router.register(r'comed', views.ComedFiveMinFeedViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]