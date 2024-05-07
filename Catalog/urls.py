from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from Catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
