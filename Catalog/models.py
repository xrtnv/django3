from django.db import models


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
    picture = models.ImageField(upload_to='DjangoORM/ProductPictures', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, verbose_name='Категория',
                                 help_text="Введите категорию",
                                 null=True, blank=True, related_name="products")
    price = models.CharField(verbose_name='Цена', help_text="Введите цену")
    create_at = models.DateTimeField(blank=False, null=False, verbose_name='Дата создания',
                                     help_text="Введите дату создания")
    updated_at = models.DateTimeField(blank=False, null=False, verbose_name='Дата последнего изменения',
                                      help_text="Введите дату создания последнего изменения")

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['name', 'description', 'category', 'price', 'create_at', 'updated_at']

    def __str__(self):
        return self.name
