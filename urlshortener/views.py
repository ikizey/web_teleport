from django.shortcuts import redirect, render, get_object_or_404

from .models import ShortenedUrls


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
    return render(request, 'urlshortener/create_url.html')

