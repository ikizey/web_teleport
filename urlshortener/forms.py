from django import forms
from django.core.exceptions import ValidationError

from .models import ShortenedUrls
from .urlgenerator import generate_label, generate_placeholder, generate_short_url


def validate_full_url_is_new(url):
    """Validator for full url.

    passes if urls doesn't exist
    """
    if not ShortenedUrls.has.full_url(url):
        return True
    else:
        raise ValidationError("%(url) already has teleport.", params={'url': url})


class CreateShortUrlForm(forms.Form):
    """Form for creating short urls"""

    url = forms.URLField(
        max_length=1024,
        label=generate_label(),
        widget=forms.TextInput(attrs={'placeholder': generate_placeholder()}),
        validators=(validate_full_url_is_new,),
    )

    def save(self, commit=True):
        full_url = self.cleaned_data['url']
        short_url = generate_short_url(ShortenedUrls.get_set_of.short_urls())
        url_obj = ShortenedUrls(short_url=short_url, full_url=full_url)
        if commit:
            url_obj.save()
        return url_obj
