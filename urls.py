from handler import TestView, View, Response_404, FileReader, MyView
import os
import config



class StaticUrls:
    def path(self, url):
        handler = None
        if os.path.exists(config.STATIC_FOLDER + url):
            handler = FileReader
        return handler

class Urls:
    
    def __init__(self, urls:dict):
        self.urls = urls
        
    def path(self, url):
        return self.urls.get(url)
    




urls = Urls({
    '/': MyView,
    '/test': TestView
    
})
static_url = StaticUrls()