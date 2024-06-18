from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from Catalog.apps import CatalogConfig
from Catalog.views import ProductListView, ProductDetailView, ProductCreateView, HomeView, ProductUpdateView

app_name = CatalogConfig.name

urlpatterns = [
                  path('', HomeView.as_view(), name='home'),
                  path('base/', ProductListView.as_view(), name='product_list'),
                  path('product/<int:pk>/', ProductDetailView.as_view(), name='product_details'),
                  path('product/create/', ProductCreateView.as_view(), name='product_create'),
                  path('product/update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
