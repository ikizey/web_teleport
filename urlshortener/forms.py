from django import forms

from .models import ShortenedUrls
from .urlgenerator import generate_label, generate_placeholder, generate_short_url
from .validators import validate_full_url_is_new, validate_full_url_is_external


class CreateShortUrlForm(forms.Form):
    """Form for creating short urls"""

    url = forms.URLField(
        max_length=1024,
        label=generate_label(),
        widget=forms.TextInput(
            attrs={'placeholder': generate_placeholder(), 'size': 64}
        ),
        validators=(validate_full_url_is_new, validate_full_url_is_external),
    )

    def save(self, commit=True):
        full_url = self.cleaned_data['url']
        short_url = generate_short_url(ShortenedUrls.get_set_of.short_urls())
        url_obj = ShortenedUrls(short_url=short_url, full_url=full_url)
        if commit:
            url_obj.save()
        return url_obj
