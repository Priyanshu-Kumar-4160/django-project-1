from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NoteViewSet, RestaurantViewSet, MenuItemViewSet




router = DefaultRouter()
router.register(r'restaurants', RestaurantViewSet)
router.register(r'menu-items', MenuItemViewSet)

urlpatterns = [
    #path('', include(router.urls)),
    path('api/restaurant/', include('restaurant.urls')),

]