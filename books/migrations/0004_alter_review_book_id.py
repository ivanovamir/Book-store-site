# Generated by Django 4.0.3 on 2022-05-06 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_alter_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='book_id',
            field=models.SlugField(),
        ),
    ]
