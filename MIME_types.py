class Types:
    def __init__(self, types) -> None:
        self.types =  types
        
    def get_type(self, extension):
        mime_type = self.types.get(extension)
        return self.types['default'] if not mime_type else mime_type
        

types = Types({
    'ico': 'image/vnd.microsoft.icon',
    'html': 'text/html',
    'js': 'text/javascript',
    'css': 'text/css',
    'default': 'text/html'
})
