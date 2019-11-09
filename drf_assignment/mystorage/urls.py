from rest_framework.routers import DefaultRouter
from django.urls import path, include
from mystorage import views

router = DefaultRouter()
router.register('essay', views.PostViewSet) 
router.register('album', views.AlbumViewSet)
router.register('files', views.FilesViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
