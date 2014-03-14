import requests


class GitHubUser(object):
    url = 'https://api.github.com/users/{0}'

    def __init__(self, username):
        self.username = username
        self.url = self.url.format(username)

    def fetch(self):
        r = requests.get(self.url)
        return r.json()

    def short_info(self):
        user = self.fetch()
        return """------------------
Username: {0}
Name:     {1}
Link:     {2}
""".format(user['login'], user['name'],
           user['html_url'])
