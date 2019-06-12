from urllib import parse


class WebhookConfig(object):
    def __init__(self, webhook):
        self._webhook = webhook

    def url(self):
        return self._webhook

class BaseAuthConfig(object):
    def __init__(self, base_url, **auth):
        self._base_url = base_url
        self._auth = auth

    def url(self):
        return self._base_url + "?" + parse.urlencode(self._auth)
