from django.contrib import admin

# Register your models here.
from django.contrib import admin
from . import models

@admin.register(models.Sheet)
class SheetAdmin(admin.ModelAdmin):
    list_display = (
        'defect',
        'process',
        'period',
        'created',   
    )
    search_fields = (
        'defect',
    )

    def __str__(self):
        return self.Sheet