NAME
====

fmt - simple optimal text formatter

SYNOPSIS
========

**fmt** [*-WIDTH*] [*OPTION*]... [*FILE*]...

DESCRIPTION
===========

Reformat each paragraph in the FILE(s), writing to standard output. The option **-WIDTH** is an abbreviated form of **--width**=*DIGITS*.

Mandatory arguments to long options are mandatory for short options too.

**-c**, **--crown-margin**
:   preserve indentation of first two lines

**-p**, **--prefix**=*STRING*
:   reformat only lines beginning with STRING, reattaching the prefix to reformatted lines

**-s**, **--split-only**
:   split long lines, but do not refill

**-t**, **--tagged-paragraph**
:   indentation of first line different from second

**-u**, **--uniform-spacing**
:   one space between words, two after sentences

**-w**, **--width**=*WIDTH*
:   maximum line width (default of 75 columns)

**-g**, **--goal**=*WIDTH*
:   goal width (default of 93% of width)

**--help**
:   display this help and exit

**--version**
:   output version information and exit

With no FILE, or when FILE is -, read standard input.

AUTHOR
======

Written by Ross Paterson.

REPORTING BUGS
==============

GNU coreutils online help: \<<http://www.gnu.org/software/coreutils/>\>\
 Report fmt translation bugs to \<<http://translationproject.org/team/>\>

COPYRIGHT
=========

Copyright © 2014 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later \<<http://gnu.org/licenses/gpl.html>\>.\
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.

SEE ALSO
========

Full documentation at: \<<http://www.gnu.org/software/coreutils/fmt>\>\
 or available locally via: info aq(coreutils) fmt invocationaq
