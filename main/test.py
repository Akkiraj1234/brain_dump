from rich.console import Console
from rich.markdown import Markdown

console = Console()

with open("C:\\Users\\DELL\\Desktop\\brain_dump\\python-dump\\_dump_\\linked_list.md","r",encoding="utf-8")as lol:
    text = lol.read()

md = Markdown(text) 
console.print(md)