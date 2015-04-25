NAME
====

paste - merge lines of files

SYNOPSIS
========

**paste** [*OPTION*]... [*FILE*]...

DESCRIPTION
===========

Write lines consisting of the sequentially corresponding lines from each FILE, separated by TABs, to standard output. With no FILE, or when FILE is -, read standard input.

Mandatory arguments to long options are mandatory for short options too.

**-d**, **--delimiters**=*LIST*
:   reuse characters from LIST instead of TABs

**-s**, **--serial**
:   paste one file at a time instead of in parallel

**--help**
:   display this help and exit

**--version**
:   output version information and exit

AUTHOR
======

Written by David M. Ihnat and David MacKenzie.

REPORTING BUGS
==============

GNU coreutils online help: \<<http://www.gnu.org/software/coreutils/>\>\
 Report paste translation bugs to \<<http://translationproject.org/team/>\>

COPYRIGHT
=========

Copyright © 2014 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later \<<http://gnu.org/licenses/gpl.html>\>.\
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.

SEE ALSO
========

Full documentation at: \<<http://www.gnu.org/software/coreutils/paste>\>\
 or available locally via: info aq(coreutils) paste invocationaq
