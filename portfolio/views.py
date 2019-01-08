from django.shortcuts import render
from gallery.models import Gallery


def home(request):
    gallerys = Gallery.objects  # 可能不止一个描述，要全部获取
    return render(request, 'home.html', {'gallerys': gallerys})
