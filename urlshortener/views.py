from django.shortcuts import redirect, render


def home(request):
    """Shows list of all stored urls"""
    return render(request, 'urlshortener/home.html')


def teleport(request, url):
    """Redirects to full url"""
    return redirect(r"http://" + url)


def create_url(request):
    """Form to add urls"""
    return render(request, 'urlshortener/create_url.html')

