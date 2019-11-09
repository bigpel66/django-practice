from rest_framework import viewsets
from mystorage.models import Essay
# from mystorage.serializers import EssaySerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Essay.objects.all()
    # serializer = EssaySerializer