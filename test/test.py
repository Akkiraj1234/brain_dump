

# path = os.path.abspath(os.path.dirname(__file__))

# main_text = []
# with open(f"{path}\\test.md","br") as markdown:
    
#     parse = markdown_parse(markdown)
#     text = inteprate_markdown(parser)
#     main_text += text
    
# print(main_text)


# so i should have 3 component
# 1. that will parse the markdowon to middle code and buffer
# 2. that will work on the buffer to handle text
# 3. that will create the text from the buffer

# the 3 step component


# the term buffer i used here to define like for example 
# ## lets asume this is markdown text with heading 2

# the markdown parser will work on the first line and create buffer like this
# {"type":"heading", "level":2, "text": "lets asume this is markdown text with heading 2"}

# and the 2. component will handele the buffer to work with this data and pass this to its managable comonent like heading_manager(level=2,text="...", width = 200)

# that will return the text and that text will be the one that going to print on terminal 

















import os
import cProfile


def test_md_binary_view():
    path = os.path.abspath(os.path.dirname(__file__))
    os.system("cls")
    with open(f"{path}\\test.md","br") as lol:
        for line in lol:
            print(line)
        print(lol.__sizeof__())

    
demo_markdown_text = """
1    \33[1m\33[38;2;255;184;77mtopics======================================================\33[0m
2       1. \33[34moops\33[0m
3       2. \33[34mmodules\33[0m
4       3. \33[1;31mgo back\33[0m
5    |\33[30m-------------------------------------------------------------\33[0m|
6    |\33[48;2;244;162;97m                \33[0m\33[1m\33[1;30;47m   python OOps Consepts   \33[0m\33[48;2;244;162;97m                   \33[0m|
7    |\33[30m=============================================================\33[0m|
8    | so in simple work oops is a programing pardigma that uses   |
9    | object and classes in programing which allow inheritance,   |
10   | polymorphsms, encapsulation, abstraction is called oops     |
11   | (object orianted prograimng)                                |
12   |                                                             |
13   | \33[1m\33[38;2;46;139;87m-> [oops Concepts in python]\33[0m                                |
14   |  • \33[34mclass\33[0m                                                    |
15   |  • \33[34mobjects\33[0m                                                  |
16   |  • \33[34mEncapsulation\33[0m                                            |
17   |  • \33[34mInheritance\33[0m                                              |
18   |  • \33[34mPolymorphism\33[0m                                             |
19   |  • \33[34mData abstraction\33[0m                                         |
20   |  • \33[34mglossary\33[0m                                                 |
21   |                                                             |
22   | \33[1m\33[38;2;255;184;77mclass====================================================== \33[0m|
23   | A class is a blueprint for creating objects that contain    |
24   | attributes (data) and methods (functions).                  |
25   |                                                             |
26   |  • contain attribute, methods, and dunder methods..         |
27   |  • All python classes implicity inherit from the build-in   |
28   |    onject class of no parent class is spacifued.            |
29   |  • Protecs the internal data of class from being dictctly   |
30   |    accessed of modified.                                    |
31   |  • \33[1;30;47mself\33[0m refer to the insance of the class calling the mthod.|
32   |    pass as first paratmeter in method.                      |
33   |  \33[48;2;30;30;30m                                                          \33[0m |
34   |  \33[48;2;30;30;30m \33[34mclass\33[0m\33[48;2;30;30;30m \33[36mdog\33[0m\33[48;2;30;30;30m:                                               \33[0m |
35   |  \33[48;2;30;30;30m   \33[34mdef\33[0m\33[48;2;30;30;30m \33[32m__init__\33[0m\33[48;2;30;30;30m\33[92m(\33[0m\33[48;2;30;30;30mself, name, age\33[92m)\33[0m\33[48;2;30;30;30m:                         \33[0m |
36   |  \33[48;2;30;30;30m        \33[36mself.name = name\33[0m\33[48;2;30;30;30m                                  \33[0m |
37   |  \33[48;2;30;30;30m        \33[36mself.age = age\33[0m\33[48;2;30;30;30m                                    \33[0m |
38   |  \33[48;2;30;30;30m \33[36mdog\33[0m\33[48;2;30;30;30m = \33[32mDog\33[0m\33[48;2;30;30;30m\33[92m(\33[0m\33[48;2;30;30;30m\33[90m"buddy"\33[0m\33[48;2;30;30;30m, \33[32m5\33[0m\33[48;2;30;30;30m\33[92m)\33[0m\33[48;2;30;30;30m                                    \33[0m |
39   |  \33[48;2;30;30;30m \33[38;2;255;184;77mprint\33[0m\33[48;2;30;30;30m\33[92m(\33[0m\33[48;2;30;30;30m\33[36mdog.name, dog.age\33[0m\33[48;2;30;30;30m\33[92m)\33[0m\33[48;2;30;30;30m #output: buddy, 5               \33[0m |
40   |  \33[48;2;30;30;30m                                                          \33[0m |
41   |                                                             |
42   ===============================================================
43   author : @akkiraj
"""

import sys

sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__)),"src"))
print(sys.path)

from app.customparser import TextNode


print("performing text styling checkup")
text1 = [
        {"style": ["faint", "underline"], "text": "hello this world"},
        {"style": ["bold", "italic"], "text": " and my name is akki "},
        {"style": ["inline", "bold", "strikethrough", "italic"], "text": "and this is **bold** text"},
        {""}
    ]
text2 = [
        {"style": ["faint", "underline"], "text": "hello this world"},
        {"style": ["bold", "italic"], "text": " and my name is akki "},
        {"style": ["inline", "bold", "strikethrough", "italic"], "text": "and this is **bold** text"},
        {""}
    ]
text3 = [
        {"style": ["faint", "underline"], "text": "hello this world"},
        {"style": ["bold", "italic"], "text": " and my name is akki "},
        {"style": ["inline", "bold", "strikethrough", "italic"], "text": "and this is **bold** text"},
        {""}
    ]
text4 = [
        {"style": ["faint", "underline"], "text": "hello this world"},
        {"style": ["bold", "italic"], "text": " and my name is akki "},
        {"style": ["inline", "bold", "strikethrough", "italic"], "text": "and this is **bold** text"},
        {""}
    ]
text5 = [
        {"style": ["faint", "underline"], "text": "hello this world"},
        {"style": ["bold", "italic"], "text": " and my name is akki "},
        {"style": ["inline", "bold", "strikethrough", "italic"], "text": "and this is **bold** text"},
        {""}
    ]
text6 = [
        {"style": ["faint", "underline"], "text": "hello this world"},
        {"style": ["bold", "italic"], "text": " and my name is akki "},
        {"style": ["inline", "bold", "strikethrough", "italic"], "text": "and this is **bold** text"},
        {"style":["bold","double_underline", "overline"], "text":"  hello world again"}
    ]
text7 = [
        {"style": ["faint", "underline"], "text": "hello this world"},
        {"style": ["bold", "italic"], "text": " and my name is akki "},
        {"style": ["inline", "bold", "strikethrough", "italic"], "text": "and this is **bold** text"},
        {"style":["bold", "overline"], "text":"  hello world"}
    ]
text8 = [
        {"style": ["faint", "underline"], "text": "hello this world"},
        {"style": ["bold", "italic"], "text": " and my name is akki "},
        {"style": ["inline", "bold", "strikethrough", "italic"], "text": "and this is **bold** text"},
        {"style":["double_underline", "overline","bold"], "text":"  hello world again"}
    ]

texts = [text1, text2, text3, text4, text5, text6, text7, text8]
text_style = TextNode()

def check_text_style():
    os.system("cls")
    for text in texts:
        print(text_style(text))
        
cProfile.run('check_text_style()', sort="time")
print(demo_markdown_text,flush=True)