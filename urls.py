
from handler import View



class Urls:
    
    def __init__(self, urls:dict):
        self.urls = urls
    
    def path(self, url):
        return self.urls.get(url)
    


urls = Urls({
    
    '/': View
})
