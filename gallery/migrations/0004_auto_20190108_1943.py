# Generated by Django 2.0.2 on 2019-01-08 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_auto_20190108_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='title',
            field=models.CharField(default='作品标题---', max_length=50),
        ),
    ]