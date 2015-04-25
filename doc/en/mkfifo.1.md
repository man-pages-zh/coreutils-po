NAME
====

mkfifo - make FIFOs (named pipes)

SYNOPSIS
========

**mkfifo** [*OPTION*]... *NAME*...

DESCRIPTION
===========

Create named pipes (FIFOs) with the given NAMEs.

Mandatory arguments to long options are mandatory for short options too.

**-m**, **--mode**=*MODE*
:   set file permission bits to MODE, not a=rw - umask

**-Z**
:   set the SELinux security context to default type

**--context**[=*CTX*]
:   like **-Z**, or if CTX is specified then set the SELinux or SMACK security context to CTX

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
 Report mkfifo translation bugs to \<<http://translationproject.org/team/>\>

COPYRIGHT
=========

Copyright © 2014 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later \<<http://gnu.org/licenses/gpl.html>\>.\
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.

SEE ALSO
========

[mkfifo](http://localhost/cgi-bin/man/man2html?3+mkfifo)(3)

\
 Full documentation at: \<<http://www.gnu.org/software/coreutils/mkfifo>\>\
 or available locally via: info aq(coreutils) mkfifo invocationaq
