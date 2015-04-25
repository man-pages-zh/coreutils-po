NAME
====

split - split a file into pieces

SYNOPSIS
========

**split** [*OPTION*]... [*INPUT* [*PREFIX*]]

DESCRIPTION
===========

Output fixed-size pieces of INPUT to PREFIXaa, PREFIXab, ...; default size is 1000 lines, and default PREFIX is 'x'. With no INPUT, or when INPUT is -, read standard input.

Mandatory arguments to long options are mandatory for short options too.

**-a**, **--suffix-length**=*N*
:   generate suffixes of length N (default 2)

**--additional-suffix**=*SUFFIX*
:   append an additional SUFFIX to file names

**-b**, **--bytes**=*SIZE*
:   put SIZE bytes per output file

**-C**, **--line-bytes**=*SIZE*
:   put at most SIZE bytes of lines per output file

**-d**, **--numeric-suffixes**[=*FROM*]
:   use numeric suffixes instead of alphabetic; FROM changes the start value (default 0)

**-e**, **--elide-empty-files**
:   do not generate empty output files with '-n'

**--filter**=*COMMAND*
:   write to shell COMMAND; file name is \$FILE

**-l**, **--lines**=*NUMBER*
:   put NUMBER lines per output file

**-n**, **--number**=*CHUNKS*
:   generate CHUNKS output files; see explanation below

**-u**, **--unbuffered**
:   immediately copy input to output with '-n r/...'

**--verbose**
:   print a diagnostic just before each output file is opened

**--help**
:   display this help and exit

**--version**
:   output version information and exit

The SIZE argument is an integer and optional unit (example: 10K is 10\*1024). Units are K,M,G,T,P,E,Z,Y (powers of 1024) or KB,MB,... (powers of 1000).

CHUNKS may be: N split into N files based on size of input K/N output Kth of N to stdout l/N split into N files without splitting lines l/K/N output Kth of N to stdout without splitting lines r/N like 'l' but use round robin distribution r/K/N likewise but only output Kth of N to stdout

AUTHOR
======

Written by Torbjorn Granlund and Richard M. Stallman.

REPORTING BUGS
==============

GNU coreutils online help: \<<http://www.gnu.org/software/coreutils/>\>\
 Report split translation bugs to \<<http://translationproject.org/team/>\>

COPYRIGHT
=========

Copyright © 2014 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later \<<http://gnu.org/licenses/gpl.html>\>.\
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.

SEE ALSO
========

Full documentation at: \<<http://www.gnu.org/software/coreutils/split>\>\
 or available locally via: info aq(coreutils) split invocationaq
