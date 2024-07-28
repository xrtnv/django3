from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.forms import inlineformset_factory
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, CreateView, UpdateView
from django.views.generic import ListView
from .services import get_cached_categories
from Catalog.forms import ProductForm, VersionForm
from Catalog.models import Product, Version


class HomeView(ListView):
    model = Product
    template_name = 'product/home.html'
    context_object_name = 'latest_products'
    order_by = '-create_at'
    queryset = Product.objects.order_by('-create_at')[:5]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        latest_products = self.object_list

        for product in latest_products:
            print(f"Название: {product.name}")
            print(f"Описание: {product.description}")
            print(f"Цена: {product.price}")
            print(f"Дата создания: {product.create_at}")
            print()

        return context


class CategoryListView(ListView):
    template_name = 'category_list.html'
    context_object_name = 'categories'

    def get_queryset(self):
        return get_cached_categories()


class ProductListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('user:login')
    model = Product
    template_name = 'product/product_list.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = context["products"]

        for product in products:
            current_version = product.versions.filter(is_current=True).first()
            if current_version:
                product.current_version = {
                    "version_number": current_version.version_number,
                    "version_name": current_version.version_name,
                }
            else:
                product.current_version = None

        return context

    def get_queryset(self):
        return get_cached_categories()


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'product/product_details.html'


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    template_name = 'product/product_form.html'
    form_class = ProductForm
    success_url = reverse_lazy('shop:product_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product/product_form.html'
    success_url = reverse_lazy('shop:product_details')

    def get_success_url(self):
        return reverse("shop:product_details", args=[self.kwargs.get("pk")])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        version_fromset = inlineformset_factory(Product, Version, VersionForm, extra=1)
        if self.request.method == "POST":
            context_data["formset"] = version_fromset(
                self.request.POST, instance=self.object
            )
        else:
            context_data["formset"] = version_fromset(instance=self.object)
        return context_data

    def get_form_class(self):
        user = self.request.user
        if self.object.owner == user or user.is_superuser or user.has_perms(["shop.can_cancel_publication",
                                                                             "shop.can_change_description_any",
                                                                             "shop.can_change_category_any"]):
            return ProductForm
        raise PermissionDenied
