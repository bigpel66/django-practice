from userpost.models import UserPost
from userpost.serializer import UserPostSerializer
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication

class UserPostViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    queryset = UserPost.objects.all()
    serializer_class = UserPostSerializer

    filter_backends = [SearchFilter]
    search_fields = ('title', 'body',)

    def get_queryset(self):
        qs = super().get_queryset()

        #.filter .exclude
        # qs = qs.filter(author__id = 1)
        # qs = qs.exclude(author__id = 1

        #logged in user filtering
        # qs = qs.filter(author=self.request.user)

        #if logged in user filtering, else empty filtering
        if self.request.user.is_authenticated:
            qs = qs.filter(author=self.request.user)
        else :
            qs = qs.none()

        return qs
        

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)