from autoslug import AutoSlugField
from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок поста")
    slug = AutoSlugField(populate_from='title', unique=True, verbose_name="Ссылка на пост")
    content = models.TextField(verbose_name="Текст поста")
    preview_image = models.ImageField(upload_to="blog_preview", verbose_name="Превью поста", null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    is_published = models.BooleanField(default=False, verbose_name="Опубликованные посты")
    views_count = models.PositiveIntegerField(default=0, verbose_name="Количество просмотров")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        ordering = ['-created_at']
