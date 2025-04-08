from customparser import (
    TextStyle
)
from setting import (
    ansi_text_data
)
from utility import (
    check_ansi_compatibility
)
from markup_parser import get_parser_by_extension


if check_ansi_compatibility():
    text_style = TextStyle(ansi_text_data)
else:
    pass


class pipeline:
    def __init__(self,path:str, render:bool = True):
        self.path = path
        self.render = render
        self.parser = get_parser_by_extension(
            self.path.rsplit(".",1)[0]
        )
        self.formatted_text = None
        self.data = {}

    def render(self):
        pass





