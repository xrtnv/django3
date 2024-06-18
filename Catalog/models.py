from django.db import models
from user.models import User


class Category(models.Model):
    name = models.CharField(verbose_name='Наименование категории', help_text="Введите наименование категории",
                            blank=True, null=True)
    description = models.TextField(verbose_name='Описание категории', help_text="Введите описание категории",
                                   blank=True, null=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(verbose_name='Наименование', help_text="Введите наименование")
    description = models.TextField(verbose_name='Описание', help_text="Введите описание")
    picture = models.ImageField(verbose_name='Изображение',blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, verbose_name='Категория',
                                 help_text="Введите категорию",
                                 null=True, blank=True, related_name="products")
    price = models.CharField(verbose_name='Цена', help_text="Введите цену")
    create_at = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name='Дата создания',
                                     help_text="Введите дату создания")
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name='Дата последнего изменения',
                                      help_text="Введите дату создания последнего изменения")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products', verbose_name='Создатель',
                              blank=True, null=True)
    is_published = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['name', 'description', 'category', 'price', 'create_at', 'updated_at']
        permissions = [
            ("can_cancel_publication", "Может отменять публикацию продукта"),
            ("can_change_description_any", "Может менять описание любого продукта"),
            ("can_change_category_any", "Может менять категорию любого продукта"),
        ]

    def __str__(self):
        return self.name


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='versions')
    version_number = models.CharField(max_length=20)
    version_name = models.CharField(max_length=255)
    is_current = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Версия товара"
        verbose_name_plural = "Версии товара"

    def __str__(self):
        return f"{self.version_name} ({self.version_number})"
