from customparser import (
    TextStyle
)
from setting import (
    ansi_text_data
)
from utilily import (
    check_ansi_compatiblity
)



if check_ansi_compatiblity():
    text_style = TextStyle(ansi_text_data)
else:
    pass





