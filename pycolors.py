"""
Interpolation of strings for color printing.

See e.g. http://stackoverflow.com/questions/287871

MIT LICENSE
Copyright (C) 2012 Brian M Hunt

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
import string

"""This is the number that goes in the insignificant decimal position of the map 
e.g. BLUE => x4, where x is 3 for foreground and 4 for background."""
_COLOR_MAP = dict(
    BLACK   = 0,
    RED     = 1,
    GREEN   = 2,
    YELLOW  = 3,
    BLUE    = 4,
    MAGENTA = 5,
    CYAN    = 6,
    WHITE   = 7,
    DEFAULT = 9,
)

"A map of the name of an ANSI escape sequence to its number"
ANSI_CODE_MAP = dict(
        RESET = 0,
        BOLD = 1,
        INVERSE = 7,
        STRIKE = 9,
        UNBOLD = 22,
        )

for color, code in _COLOR_MAP.items():
    ANSI_CODE_MAP[color] = 30 + code # e.g. RED => 31
    ANSI_CODE_MAP[color + "BG"] = 40 + code # e.g. REDBG = 41

"A map of the strings to the actual escape sequences"
ANSI_STRING_MAP = {name:"\033[%dm" % code for name, code in ANSI_CODE_MAP.items()}

class ColorTemplate(string.Template):
    """A string template where the delimiter is '#' and the idpattern is 
    the all-caps name of an ANSI escape sequence (e.g. RED, RESET, BOLD, etc.).
    """
    delimiter = '#'

    """All of, and only, the ANSI uppercase escape sequence names e.g. 
    (RESET|DEFAULTBG|DEFAULT|...)"""
    idpattern = r'(%s)' % "|".join(c for c in ANSI_CODE_MAP.keys())

def cprint(msg, reset=True):
    """Same as cformat but prints a string.
    """
    print(cformat(msg))

def cformat(msg, reset=True):
    """
    Transform msg so that colors e.g. #RED, #{BLUE}, etc are mapped to the
    corresponding ANSI escape codes. e.g.

    >>> cformat("This is #REDa red string.")
    'This is \\x1b[31ma red string.\\x1b[0m'

    >>> cformat("This is #BLUEa blue string.", reset=False)
    'This is \\x1b[34ma blue string.'

    The returned string is escaped unless reset=False
    """
    ct = ColorTemplate(msg)
    m = ct.safe_substitute(ANSI_STRING_MAP)

    if reset:
        m += ANSI_STRING_MAP['RESET']

    return m

if __name__ == "__main__":
    cprint("""
    Color test:
        Red: #RED red on black#RESET #RED...#RESET
        Red bg: #{WHITEBG}red on white#RESET
        Bold: #{BOLD}Bolded.#RESET
        Not colored: #red #Red ##RED
    """)

    import doctest
    doctest.testmod()
    

