from .markdown import markdown
from .restructuredtext import restructuredtext

# Dictionary of supported formats and their respective parsers
supported_formats = {
    'md': markdown,
    'rst': restructuredtext,
}

def get_parser_by_extension(extension) -> object|None:
    canonical_extension = {
        'markdown': 'md',
        'mkd': 'md',
        'mkdn': 'md',
        'mdown': 'md',
        'rest': 'rst',
        'txt': 'rst',  
    }.get(extension, None)

    if canonical_extension is None:
        return None

    return supported_formats.get(canonical_extension)


__all__ = ['markdown', 'restructuredtext', 'supported_formats', 'get_parser_by_extension']
