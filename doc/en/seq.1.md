NAME
====

seq - print a sequence of numbers

SYNOPSIS
========

**seq** [*OPTION*]... *LAST*\
 **seq** [*OPTION*]... *FIRST LAST*\
 **seq** [*OPTION*]... *FIRST INCREMENT LAST*

DESCRIPTION
===========

Print numbers from FIRST to LAST, in steps of INCREMENT.

Mandatory arguments to long options are mandatory for short options too.

**-f**, **--format**=*FORMAT*
:   use printf style floating-point FORMAT

**-s**, **--separator**=*STRING*
:   use STRING to separate numbers (default: \\n)

**-w**, **--equal-width**
:   equalize width by padding with leading zeroes

**--help**
:   display this help and exit

**--version**
:   output version information and exit

If FIRST or INCREMENT is omitted, it defaults to 1. That is, an omitted INCREMENT defaults to 1 even when LAST is smaller than FIRST. The sequence of numbers ends when the sum of the current number and INCREMENT would become greater than LAST. FIRST, INCREMENT, and LAST are interpreted as floating point values. INCREMENT is usually positive if FIRST is smaller than LAST, and INCREMENT is usually negative if FIRST is greater than LAST. FORMAT must be suitable for printing one argument of type 'double'; it defaults to %.PRECf if FIRST, INCREMENT, and LAST are all fixed point decimal numbers with maximum precision PREC, and to %g otherwise.

AUTHOR
======

Written by Ulrich Drepper.

REPORTING BUGS
==============

GNU coreutils online help: \<<http://www.gnu.org/software/coreutils/>\>\
 Report seq translation bugs to \<<http://translationproject.org/team/>\>

COPYRIGHT
=========

Copyright © 2014 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later \<<http://gnu.org/licenses/gpl.html>\>.\
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.

SEE ALSO
========

Full documentation at: \<<http://www.gnu.org/software/coreutils/seq>\>\
 or available locally via: info aq(coreutils) seq invocationaq
