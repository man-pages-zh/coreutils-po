NAME
====

tac - concatenate and print files in reverse

SYNOPSIS
========

**tac** [*OPTION*]... [*FILE*]...

DESCRIPTION
===========

Write each FILE to standard output, last line first. With no FILE, or when FILE is -, read standard input.

Mandatory arguments to long options are mandatory for short options too.

**-b**, **--before**
:   attach the separator before instead of after

**-r**, **--regex**
:   interpret the separator as a regular expression

**-s**, **--separator**=*STRING*
:   use STRING as the separator instead of newline

**--help**
:   display this help and exit

**--version**
:   output version information and exit

AUTHOR
======

Written by Jay Lepreau and David MacKenzie.

REPORTING BUGS
==============

GNU coreutils online help: \<<http://www.gnu.org/software/coreutils/>\>\
 Report tac translation bugs to \<<http://translationproject.org/team/>\>

COPYRIGHT
=========

Copyright © 2014 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later \<<http://gnu.org/licenses/gpl.html>\>.\
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.

SEE ALSO
========

**[rev](http://localhost/cgi-bin/man/man2html?1+rev)**(1)

\
 Full documentation at: \<<http://www.gnu.org/software/coreutils/tac>\>\
 or available locally via: info aq(coreutils) tac invocationaq
