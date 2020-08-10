from django.contrib import admin

from .models import ShortenedUrls


@admin.register(ShortenedUrls)
class ShortenedUrlsAdmin(admin.ModelAdmin):
    # readonly_fields = ('short_url', 'full_url',)
    search_fields = ('full_url', 'short_url')
    list_display = ('short_url', 'str_full_url', 'redirects', 'last_redirect')
    ordering = ('-redirects',)

