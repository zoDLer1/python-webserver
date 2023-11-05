from ..exceptions.http_exceptions import UnsupportedMediaTypeException

class JsonPayload:
    @staticmethod
    def parse(data):
        return {}


class MediaPayloadHandler:
    media_types = {
        'application/json': JsonPayload
    }

    @classmethod
    def parse(cls, type, data):
        handler = cls.media_types.get(type, None)
        if (not handler):
            raise UnsupportedMediaTypeException()

        return handler.parse(data)
