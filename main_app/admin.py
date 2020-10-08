from django.contrib import admin

# import your models here
from .models import Comic, Reading

# Register your models here
admin.site.register(Comic)
admin.site.register(Reading)