NAME
====

dirname - strip last component from file name

SYNOPSIS
========

**dirname** [*OPTION*] *NAME*...

DESCRIPTION
===========

Output each NAME with its last non-slash component and trailing slashes removed; if NAME contains no /'s, output '.' (meaning the current directory).

**-z**, **--zero**
:   end each output line with NUL, not newline

**--help**
:   display this help and exit

**--version**
:   output version information and exit

EXAMPLES
========

dirname /usr/bin/
:   -\> "/usr"

dirname dir1/str dir2/str
:   -\> "dir1" followed by "dir2"

dirname stdio.h
:   -\> "."

AUTHOR
======

Written by David MacKenzie and Jim Meyering.

REPORTING BUGS
==============

GNU coreutils online help: \<<http://www.gnu.org/software/coreutils/>\>\
 Report dirname translation bugs to \<<http://translationproject.org/team/>\>

COPYRIGHT
=========

Copyright © 2014 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later \<<http://gnu.org/licenses/gpl.html>\>.\
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.

SEE ALSO
========

[basename](http://localhost/cgi-bin/man/man2html?1+basename)(1), [readlink](http://localhost/cgi-bin/man/man2html?1+readlink)(1)

\
 Full documentation at: \<<http://www.gnu.org/software/coreutils/dirname>\>\
 or available locally via: info aq(coreutils) dirname invocationaq
