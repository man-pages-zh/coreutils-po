NAME
====

unexpand - convert spaces to tabs

SYNOPSIS
========

**unexpand** [*OPTION*]... [*FILE*]...

DESCRIPTION
===========

Convert blanks in each FILE to tabs, writing to standard output. With no FILE, or when FILE is -, read standard input.

Mandatory arguments to long options are mandatory for short options too.

**-a**, **--all**
:   convert all blanks, instead of just initial blanks

**--first-only**
:   convert only leading sequences of blanks (overrides **-a**)

**-t**, **--tabs**=*N*
:   have tabs N characters apart instead of 8 (enables **-a**)

**-t**, **--tabs**=*LIST*
:   use comma separated LIST of tab positions (enables **-a**)

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
 Report unexpand translation bugs to \<<http://translationproject.org/team/>\>

COPYRIGHT
=========

Copyright © 2014 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later \<<http://gnu.org/licenses/gpl.html>\>.\
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.

SEE ALSO
========

[expand](http://localhost/cgi-bin/man/man2html?1+expand)(1)

\
 Full documentation at: \<<http://www.gnu.org/software/coreutils/unexpand>\>\
 or available locally via: info aq(coreutils) unexpand invocationaq
