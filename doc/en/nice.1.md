NAME
====

nice - run a program with modified scheduling priority

SYNOPSIS
========

**nice** [*OPTION*] [*COMMAND* [*ARG*]...]

DESCRIPTION
===========

Run COMMAND with an adjusted niceness, which affects process scheduling. With no COMMAND, print the current niceness. Niceness values range from **-20** (most favorable to the process) to 19 (least favorable to the process).

Mandatory arguments to long options are mandatory for short options too.

**-n**, **--adjustment**=*N*
:   add integer N to the niceness (default 10)

**--help**
:   display this help and exit

**--version**
:   output version information and exit

NOTE: your shell may have its own version of nice, which usually supersedes the version described here. Please refer to your shell's documentation for details about the options it supports.

AUTHOR
======

Written by David MacKenzie.

REPORTING BUGS
==============

GNU coreutils online help: \<<http://www.gnu.org/software/coreutils/>\>\
 Report nice translation bugs to \<<http://translationproject.org/team/>\>

COPYRIGHT
=========

Copyright © 2014 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later \<<http://gnu.org/licenses/gpl.html>\>.\
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.

SEE ALSO
========

[nice](http://localhost/cgi-bin/man/man2html?2+nice)(2), [renice](http://localhost/cgi-bin/man/man2html?1+renice)(1)

\
 Full documentation at: \<<http://www.gnu.org/software/coreutils/nice>\>\
 or available locally via: info aq(coreutils) nice invocationaq
