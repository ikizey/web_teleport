from datetime import datetime as dt
from django.db import models


class ShortenedUrlsHasQuerySet(models.QuerySet):
    def short_url(self, url) -> bool:
        """Checks if url is in short_urls"""
        return self.filter(short_url=url).exists()

    def full_url(self, url) -> bool:
        """Checks if url is in full_urls"""
        return self.filter(full_url=url).exists()


class ShortenedUrlsGetSetQuerySet(models.QuerySet):  # ..GetSet.. :(
    def short_urls(self) -> set:
        """Returns set of strings of all short_urls from db"""
        return set(self.all().values_list('short_url', flat=True))

    def full_urls(self) -> set:
        """Returns set of strings of all full_urls from db"""
        return set(self.all().values_list('full_url', flat=True))


class ShortenedUrls(models.Model):
    """Model represents mapping between short url and full url

    Default len of random short_url == 6, custom urls will be suffixed with additional '-' 
    
    Two additional managers are present:

    has: checks if url is present

        usage: ShortenedUrls.has.short_url(<some_url_to_check>) -> bool

        usage: ShortenedUrls.has.full_url(<some_url_to_check>) -> bool

    get_list_of: returns set of strings of urls from db

        usage: ShortenedUrls.get_set_of.short_urls() -> set

        usage: ShortenedUrls.get_set_of.full_urls() -> set
    """

    short_url = models.CharField(max_length=7, unique=True, null=False)
    full_url = models.URLField(max_length=1024, null=False)
    created = models.DateTimeField(auto_now_add=True, null=False)
    redirects = models.IntegerField(default=0, null=False)
    last_redirect = models.DateTimeField(null=True, blank=True)

    objects = models.Manager()  # default manager
    has = ShortenedUrlsHasQuerySet.as_manager()
    get_set_of = ShortenedUrlsGetSetQuerySet.as_manager()

    def str_full_url(self) -> str:
        """Truncates full_url if too long."""
        MAX_SHOW_LEN = 50
        if len(self.full_url) > MAX_SHOW_LEN:
            TRUNCATED_SUFFIX = "[...]"
            return "".join((str(self.full_url)[: MAX_SHOW_LEN + 1], TRUNCATED_SUFFIX))
        return str(self.full_url)

    def __str__(self) -> str:
        return f"{str(self.short_url)} -> {self.str_full_url()}"

    def increase_redirects(self) -> None:
        self.redirects += 1

    def set_last_redirect(self) -> None:
        self.last_redirect = dt.now()
