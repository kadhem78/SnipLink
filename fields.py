import re
from peewee import CharField


class UrlField(CharField) : 
    def db_value(self, value):
        url_regex = re.compile(r'https?://(?:www\.)?[a-zA-Z0-9./]+')
        result = bool(url_regex.match(value))
        if not result  :
            raise TypeError("Not a url") 
        return super().db_value(value)

