NAME
====

pinky - lightweight finger

SYNOPSIS
========

**pinky** [*OPTION*]... [*USER*]...

DESCRIPTION
===========

**-l**
:   produce long format output for the specified USERs

**-b**
:   omit the user's home directory and shell in long format

**-h**
:   omit the user's project file in long format

**-p**
:   omit the user's plan file in long format

**-s**
:   do short format output, this is the default

**-f**
:   omit the line of column headings in short format

**-w**
:   omit the user's full name in short format

**-i**
:   omit the user's full name and remote host in short format

**-q**
:   omit the user's full name, remote host and idle time in short format

**--help**
:   display this help and exit

**--version**
:   output version information and exit

A lightweight 'finger' program; print user information. The utmp file will be */var/run/utmp*.

AUTHOR
======

Written by Joseph Arceneaux, David MacKenzie, and Kaveh Ghazi.

REPORTING BUGS
==============

GNU coreutils online help: \<<http://www.gnu.org/software/coreutils/>\>\
 Report pinky translation bugs to \<<http://translationproject.org/team/>\>

COPYRIGHT
=========

Copyright © 2014 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later \<<http://gnu.org/licenses/gpl.html>\>.\
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.

SEE ALSO
========

Full documentation at: \<<http://www.gnu.org/software/coreutils/pinky>\>\
 or available locally via: info aq(coreutils) pinky invocationaq
