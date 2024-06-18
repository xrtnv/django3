from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from blog.apps import BlogConfig
from blog.views import BlogPostCreateView, BlogPostUpdateView, BlogPostListView, BlogPostDetailView, BlogPostDeleteView

app_name = BlogConfig.name

urlpatterns = [
                  path('create-post/', BlogPostCreateView.as_view(), name='blogpost_create'),
                  path('post-update/<slug>/', BlogPostUpdateView.as_view(), name='blogpost_update'),
                  path('post-list/', BlogPostListView.as_view(), name='blogpost_list'),
                  path('post-detail/<slug>/', BlogPostDetailView.as_view(), name='blogpost_detail'),
                  path('post-delete/<slug>/', BlogPostDeleteView.as_view(), name='blogpost_delete'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
