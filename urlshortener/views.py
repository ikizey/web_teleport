from django.shortcuts import redirect, render, get_object_or_404

from .models import ShortenedUrls
from .forms import CreateShortUrlForm


def home(request):
    """Shows list of all stored urls"""
    template_name = 'urlshortener/home.html'
    urls_list = ShortenedUrls.objects.all()
    context = {'urls': urls_list}
    return render(request, template_name, context)


def teleport(_, url):
    """Redirects to full url"""

    url_obj = get_object_or_404(ShortenedUrls, short_url=url)
    url_obj.increase_redirects()
    url_obj.set_last_redirect()
    url_obj.save()

    destination_url = url_obj.full_url
    # TODO check for malicious links before redirecting
    return redirect(destination_url)


def create_url(request):
    """Form to add urls"""
    template_name = 'urlshortener/create_url.html'
    form = CreateShortUrlForm()
    if request.method == 'POST':
        form = CreateShortUrlForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, template_name, context)
