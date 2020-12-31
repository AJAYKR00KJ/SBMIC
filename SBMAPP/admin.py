from django.contrib import admin

# Register your models here.
from .models import Carousel, Implinks, Marque, Welcome
admin.site.register(Carousel)
admin.site.register(Implinks)
admin.site.register(Marque)
admin.site.register(Welcome)
