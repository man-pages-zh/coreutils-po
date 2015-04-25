NAME
====

realpath - print the resolved path

SYNOPSIS
========

**realpath** [*OPTION*]... *FILE*...

DESCRIPTION
===========

Print the resolved absolute file name; all but the last component must exist

**-e**, **--canonicalize-existing**
:   all components of the path must exist

**-m**, **--canonicalize-missing**
:   no components of the path need exist

**-L**, **--logical**
:   resolve '..' components before symlinks

**-P**, **--physical**
:   resolve symlinks as encountered (default)

**-q**, **--quiet**
:   suppress most error messages

**--relative-to**=*FILE*
:   print the resolved path relative to FILE

**--relative-base**=*FILE*
:   print absolute paths unless paths below FILE

**-s**, **--strip**, **--no-symlinks**
:   don't expand symlinks

**-z**, **--zero**
:   end each output line with NUL, not newline

**--help**
:   display this help and exit

**--version**
:   output version information and exit

AUTHOR
======

Written by Padraig Brady.

REPORTING BUGS
==============

GNU coreutils online help: \<<http://www.gnu.org/software/coreutils/>\>\
 Report realpath translation bugs to \<<http://translationproject.org/team/>\>

COPYRIGHT
=========

Copyright © 2014 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later \<<http://gnu.org/licenses/gpl.html>\>.\
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.

SEE ALSO
========

[readlink](http://localhost/cgi-bin/man/man2html?1+readlink)(1), [readlink](http://localhost/cgi-bin/man/man2html?2+readlink)(2), [realpath](http://localhost/cgi-bin/man/man2html?3+realpath)(3)

\
 Full documentation at: \<<http://www.gnu.org/software/coreutils/realpath>\>\
 or available locally via: info aq(coreutils) realpath invocationaq
