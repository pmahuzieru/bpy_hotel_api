from django.contrib import admin
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import RoomViewSet, ReservationViewSet
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

router = DefaultRouter()
router.register('rooms', RoomViewSet)
router.register('reservations', ReservationViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-token/', obtain_auth_token, name='api_token'), 
    path('', include(router.urls)),   

    # Spectacular routes
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]
