from django.contrib import admin

from .models import Comic, Reading, Collectable

admin.site.register(Comic)
admin.site.register(Reading)
admin.site.register(Collectable)
