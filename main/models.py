from django.db import models

class Product(models.Model):
    Name = models.CharField(max_length=100, verbose_name="Название")
    image = models.ImageField(upload_to='image/%Y', verbose_name="Изображение продукта")
    description_smoll = models.CharField(max_length=200, verbose_name="Краткое описание")
    description_big = models.TextField(null=True, blank=True, verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Стоимость")
    Cat_product = models.ForeignKey('Cat_list', null=True, on_delete=models.PROTECT, verbose_name="Катигория")

    class Meta:
        verbose_name_plural = "Продукция"
        verbose_name = "Продукт"
        ordering = ['-id']


class Cat_list(models.Model):
    name = models.CharField(max_length=50, db_index=True, verbose_name="Название")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Категории"
        verbose_name = "Категория"
        ordering = ['-id']
