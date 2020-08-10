from django.shortcuts import redirect, render, get_object_or_404

from .models import ShortenedUrls
from .forms import CreateShortUrlForm
from .urlgenerator import generate_short_url


def home(request):
    """Shows list of all stored urls"""
    template_name = 'urlshortener/home.html'
    urls_list = ShortenedUrls.objects.all()
    context = {'urls': urls_list}
    return render(request, template_name, context)


def teleport(_, url):
    """Redirects to full url"""

    url_obj = get_object_or_404(ShortenedUrls, short_url=url)
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
            full_url = form.cleaned_data['url']
            if not ShortenedUrls.has.full_url(full_url):
                short_url = generate_short_url(ShortenedUrls.get_set_of.short_urls())
                ShortenedUrls.objects.create(short_url=short_url, full_url=full_url)

    context = {'form': form}
    return render(request, template_name, context)
