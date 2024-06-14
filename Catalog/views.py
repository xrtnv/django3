from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from Catalog.models import Category, Product, BlogPost


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


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/product_details.html'


class ProductCreateView(CreateView):
    model = Product
    template_name = 'product/product_form.html'
    fields = ("name", "description", "picture", "category", "price")
    success_url = reverse_lazy('shop:product_list')


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
    fields = ("title", "content", "preview_image", "is_published")
    template_name = 'product/blogpost_form.html'
    success_url = reverse_lazy('shop:blogpost_list')

    def get_success_url(self):
        return reverse('shop:blogpost_detail', kwargs={'slug': self.object.slug})


class BlogPostUpdateView(UpdateView):
    model = BlogPost
    fields = ("title", "content", "preview_image", "is_published")
    template_name = 'product/blogpost_form.html'
    context_object_name = 'blogposts'
    success_url = reverse_lazy('shop:blogpost_list')

    def get_success_url(self):
        return reverse('shop:blogpost_detail', kwargs={'slug': self.object.slug})


class BlogPostDeleteView(DeleteView):
    model = BlogPost
    template_name = 'product/confirm_delete_blogpost.html'
    success_url = reverse_lazy('shop:blogpost_list')
