from rest_framework.routers import DefaultRouter
from django.urls import include, path
from post import views

router = DefaultRouter()
router.register('', views.PostViewSet)

urlpatterns = [
    path('', include(router.urls))
]
