from django import forms

from .urlgenerator import generate_label, generate_placeholder


class CreateShortUrlForm(forms.Form):
    """Form for creating short urls"""

    url = forms.URLField(
        max_length=1024,
        label=generate_label(),
        widget=forms.TextInput(attrs={'placeholder': generate_placeholder()}),
    )
