from django.core.cache import cache
from Catalog.models import Category


def get_cached_categories():
    categories = cache.get('categories')
    if not categories:
        categories = list(Category.objects.all())
        cache.set('categories', categories, 60 * 15)
    return categories
