NAME
====

rmdir - remove empty directories

SYNOPSIS
========

**rmdir** [*OPTION*]... *DIRECTORY*...

DESCRIPTION
===========

Remove the DIRECTORY(ies), if they are empty.

**--ignore-fail-on-non-empty**

ignore each failure that is solely because a directory

is non-empty

**-p**, **--parents**

remove DIRECTORY and its ancestors; e.g., 'rmdir **-p** a/b/c' is similar to 'rmdir a/b/c a/b a'

**-v**, **--verbose**

output a diagnostic for every directory processed

**--help**

display this help and exit

**--version**

output version information and exit

AUTHOR
======

Written by David MacKenzie.

REPORTING BUGS
==============

GNU coreutils online help: \<<http://www.gnu.org/software/coreutils/>\>\
 Report rmdir translation bugs to \<<http://translationproject.org/team/>\>

COPYRIGHT
=========

Copyright © 2014 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later \<<http://gnu.org/licenses/gpl.html>\>.\
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.

SEE ALSO
========

[rmdir](http://localhost/cgi-bin/man/man2html?2+rmdir)(2)

\
 Full documentation at: \<<http://www.gnu.org/software/coreutils/rmdir>\>\
 or available locally via: info aq(coreutils) rmdir invocationaq
