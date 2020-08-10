from random import choice
from string import ascii_lowercase


def generate_short_url(clash_set) -> str:
    """generates random string of 6 lowercase letters"""
    max_len = 6
    clash_url_paths = {'create'}
    list_of_6 = [choice(ascii_lowercase) for _ in range(max_len)]
    str_of_6 = "".join(list_of_6)
    if str_of_6 in clash_url_paths.union(clash_set):
        return generate_short_url(clash_set)
    return str_of_6


def generate_placeholder() -> str:
    """Returns url from predefined list. for placeholder in form"""
    prefix = "https://"

    websites = (
        'www.myrecipes.com',
        'hackernoon.com',
        'theoutline.com',
        'theculturetrip.com',
        'www.seeker.com',
        'medium.com/the-mission',
        'www.inverse.com',
        'www.booooooom.com',
        'www.boundless.com',
    )

    url = "".join((prefix, choice(websites)))
    return url


def generate_label() -> str:
    """Returns phrase for label in form"""
    prefix = "Url to "
    to_small_words = (
        'shrunk',
        'minify',
        'scale down',
        'reduce',
        'cut',
        'cut down',
        'abbreviate',
        'axe',
        'shorten',
        'tear',
        'crush',
        'smash',
        'press',
    )
    label = "".join((prefix, choice(to_small_words)))
    return label
