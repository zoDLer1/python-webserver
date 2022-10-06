import os
import config 
from core.views_objects.view import FileReader

class StaticUrls:
    def path(self, url):
        handler = None
        if os.path.isfile(config.STATIC_FOLDER + url):
            handler = FileReader
        return handler
