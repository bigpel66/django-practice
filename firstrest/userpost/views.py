from userpost.models import UserPost
from userpost.serializer import UserPostSerializer
from rest_framework import viewsets

class UserPostViewSet(viewsets.ModelViewSet):
    queryset = UserPost.objects.all()
    serializer_class = UserPostSerializer