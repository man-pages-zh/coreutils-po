NAME
====

expand - convert tabs to spaces

SYNOPSIS
========

**expand** [*OPTION*]... [*FILE*]...

DESCRIPTION
===========

Convert tabs in each FILE to spaces, writing to standard output. With no FILE, or when FILE is -, read standard input.

Mandatory arguments to long options are mandatory for short options too.

**-i**, **--initial**
:   do not convert tabs after non blanks

**-t**, **--tabs**=*NUMBER*
:   have tabs NUMBER characters apart, not 8

**-t**, **--tabs**=*LIST*
:   use comma separated list of explicit tab positions

**--help**
:   display this help and exit

**--version**
:   output version information and exit

AUTHOR
======

Written by David MacKenzie.

REPORTING BUGS
==============

GNU coreutils online help: \<<http://www.gnu.org/software/coreutils/>\>\
 Report expand translation bugs to \<<http://translationproject.org/team/>\>

COPYRIGHT
=========

Copyright © 2014 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later \<<http://gnu.org/licenses/gpl.html>\>.\
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.

SEE ALSO
========

[unexpand](http://localhost/cgi-bin/man/man2html?1+unexpand)(1)

\
 Full documentation at: \<<http://www.gnu.org/software/coreutils/expand>\>\
 or available locally via: info aq(coreutils) expand invocationaq
