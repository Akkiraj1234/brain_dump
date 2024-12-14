from typing import List, Dict, Any

class TextStyle:
    def __init__(self, ansi_code:dict|None = None):
        self.ansi_code = ansi_code or {
            "reset": "0",
            "bold": "1",
            "faint": "2",
            "italic": "3",
            "underline": "4",
            "strikethrough": "9",
            "inline": "47;30",
            "overline": "53",        #does not work in window 10 cmd
            "double_underline": "21" #does not work in window 10 cmd
        }

    def __call__(self, tokens: List[Dict[str, Any]]) -> str:
        if not isinstance(tokens, list) or not tokens:
            return "" 
        
        return "".join(self.format_text(token) for token in tokens)

    def format_text(self, token: Dict[str, Any]) -> str:
        if not isinstance(token, dict):
            return ""
        
        styles = token.get("style", [])
        text = token.get("text", "")
        
        return f"{self.generate_ansi_sequence(styles)}{text}{self.generate_ansi_sequence(['reset'])}"
    
    def generate_ansi_sequence(self, styles: List[str]) -> str:
        """Generate the escape sequence from styles"""
        codes = ";".join(self.ansi_code.get(style, self.ansi_code["reset"]) for style in styles)
        return f"\033[{codes}m"
    
    def __future_plan__(self) -> str:
        return """\n
        # will do in upcoming future
        1. Use ANSI escape codes as your default formatting system.
            a. Try to enable ANSI using SetConsoleMode with ctypes (on Windows 10+).
            b. If ANSI fails, fallback to Win32 Console APIs for compatibility with older versions.
            c. Terminfo-based handling in the future. for legesy system
            
        2. LRU Cache (for Precomputed ANSI Codes): Great addition for optimizing repeated style combinations in the future.
        
        3. _load_color_and_all_from_somewhere.
        
        # not now
        1. will make it compatible with sixel graphics for terminal like kitty
        """






# Example usage
if __name__ == "__main__":
    text = [
        {"style": ["faint", "underline"], "text": "hello this world"},
        {"style": ["bold", "italic"], "text": " and my name is akki "},
        {"style": ["inline", "bold", "strikethrough", "italic"], "text": "and this is **bold** text"},
        {"style": ["underline","faint","inline", "bold", "strikethrough", "italic"], "text": "\nand this is **bold** text"}
    ]
    ansi_code_set = {
        "reset": "0",
        "bold": "2",
        "faint": "1",
        "italic": "9",
        "underline": "47;30",
        "strikethrough": "3",
        "inline": "4",
        "overline": "53",        #does not work in window 10 cmd
        "double_underline": "21" #does not work in window 10 cmd
    }

    text_style = TextStyle(None)
    print(text_style(text))














# Foreground Colors:

#     Black: 30
#     Red: 31
#     Green: 32
#     Yellow: 33
#     Blue: 34
#     Magenta: 35
#     Cyan: 36
#     White: 37

# Background Colors:

#     Background Black: 40
#     Background Red: 41
#     Background Green: 42
#     Background Yellow: 43
#     Background Blue: 44
#     Background Magenta: 45
#     Background Cyan: 46
#     Background White: 47

# Bright Colors (Foreground and Background):

#     Bright Black (Gray): 90
#     Bright Red: 91
#     Bright Green: 92
#     Bright Yellow: 93
#     Bright Blue: 94
#     Bright Magenta: 95
#     Bright Cyan: 96
#     Bright White: 97

# Text Effects:

#     -----Blink (Slow): 5-----
#     -----Blink (Rapid): 6 (Note: Rarely supported in modern terminals)-----
#     -----Conceal (Hidden Text): 8-----
#     Double Underline: 21 (Supported in some terminals)[done]
#     Overline: 53[done]

# Reset Specific Attributes:

#     Reset Bold/Dim: 22
#     Reset Italic: 23
#     Reset Underline: 24
#     Reset Blink: 25
#     Reset Inverse: 27
#     Reset Conceal: 28
#     Reset Strikethrough: 29