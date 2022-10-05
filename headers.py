from dataclasses import dataclass



class Header:
    value: str
    
    def __init__(self,  value):
        self.value = value
    
    @classmethod
    def parse(cls, value):
        name, value =  value.split(":", maxsplit=1)
        return cls(value.strip())
    
    def to_string(self):
        return f'{self.name}: {self.value}\r\n'

    @property
    def name(self):
        return self.__class__.__name__.replace("_", "-")
    
class ContentType(Header):
    
    def __init__(self,  value, charset):
        self.value = value
        self.charset = charset
    
    @classmethod
    def parse(cls, value):
        name, value =  value.split(":")
        value, charset = value.split(';')
        charset = charset[charset.rfind('=')+1:]
        return cls(*map(lambda i: i.strip(), (value, charset)))
    
    def to_string(self):
        return self.name + f'; charset={self.charset}\r\n'

class Host(Header):
    pass
 
class Connection(Header):
    pass


class Cache_Control(Header):

    def __init__(self, value, count):
        super().__init__(value)
        self.count = count
    
    
    
    @classmethod
    def parse(cls, value):
        count = ''
        name, value =  value.split(":")
        if '=' in value:
            value, count = value.split('=')
        return cls(*map(lambda i: i.strip(), (value, count)))
    
    def to_string(self):    
        count = '' if not self.count else f'={self.count}\r\n'
        return self.name + count

class Sec_Ch_Ua(Header):
    pass

class Sec_Ch_Ua_Mobile(Header):
    pass

class Sec_Ch_Ua_Platform(Header):
    pass

class Upgrade_Insecure_Requests(Header):
    pass

class User_Agent(Header):
    pass

class Accept(Header):
    value: dict
    
    @classmethod
    def parse(cls, value):
        dict_value = {}
        name, mime_types = value.split(":")
        for mime_type in mime_types.split(','):
            mime_type, *adding,  = mime_type.split(';')
            adding = dict([tuple(item.split('=')) for item in adding]) if adding else {}
            dict_value[mime_type] = adding
        return cls(dict_value)
    
    def to_string(self):
        string = f'{self.name}'
        for mime_type, value in self.value.items():
            string += f'{mime_type}'
            for key, val in value.items():
                string += f';{key}={val}'
            string += ','
        return string[:-1] + '\r\n'
    
class Sec_Fetch_Site(Header):
    pass

class Sec_Fetch_Mode(Header):
    pass

class Sec_Fetch_User(Header):
    pass

class Sec_Fetch_Dest(Header):
    pass

class Accept_Encoding(Header):
    value: list
    
    @classmethod
    def parse(cls, value):
        name, value =  value.split(":")
        encoding_types = value.split(",")
        return cls(encoding_types)
    
    def to_string(self):
        return f'{self.name}: ' + ','.join(self.value) + '\r\n'
    
class Accept_Language(Header):
    pass

class Indefinited_Headrer(Header):
    def __init__(self, name, value):
        print(f'Header {name} is not definded')
        self.label = name
        self.value = value    
    
    @classmethod
    def parse(cls, value):
        name, value =  value.split(":", maxsplit=1)
        return cls(name.strip(), value.strip())

class Referer(Header):
    pass

class Access_Control_Allow_Origin(Header):
    pass

class Access_Control_Allow_Methods(Header):
    pass

class Access_Control_Allow_Headers(Header):
    pass

class Headers:
    DEFAULT_HEADER = Indefinited_Headrer
    HEADERS = {
        'host': Host,
        'connection': Connection,
        'cache-control': Cache_Control,
        'sec-ch-ua': Sec_Ch_Ua,
        'sec-ch-ua-mobile': Sec_Ch_Ua_Mobile,
        'sec-ch-ua-platform': Sec_Ch_Ua_Platform,
        'upgrade-insecure-requests': Upgrade_Insecure_Requests,
        'user-agent': User_Agent,
        'accept': Accept,
        'sec-fetch-site': Sec_Fetch_Site,
        'sec-fetch-mode': Sec_Fetch_Mode,
        'sec-fetch-user': Sec_Fetch_User,
        'sec-fetch-dest': Sec_Fetch_Dest,
        'accept-encoding': Accept_Encoding,
        'accept-language': Accept_Language,
        'referer': Referer,
        'access-control-allow-origin': Access_Control_Allow_Origin,
        'access-control-allow-methods': Access_Control_Allow_Methods
    }
        
    @classmethod
    def header(cls, header):
        hdr = cls.HEADERS.get(cls.name(header))
        return cls.DEFAULT_HEADER.parse(header) if not hdr else hdr.parse(header)

    @staticmethod
    def name(value):
        name, *_ =  value.split(":")
        return name.strip().lower()






# p = Accept_Encoding.parse('Accept-Encoding: gzip, deflate, br')
# print(p.value)
# print(p.to_string())

['Host: localhost', 'Connection: keep-alive', 'Cache-Control: max-age=0', 
 'sec-ch-ua: "Not-A.Brand";v="99", "Opera GX";v="91", "Chromium";v="105"', 
 'sec-ch-ua-mobile: ?0', 
 'sec-ch-ua-platform: "Windows"', 
 'Upgrade-Insecure-Requests: 1', 
 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 OPR/91.0.4516.36', 
 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 
 'Sec-Fetch-Site: none', 
 'Sec-Fetch-Mode: navigate', 
 'Sec-Fetch-User: ?1', 
 'Sec-Fetch-Dest: document', 
 'Accept-Encoding: gzip, deflate, br', 
 'Accept-Language: ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7', '', '']