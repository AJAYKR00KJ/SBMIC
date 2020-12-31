from django.shortcuts import render
from .models import Carousel, Implinks, Marque, Welcome

def home(request):
    car_img = Carousel.objects.filter(featured=True)
    imp_links = Implinks.objects.filter(featured= True)
    mar_links = Marque.objects.filter(featured=True)
    welcome= Welcome.objects.filter(featured=True).order_by('-date')[0:1]
    context = {
        'object_list': car_img,
        'important_links': imp_links,
        'marque_links': mar_links,
        'welcome': welcome
    }
    return render(request,'home.html',context)

def gallery(request):
    return render(request,'gallery.html',{})

