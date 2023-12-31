# Generated by Django 4.2.4 on 2023-08-04 09:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cat_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=50, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100, verbose_name='Название')),
                ('image', models.ImageField(upload_to='image/%Y', verbose_name='Изображение продукта')),
                ('description_smoll', models.CharField(max_length=200, verbose_name='Краткое описание')),
                ('description_big', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Стоимость')),
                ('Cat_product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='main.cat_list', verbose_name='Катигория')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукция',
            },
        ),
    ]
