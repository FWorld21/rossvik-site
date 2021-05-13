from django.contrib import admin
from .models import *


class PostImageAdmin(admin.StackedInline):
    model = Images


@admin.register(News)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]

    class Meta:
        model = News


admin.site.register(Comments)
