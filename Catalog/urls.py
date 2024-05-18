from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from Catalog.apps import CatalogConfig
from Catalog.views import catalog, product_details

app_name = CatalogConfig.name

urlpatterns = [
    path('', catalog, name='catalog'),
    path('product/<int:pk>/', product_details, name='product_details'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
