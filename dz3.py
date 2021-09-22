#!usr/bin/python3

class Url:
    def __init__(self, scheme=None, authority='', path=[], query={}, fragment=''):
        self.scheme = scheme
        self.authority = authority
        self.path = path
        self.query = query
        self.fragment = fragment

    def __str__(self):
        link = str(self.scheme + "://" + self.authority)
        if self.path:
            for i in self.path:
                link += str("/" + i)
        if self.query != {}:
            flag = False
            if self.query != {}:
                for i in self.query:
                    if flag:
                        link += str('&' + i + '=' + self.query[i])
                    else:
                        flag = True
                        link += str("?" + i + '=' + self.query[i])
        if self.fragment == '':
            pass
        else:
            link += str("#" + self.fragment)
        return link

    def __eq__ (self, other):
        if str(self) == other:
            return True


class HttpsUrl(Url):
    def __init__(self, scheme='https', authority='', path=[], query={}, fragment=''):
        super().__init__(scheme, authority, path, query, fragment)
        self.scheme = 'https'


class HttpUrl(Url):
    def __init__(self, scheme='http', authority='', path=[], query={}, fragment=''):
        super().__init__(scheme, authority, path, query, fragment)
        self.scheme = 'http'


class GoogleUrl(Url):
    def __init__(self, scheme='https', authority='', path=[], query={}, fragment=''):
        super().__init__(scheme, authority, path, query, fragment)
        self.authority = 'google.com'


class WikiUrl(Url):
    def __init__(self, scheme='https', authority='', path=[], query={}, fragment=''):
        super().__init__(scheme, authority, path, query, fragment)
        self.authority = 'wikipedia.org'


assert GoogleUrl() == HttpsUrl(authority='google.com')
assert GoogleUrl() == Url(scheme='https', authority='google.com')
assert GoogleUrl() == 'https://google.com'
assert WikiUrl() == str(Url(scheme='https', authority='wikipedia.org'))
assert WikiUrl(path=['wiki', 'python']) == 'https://wikipedia.org/wiki/python'
assert GoogleUrl(query={'q': 'python', 'result': 'json'}) == 'https://google.com?q=python&result=json'

#class UrlCreator:
    #def __init__(self, scheme='', authority=''):
