icolor
======

Print Python strings with interpolated colors.


Usage
-----

Example:

    >>> cformat("This is #RED;a red string.")
    'This is \\x1b[31ma red string.\\x1b[0m'

    >>> cformat("This is #BLUE;a blue string.", reset=False)
    'This is \\x1b[34ma blue string.'

Also included is a `cprint` command, which as a convenience prints the
result of the `cformat` call.

Installation
------------

The usual:

    $ easy_install icolor

or 

    $ pip install icolor

Variants on the above include `-U` option to upgrade and `sudo` to elevate
permissions.


License
-------

This package is licensed under the MIT License, included.

