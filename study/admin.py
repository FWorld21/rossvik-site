from django.contrib import admin
from .models import *


class PostImageAdmin(admin.StackedInline):
    model = Images


@admin.register(Study)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]

    class Meta:
        model = Study


admin.site.register(Comments)
