from blog.views import (
    PostCreateAPIView, PostListAPIView, PostDeleteAPIView, PostUpdateAPIView,
    PostListView, PostDetailView, vue_view, PostDetailAPIView
    )
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='blog/index.html')),
    path('admin/', admin.site.urls),
    # rest api
    path('schema.yml', TemplateView.as_view(template_name="blog/schema.yml", content_type='text/yaml')),
    path('api/detail/<int:pk>/', PostDetailAPIView.as_view(), name='api_post_detail'),
    path('api/create/', PostCreateAPIView.as_view(), name='api_post_create'),
    path('api/list/', PostListAPIView.as_view(), name='api_post_list'),
    path('api/delete/<int:pk>/', PostDeleteAPIView.as_view(), name='api_post_delete'),
    path('api/update/<int:pk>/', PostUpdateAPIView.as_view(), name='api_post_update'),
    # django
    path('django/list/', PostListView.as_view(), name='post_list'),
    path('django/detail/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    # Vue
    path('vue-blog/', vue_view, name='vue_blog'),
]
