# Generated by Django 2.0.2 on 2019-01-09 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0005_auto_20190108_1949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='image/'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='titlee',
            field=models.CharField(default='作品标题', max_length=50),
        ),
    ]
