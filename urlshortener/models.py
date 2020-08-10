from django.db import models


class ShortenedUrls(models.Model):
    """Model represents mapping between short url and full url
    Default len of random short_url == 6, custom urls will be suffixed with additional '-' """

    short_url = models.CharField(max_length=7, unique=True, null=False)
    full_url = models.CharField(max_length=1024, null=False, editable=False)
    created = models.DateTimeField(auto_now_add=True, null=False)
    redirects = models.IntegerField(default=0, null=False)
    last_redirect = models.DateTimeField(null=True)

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
