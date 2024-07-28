from django.contrib import admin
from django.urls import path, include
from django.views.decorators.cache import cache_page
from Catalog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Catalog.urls', namespace='shop')),
    path('user/', include('user.urls', namespace='user')),
    path('blog/', include('blog.urls', namespace='blog')),
    path('product/<int:id>/', cache_page(60 * 15)(views.ProductDetailView.as_view()), name='product_detail'),
]
