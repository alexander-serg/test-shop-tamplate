from django.db import models
from django.urls import reverse

class Item(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    description = models.TextField(blank=True, verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")


    def __str__(self):
        return '{}'.format(self.name)

    def get_absolute_url(self):
        return reverse('shop:post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['-time_create', 'name']
        index_together = (('id', 'slug'),)

class ItemImage(models.Model):
    itpm = models.ForeignKey(Item, blank=True, null=True,on_delete=models.CASCADE, default=True, related_name='itpm',)
    image = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото")
    is_main = models.BooleanField(default=False, verbose_name="Главная")
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")

    def __str__(self):
        return '{}'.format(self.id)

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'