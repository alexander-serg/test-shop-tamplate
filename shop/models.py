from django.db import models
from django.urls import reverse

class StatusMessages(models.Model):
    name = models.CharField(max_length=24, blank=True, null=True, default=None, verbose_name='статус сообщения')
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Статус {}'.format(self.name)

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class ItemCategory(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None, verbose_name='название категории')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Категория товара'
        verbose_name_plural = 'Категории товаров'

class Item(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    description = models.TextField(blank=True, verbose_name="Описание")
    size = models.CharField(max_length=10, verbose_name="Размер")
    old_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, default=None, verbose_name='пред. цена')
    is_new = models.BooleanField(default=True, verbose_name="Новое")
    action = models.DecimalField(max_digits=4, decimal_places=0, default=None, blank=True, null=True, verbose_name='скидка %')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='цена')
    stock = models.PositiveIntegerField(verbose_name="запас на складе")
    category = models.ForeignKey(ItemCategory, on_delete=models.CASCADE, blank=True, null=True, default=None, verbose_name='категория')
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")


    def __str__(self):
        return '{}'.format(self.name)

    def get_absolute_url(self):
        return reverse('shop:post', kwargs={'post_slug': self.slug})

    def image_get(self):
        return ItemImage.objects.get(itpm=self, is_main=True)

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
        return '{}'.format(self.itpm.name)

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

class Messages(models.Model):
    phone = models.CharField(max_length=48, verbose_name='Номер телефона')
    status = models.ForeignKey(StatusMessages, blank=True, null=True, default=None, on_delete=models.CASCADE, related_name='статус')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Телефон'
        verbose_name_plural = 'Телефоны'

    def __str__(self):
        return  'Телефон {0}'.format(self.phone)

class MessagesDetail(models.Model):
    name = models.CharField(max_length=55, verbose_name="Имя")
    phone = models.CharField(max_length=48, verbose_name='Телефон')
    message = models.TextField(verbose_name="Сообщение")
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

    def __str__(self):
        return  'Имя {0}'.format(self.name)

class Reviews(models.Model):
    image = models.ImageField(upload_to="reviews/%Y/%m/%d/", verbose_name="Фото отзыва")
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")

    def __str__(self):
        return 'Отзыв {0}'.format(self.id)

    class Meta:

        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'