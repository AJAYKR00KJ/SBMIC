from django.contrib import admin

# Register your models here.
from .models import Carousel, Implinks, Marque, Welcome, Youtube, Announcement, Tender, Events, Notice, Footer
admin.site.register(Carousel)
admin.site.register(Implinks)
admin.site.register(Marque)
admin.site.register(Welcome)
admin.site.register(Youtube)
admin.site.register(Tender)
admin.site.register(Announcement)
admin.site.register(Events)
admin.site.register(Notice)
admin.site.register(Footer)
