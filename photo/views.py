from django.shortcuts import render
import os
from django.conf import settings
from django.templatetags.static import static

# Create your views here.

def index(request):
    path = settings.MEDIA_ROOT
    img_list = os.listdir(path + '/images')
    context = {'images' : img_list}
    return render(request, "photo/index.html", context)

    