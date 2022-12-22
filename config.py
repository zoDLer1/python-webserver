from core.views_objects.view import Response_404
from project.urls import *

STATIC_FOLDER = 'static'
PROJECT_FOLDER = 'project'

DEFAULT_CHARSET = 'utf-8'
HOST = ('localhost', 8080)
URLS = [urls]
DEFAULT_404_VIEW = Response_404