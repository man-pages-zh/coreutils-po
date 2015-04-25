NAME
====

pathchk - check whether file names are valid or portable

SYNOPSIS
========

**pathchk** [*OPTION*]... *NAME*...

DESCRIPTION
===========

Diagnose invalid or unportable file names.

**-p**
:   check for most POSIX systems

**-P**
:   check for empty names and leading "-"

**--portability**
:   check for all POSIX systems (equivalent to **-p** **-P**)

**--help**
:   display this help and exit

**--version**
:   output version information and exit

AUTHOR
======

Written by Paul Eggert, David MacKenzie, and Jim Meyering.

REPORTING BUGS
==============

GNU coreutils online help: \<<http://www.gnu.org/software/coreutils/>\>\
 Report pathchk translation bugs to \<<http://translationproject.org/team/>\>

COPYRIGHT
=========

Copyright © 2014 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later \<<http://gnu.org/licenses/gpl.html>\>.\
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.

SEE ALSO
========

Full documentation at: \<<http://www.gnu.org/software/coreutils/pathchk>\>\
 or available locally via: info aq(coreutils) pathchk invocationaq
