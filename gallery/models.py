from django.db import models

# Create your models here.


class Gallery(models.Model):
    # default为默认选项
    description = models.CharField(default='在这里写作品的简介', max_length=100)
    image = models.ImageField(default='default.jpg', upload_to='image/')
    titlee = models.CharField(default='作品标题', max_length=50)

    def __str__(self):
        return self.titlee
