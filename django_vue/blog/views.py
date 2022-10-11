from .models. import Post
from .serializers import PostSerializer
from django.utils import timezone
from rest_framework import generics

class PostCreateAPIView(generics.CreateAPIView):

    serializer_class = PostSerializer


class PostListAPIView(generics.ListAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self, *args, **kwargs):
        nowish = timezone.now()
        qs = super().get_queryset(*args, **kwargs)
        qs = qs.filter(published__gte=nowish)
        return qs


class PostDeleteAPIView(generics.DestroyAPIView):

    serializer_class = PostSerializer

    class Meta:
        model = Reflection


class PostUpdateAPIView(generics.UpdateAPIView):

    serializer_class = PostSerializer
    queryset = Post.objects.all()