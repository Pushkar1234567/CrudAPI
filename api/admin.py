from django.contrib import admin
from .models import meriDukan


@admin.register(meriDukan)

class dukanAdmin(admin.ModelAdmin):
    list_display: ["__all__"]
