from core.urls.url import Urls
from views import *



urls = Urls({
    '/': MyView,
    '/test': TestView
    
})
