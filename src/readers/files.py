import mimetypes

mimetypes.add_type('image/webp', '.webp')

class FileReader:

    def __init__(self, filepath) -> None:
        self.file_read_rb(filepath)

    def file_read_rb(self, filepath):
        mimetype, encoding = mimetypes.guess_type(filepath)
        self.encoding = encoding
        self.mimetype = mimetype

        with open(filepath, 'rb') as file:
            self.content = file.read()

