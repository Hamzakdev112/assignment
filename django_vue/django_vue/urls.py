from blog.viewsets import PostViewSet
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'post', PostViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/viewset/', include(router.urls)),
    path('schema.yml', TemplateView.as_view(template_name="common/schema.yml", content_type='text/yaml')),
]
