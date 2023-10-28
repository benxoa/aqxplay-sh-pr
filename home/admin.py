from django.contrib import admin
from .models.publish import *
# Register your models here.

@admin.register(Publish)
class PublishAdmin(admin.ModelAdmin):
    list_display = ['title']
