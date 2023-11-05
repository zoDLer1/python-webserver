from typing import Any

class HeadersSet:

    def __init__(self, headers_set: dict[str, str] = {}) -> None:
        self.headers_set = headers_set


    def __setitem__(self, key: str, value: Any):
        self.headers_set[key.lower()] = str(value)

    def __getitem__(self, key: str):
        return self.headers_set.get(key.lower(), None)

    def prepare(self):
        str_headers = ''
        for header_name in self.headers_set:
            str_headers += ': '.join([header_name, self.headers_set[header_name]]) + '\r\n'
        return str_headers

    @classmethod
    def parse(cls, headers_list: list[str]):
        headers = {}
        for header in headers_list:
            key, value = header.split(':', 1)
            headers[key.strip().lower()] = value.strip()
        return cls(headers)



    def __str__(self) -> str:
        return f'<Headers: {self.headers_set}>'
