from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from pet.views import SexViewSet, PetInfoViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'pet_info', PetInfoViewSet)
router.register(r'sex', SexViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
]
