from .models import Post
from .serializers import PostSerializer
from django.shortcuts import render
from django.utils import timezone
from django.views.generic import ListView, DetailView
from rest_framework import generics
from rest_framework.generics import get_object_or_404

def vue_view(request):

    context = {}
    context['vue_element'] = 'vueblog'
    return render(request, 'blog/vue_blog.html', context)

class PostDetailView(DetailView):

    context_object_name = 'post'
    template_name = 'blog/django_detail.html'
    model = Post

class PostListView(ListView):
    
    queryset = Post.objects.all()
    context_object_name = 'post_list'
    template_name = 'blog/django_list.html'

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        qs = qs.filter(published__lte=timezone.now())
        return qs

    class Meta:
        model = Post


class PostDetailAPIView(generics.RetrieveAPIView):
    
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class PostCreateAPIView(generics.CreateAPIView):

    serializer_class = PostSerializer

    def perform_create(self, serializer):
            serializer.save(published=timezone.now())

class PostListAPIView(generics.ListAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self, *args, **kwargs):
        nowish = timezone.now()
        qs = super().get_queryset(*args, **kwargs)
        qs = qs.filter(published__lte=nowish)
        return qs



class PostDeleteAPIView(generics.DestroyAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get_object(self):
        queryset = self.get_queryset()
        filter_kwargs = {'pk': self.kwargs['pk']}
        return get_object_or_404(queryset, **filter_kwargs)



class PostUpdateAPIView(generics.UpdateAPIView):

    serializer_class = PostSerializer
    queryset = Post.objects.all()