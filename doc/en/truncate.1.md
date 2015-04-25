NAME
====

truncate - shrink or extend the size of a file to the specified size

SYNOPSIS
========

**truncate** *OPTION*... *FILE*...

DESCRIPTION
===========

Shrink or extend the size of each FILE to the specified size

A FILE argument that does not exist is created.

If a FILE is larger than the specified size, the extra data is lost. If a FILE is shorter, it is extended and the extended part (hole) reads as zero bytes.

Mandatory arguments to long options are mandatory for short options too.

**-c**, **--no-create**
:   do not create any files

**-o**, **--io-blocks**
:   treat SIZE as number of IO blocks instead of bytes

**-r**, **--reference**=*RFILE*
:   base size on RFILE

**-s**, **--size**=*SIZE*
:   set or adjust the file size by SIZE bytes

**--help**
:   display this help and exit

**--version**
:   output version information and exit

The SIZE argument is an integer and optional unit (example: 10K is 10\*1024). Units are K,M,G,T,P,E,Z,Y (powers of 1024) or KB,MB,... (powers of 1000).

SIZE may also be prefixed by one of the following modifying characters: '+' extend by, '-' reduce by, '\<' at most, '\>' at least, '/' round down to multiple of, '%' round up to multiple of.

AUTHOR
======

Written by Padraig Brady.

REPORTING BUGS
==============

GNU coreutils online help: \<<http://www.gnu.org/software/coreutils/>\>\
 Report truncate translation bugs to \<<http://translationproject.org/team/>\>

COPYRIGHT
=========

Copyright © 2014 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later \<<http://gnu.org/licenses/gpl.html>\>.\
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.

SEE ALSO
========

[dd](http://localhost/cgi-bin/man/man2html?1+dd)(1), [truncate](http://localhost/cgi-bin/man/man2html?2+truncate)(2), [ftruncate](http://localhost/cgi-bin/man/man2html?2+ftruncate)(2)

\
 Full documentation at: \<<http://www.gnu.org/software/coreutils/truncate>\>\
 or available locally via: info aq(coreutils) truncate invocationaq
