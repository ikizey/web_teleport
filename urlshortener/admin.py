from django.contrib import admin

from .models import ShortenedUrls


@admin.register(ShortenedUrls)
class ShortenedUrlsAdmin(admin.ModelAdmin):
    readonly_fields = ('full_url',)
    search_fields = ('full_url',)
