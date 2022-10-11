from .models import Post
from .serializers import PostSerializer
from rest_framework import viewsets, mixins
from rest_framework.response import Response


class PostViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):

    queryset = Post.objects.all()
    serializer_class = PostSerializer