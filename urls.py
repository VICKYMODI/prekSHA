from django.urls import path,include
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from .views import UserViewSet,PhotographerViewSet,RatingViewSet,BookingViewSet

router = routers.DefaultRouter()
router.register('shoot',UserViewSet)
#router.register('Weds',WeddingViewSet)
router.register('Photographer',PhotographerViewSet)
router.register('Rating',RatingViewSet)
router.register('Booking',BookingViewSet)


urlpatterns = [
    path('',include(router.urls))
] 