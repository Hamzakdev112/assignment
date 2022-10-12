from blog.views import (
    PostCreateAPIView, PostListAPIView, PostDeleteAPIView, PostUpdateAPIView,
    PostListView, PostDetailView, vue_view
    )
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    # rest api
    path('schema.yml', TemplateView.as_view(template_name="blog/schema.yml", content_type='text/yaml')),
    path('api/create/', PostCreateAPIView.as_view()),
    path('api/list/', PostListAPIView.as_view()),
    path('api/delete/<int:pk>/', PostDeleteAPIView.as_view()),
    path('api/update/<int:pk>/', PostUpdateAPIView.as_view()),
    # django
    path('django/list/', PostListView.as_view(), name='post_list'),
    path('django/detail/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    # Vue
    path('vue-blog/', vue_view),
]
