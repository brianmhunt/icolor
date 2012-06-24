pycolors
========

Print Python strings with interpolated colors.


Example:

    >>> cformat("This is #REDa red string.")
    'This is \\x1b[31ma red string.\\x1b[0m'

    >>> cformat("This is #BLUEa blue string.", reset=False)
    'This is \\x1b[34ma blue string.'

Also included is a `cprint` command, which as a convenience prints the
result of the `cformat` call.

