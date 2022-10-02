from dataclasses import dataclass
from re import L


@dataclass
class Header:
    name: str
    value: str
    
    @classmethod
    def parse(cls, value):
        name, value =  value.split(":")
        return cls(*map(lambda i: i.strip(), (name, value)))
    
    def to_string(self):
        return f'{self.name}: {self.value}\r\n'
    
@dataclass
class ContentType(Header):
    charset: str
    
    @classmethod
    def parse(cls, value='Content-Type: text/html; charset=utf-8'):
        name, value =  value.split(":")
        value, charset = value.split(';')
        charset = charset[charset.rfind('=')+1:]
        return cls(*map(lambda i: i.strip(), (name, value, charset)))
    
    def to_string(self):
        return f'{self.name}: {self.value}; charset={self.charset}\r\n'

class Host(Header):
    pass
 
class Connection(Header):
    pass

@dataclass
class Cache_Control(Header):
    count: str
    
    @classmethod
    def parse(cls, value):
        count = ''
        name, value =  value.split(":")
        if '=' in value:
            value, count = value.split('=')
        return cls(*map(lambda i: i.strip(), (name, value, count)))
    
    def to_string(self):    
        count = '' if not self.count else f'={self.count}'
        return f'{self.name}: {self.value}{count}\r\n'

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
        return cls(name.strip(), dict_value)
    
    def to_string(self):
        string = f'{self.name}: '
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
        return cls(name.strip(), encoding_types)
    
    def to_string(self):
        return f'{self.name}: ' + ','.join(self.value) + '\r\n'
    
class Accept_Language(Header):
    pass



class Headers:
    DEFAULT_HEADER = Header
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
        'accept-language': Accept_Language
    }
        
    @classmethod
    def header(cls, header):
        header = cls.HEADERS.get(header)
        if not header:
            header = cls.DEFAULT_HEADER
        return header

    @staticmethod
    def name(value):
        name, *_ =  value.split(":")
        return name






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