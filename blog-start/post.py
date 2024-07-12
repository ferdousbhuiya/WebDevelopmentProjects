import requests

class Post:
    def __init__(self, url):
        self.url = url

    def blog_post(self):
        response = requests.get(self.url)
        response.raise_for_status()
        blog_data = response.json()
        return blog_data
