from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Carousel, Implinks, Marque, Welcome, Youtube, Announcement, Notice, Events, Tender, Footer
from message.models import Message


def home(request):
    car_img = Carousel.objects.filter(featured=True)
    imp_links = Implinks.objects.filter(featured=True)
    mar_links = Marque.objects.filter(featured=True)
    welcome = Welcome.objects.filter(featured=True).order_by('-date')[0:1]
    youtube = Youtube.objects.filter(featured=True).order_by('-date')[0:1]

    announcement = Announcement.objects.filter(featured=True).order_by('-date')[0:8]
    notice = Notice.objects.filter(featured=True).order_by('-date')[0:8]
    events = Events.objects.filter(featured=True).order_by('-date')[0:8]
    tender = Tender.objects.filter(featured=True).order_by('-date')[0:8]

    footer = Footer.objects.all()

    if request.method == 'POST':
        email = request.POST["email"]
        text = request.POST["message"]
        new_message = Message()
        new_message.email = email
        new_message.text_message = text

        new_message.save()
        messages.success(request, 'Submitted')
        return HttpResponseRedirect('/')

    context = {
        'object_list': car_img,
        'important_links': imp_links,
        'marque_links': mar_links,
        'welcome': welcome,
        'Youtube': youtube,
        'Announcement': announcement,
        'Notice': notice,
        'Event': events,
        'Tender': tender,
        'Footer': footer,
    }
    return render(request, 'home.html', context)


def gallery(request):
    return render(request, 'gallery.html', {})
