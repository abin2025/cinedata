from django.contrib import admin

# Register your models here.

from . import models

admin.site.register(models.Movies)

admin.site.register(models.Artist)

admin.site.register(models.Production)

admin.site.register(models.Genre)

admin.site.register(models.Rating)