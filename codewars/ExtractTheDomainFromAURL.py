def parse_url(url):
    return url if type(url) == str else ''.join(url)


def splitting(url, splitter):
    url = parse_url(url)
    return url.split(splitter)


def domain_name(url):
    url = splitting(url, 'https')
    url = splitting(url, 'http')
    url = splitting(url, '://')
    url = splitting(url, 'www.')
    url = splitting(url, '.')
    return url[0]
