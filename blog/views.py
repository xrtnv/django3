from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from blog.forms import BlogPostForm
from blog.models import BlogPost


class BlogPostListView(ListView):
    model = BlogPost
    template_name = 'blogpost_list.html'
    context_object_name = 'blogposts'
    paginate_by = 10

    def get_queryset(self):
        return BlogPost.objects.filter(is_published=True)


class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = 'blogpost_detail.html'
    context_object_name = 'blogpost'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.views_count += 1
        obj.save()
        return obj


class BlogPostCreateView(CreateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'blogpost_form.html'
    success_url = reverse_lazy('blog:blogpost_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:blogpost_detail', kwargs={'slug': self.object.slug})


class BlogPostUpdateView(UpdateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'blogpost_form.html'
    context_object_name = 'blogposts'
    success_url = reverse_lazy('blog:blogpost_list')

    def get_success_url(self):
        return reverse('blog:blogpost_detail', kwargs={'slug': self.object.slug})

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if not self.request.user == obj.owner and not self.request.user.is_superuser:
            raise PermissionDenied("Недостаточно прав.")
        return obj

    def get_form_class(self):
        user = self.request.user
        if self.object.owner == user or user.is_superuser or user.has_perms([
            "shop.can_cancel_publication",
            "shop.can_change_description_any",
            "shop.can_change_category_any"
        ]):
            return BlogPostForm
        else:
            raise PermissionDenied("Недостаточно прав.")


class BlogPostDeleteView(DeleteView):
    model = BlogPost
    template_name = 'blogpost_confirm_delete.html'
    success_url = reverse_lazy('blog:blogpost_list')
