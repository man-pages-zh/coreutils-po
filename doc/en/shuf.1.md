NAME
====

shuf - generate random permutations

SYNOPSIS
========

**shuf** [*OPTION*]... [*FILE*]\
 **shuf** *-e* [*OPTION*]... [*ARG*]...\
 **shuf** *-i LO-HI* [*OPTION*]...

DESCRIPTION
===========

Write a random permutation of the input lines to standard output.

Mandatory arguments to long options are mandatory for short options too.

**-e**, **--echo**
:   treat each ARG as an input line

**-i**, **--input-range**=*LO-HI*
:   treat each number LO through HI as an input line

**-n**, **--head-count**=*COUNT*
:   output at most COUNT lines

**-o**, **--output**=*FILE*
:   write result to FILE instead of standard output

**--random-source**=*FILE*
:   get random bytes from FILE

**-r**, **--repeat**
:   output lines can be repeated

**-z**, **--zero-terminated**
:   line delimiter is NUL, not newline

**--help**
:   display this help and exit

**--version**
:   output version information and exit

With no FILE, or when FILE is -, read standard input.

AUTHOR
======

Written by Paul Eggert.

REPORTING BUGS
==============

GNU coreutils online help: \<<http://www.gnu.org/software/coreutils/>\>\
 Report shuf translation bugs to \<<http://translationproject.org/team/>\>

COPYRIGHT
=========

Copyright © 2014 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later \<<http://gnu.org/licenses/gpl.html>\>.\
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.

SEE ALSO
========

Full documentation at: \<<http://www.gnu.org/software/coreutils/shuf>\>\
 or available locally via: info aq(coreutils) shuf invocationaq
