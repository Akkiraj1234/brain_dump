"""
0. lets say i have the markdown fille which will transfer markdown syntax into my code form and then that will parse into my custom parser that will print the text

which will create my custom parser whom i can work with okay 

1. now what i need my custom parser

after custom parser what i need ?

2. i need a bridge that will parse the markdown info into my custom parser and that parser will print the text ....

3. so number 2 things will only work is to parse the text into terminal
"""

from typing import TextIO

#test data
tokens = [
    {
        "type": "heading","next":
        {
            "type":"text", "next": None,
            "property":
            {
                "text":
                [
                    {"style":[], "text":"hello world"}
                ]
            }
        },
        "property": {"style":"1"}
    },
    {
        "type": "text", "data":None,
        "property":
        {
            "text":
            [
                {"style":[],"text":"this is"},
                {"style":["bold"],"text":"nothing"},
                {"style":["italic"],"text":"to do"},
                {"style":[],"text":"with u"}
            ]
        }
        
    },
    {
        "type": "ul", "data":
        {
            "type": "text", "data":
            {"style":[],"text":"and yeah this is 1st test"}
        }
    },
    {
        "type": "ul", "data":
        {
            "type": "text", "data":
            {"style":[]," text":"and this is 2nd"}
        }
    },
    {
        "type": "ul", "data":
        {
            "type": "heading", "style":"2", "data":
            {
                "type": "text", "data":
                {"style":[]," text":"and this is last one"}
            }
        }
    },
    {
        "type": "text", "data":
        {"style":[],"text":"and this is final 2nd test"}
    },
    {
        "type": "ol", "data":
        {
            "type": "text", "data":
            {"style":[],"text":"hello"}
        },
        "property":{"index":1, "indent":1}
    },
    {
        "type": "ol", "data":
        {
            "type": "text", "data":
            {"style":[],"text":"hello again"}
        },
        "property":{"index":2, "indent":1}
    },
    {
        "type": "ol", "data":
        {
            "type": "text", "data":
            {"style":[],"text":"its written as 1 but its render 3 ryt"}
        },
        "property":{"index":3, "indent":1}
    },
    {
        "type": "ol", "data":
        {
            "type":"bq", "data":
            {
                "type": "text", "data":
                {"style":[],"text":"hello"}
            },
        },
        "property":{"index":4, "indent":1}
    }
]

class parser:
    """
    a iterator object that return the markdown parsed data
    for customparser to render the txt
    """
    def __init__(self, file:TextIO):
        self.file = file
        self.data = iter(tokens)
    
    def __iter__(self):
        return self
    
    def __next__(self):
        try:
            return next(self.data)
        except StopIteration:
            raise
    







    
if __name__ == "__main__":
    import os
    path = os.path.join(os.path.dirname(__file__),"test1.md")

    with open(path, "r", encoding="utf-8") as file:
        file = parser(file)
        print("begin---------------")
        print(next(file))
        print(next(file))
        print(next(file))
        print("end-----------------")
        

    


