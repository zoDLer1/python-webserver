class Url:

    def __init__(self, path: str, params: dict[str, str] = {}) -> None:
        self.path = path
        self.params = params

    @classmethod
    def parse(cls, string_url: str):
        path, *string_params = string_url.split('?', 1)
        if (not string_params):
            return cls(path)
        params = {}
        for param in string_params[0].split('&'):
            key, *value = param.split('=')
            if value:
                params[key] = value[0]
        return cls(path, params)

    def __str__(self) -> str:
        return f"<Path: {self.path},  Params: {self.params}>"
