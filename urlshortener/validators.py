from urllib.parse import urlparse

from django.conf import settings
from django.core.exceptions import ValidationError

from .models import ShortenedUrls


def validate_full_url_is_new(url):
    """Validates that url is new"""
    if not ShortenedUrls.has.full_url(url):
        return True
    else:
        raise ValidationError("%(url)s already has teleport.", params={'url': url})


def validate_full_url_is_external(url):
    """Validates that url is external"""
    url_host = urlparse(url).hostname
    current_site_hosts = [urlparse(wbu).hostname for wbu in settings.WEBSITE_BASE_URLS]
    if url_host not in current_site_hosts:
        return True
    else:
        raise ValidationError(
            "%(url)s is not allowed. Should be external website.", params={'url': url}
        )

