from django.forms import inlineformset_factory
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from Catalog.forms import ProductForm, BlogPostForm, VersionForm
from Catalog.models import Category, Product, BlogPost, Version


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


class ProductListView(ListView):
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


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/product_details.html'


class ProductCreateView(CreateView):
    model = Product
    template_name = 'product/product_form.html'
    form_class = ProductForm
    success_url = reverse_lazy('shop:product_list')


class ProductUpdateView(UpdateView):
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


class BlogPostListView(ListView):
    model = BlogPost
    template_name = 'product/blogpost_list.html'
    context_object_name = 'blogposts'
    paginate_by = 10

    def get_queryset(self):
        return BlogPost.objects.filter(is_published=True)


class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = 'product/blogpost_detail.html'
    context_object_name = 'blogpost'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.views_count += 1
        obj.save()
        return obj


class BlogPostCreateView(CreateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'product/blogpost_form.html'
    success_url = reverse_lazy('shop:blogpost_list')

    def get_success_url(self):
        return reverse('shop:blogpost_detail', kwargs={'slug': self.object.slug})


class BlogPostUpdateView(UpdateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'product/blogpost_form.html'
    context_object_name = 'blogposts'
    success_url = reverse_lazy('shop:blogpost_list')

    def get_success_url(self):
        return reverse('shop:blogpost_detail', kwargs={'slug': self.object.slug})


class BlogPostDeleteView(DeleteView):
    model = BlogPost
    template_name = 'product/confirm_delete_blogpost.html'
    success_url = reverse_lazy('shop:blogpost_list')
