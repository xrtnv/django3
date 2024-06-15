from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from Catalog.apps import CatalogConfig
from Catalog.views import ProductListView, ProductDetailView, ProductCreateView, BlogPostCreateView, \
    BlogPostUpdateView, BlogPostListView, BlogPostDetailView, BlogPostDeleteView, HomeView, ProductUpdateView

app_name = CatalogConfig.name

urlpatterns = [
                  path('', HomeView.as_view(), name='home'),
                  path('base/', ProductListView.as_view(), name='product_list'),
                  path('product/<int:pk>/', ProductDetailView.as_view(), name='product_details'),
                  path('product/create/', ProductCreateView.as_view(), name='product_create'),
                  path('product/update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),

                  path('create-post/', BlogPostCreateView.as_view(), name='blogpost_create'),
                  path('post-update/<slug>/', BlogPostUpdateView.as_view(), name='blogpost_update'),
                  path('post-list/', BlogPostListView.as_view(), name='blogpost_list'),
                  path('post-detail/<slug>/', BlogPostDetailView.as_view(), name='blogpost_detail'),
                  path('post-delete/<slug>/', BlogPostDeleteView.as_view(), name='blogpost_delete'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
