from customparser import (
    TextNode,
    HeadingNode
)
import os
from typing import TextIO
from markup_parser import get_parser_by_extension

text_node = TextNode()
headingnode = HeadingNode()

def get_node(node:str, current:object|None = None):
    nodes = {
        "heading": headingnode,
        "text": text_node
    }
    node = nodes.get(node, None)

    if node is None:
        return None

    if current is not None and node is current:
        return None
    
    return node

class rendering_pipeline:

    def __init__(self, path:str, width:int):
        self.path = path
        self.width = width
        self.type = path.rsplit(".",1)[0]
        self.parser = get_parser_by_extension(self.type)
        self.text = []
        self.data = []

    def validate_token(self, token:dict) -> bool:
        if not isinstance(token, dict):
            return False

        type = token.get("type",None)
        next = token.get("next", None)

        if type is None:
            return False

        return self.validate_token(next) if next else True
    
    def render(self):
        while True:
            try:
                self.text.append(self.render_line())
            
            except StopIteration:
                return self.text

    def return_text(self):
        return "\n".join(self.render())
    
    def render_line(self):
        """
        this is initial methods
        raise: stopiteration
        """
        if self.parser is None:
            return ""
        
        token = next(self.parser)

        if not self.validate_token(token):
            return ""

        text, data = self.generate_text(token)

        self.data.append(data)
        return text
        

    def generate_text(self, token:dict) -> str:
        data_type = token["type"]
        next = token["next"]
        property = token["property"]

        Node = get_node(data_type,None)
        return Node(**property, next = next, width = self.width)


if __name__ == "__main__":
    width = 100
    lol = rendering_pipeline("some_path", width)

    print(lol.render())

        

    