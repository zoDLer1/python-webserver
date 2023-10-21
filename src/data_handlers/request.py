from .url import Url
from .headers import HeadersSet
from .payload import MediaPayloadHandler




class Request:

    def __init__(self, method, url, data=None, headers=[], cookies=[], protocol='HTTP/1.1') -> None:
        self.method = method
        self.url = url
        self.headers = headers
        self.cookies = cookies
        self.protocol = protocol

    @classmethod
    def parse_request(cls, request_info: str) -> list[str, Url, str, HeadersSet]:
        request_info, *headers_list = request_info.split('\r\n')
        method, string_url, protocol = request_info.split(' ')
        url = Url.parse(string_url)
        headers = HeadersSet.parse(headers_list)
        # Todo: cookies = Cookies.parse(...)

        return method, url, protocol, headers

    @classmethod
    def parse_request_data(cls, content_type, data):
        return MediaPayloadHandler.parse(content_type, data)

    @classmethod
    def parse(cls, data: str):
        data = data.strip()
        #? divide the data into information about the request (method, path, headers, ect.) and payload
        request_info, *payload = data.split('\r\n\r\n')

        #? divide information into method, path, protocol, headers, cookies
        method, url, protocol, headers = cls.parse_request(request_info)
        #? parsing payload
        payload = cls.parse_request_data(headers['Content-Type'], payload[0]) if payload else None

        return cls(
            method=method,
            url=url,
            data=payload,
            headers=headers,
            protocol=protocol
        )
