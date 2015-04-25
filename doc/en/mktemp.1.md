NAME
====

mktemp - create a temporary file or directory

SYNOPSIS
========

**mktemp** [*OPTION*]... [*TEMPLATE*]

DESCRIPTION
===========

Create a temporary file or directory, safely, and print its name. TEMPLATE must contain at least 3 consecutive 'X's in last component. If TEMPLATE is not specified, use tmp.XXXXXXXXXX, and **--tmpdir** is implied. Files are created u+rw, and directories u+rwx, minus umask restrictions.

**-d**, **--directory**
:   create a directory, not a file

**-u**, **--dry-run**
:   do not create anything; merely print a name (unsafe)

**-q**, **--quiet**
:   suppress diagnostics about file/dir-creation failure

**--suffix**=*SUFF*
:   append SUFF to TEMPLATE; SUFF must not contain a slash. This option is implied if TEMPLATE does not end in X

**-p** DIR, **--tmpdir**[=*DIR*]
:   interpret TEMPLATE relative to DIR; if DIR is not specified, use \$TMPDIR if set, else */tmp*. With this option, TEMPLATE must not be an absolute name; unlike with **-t**, TEMPLATE may contain slashes, but mktemp creates only the final component

**-t**
:   interpret TEMPLATE as a single file name component, relative to a directory: \$TMPDIR, if set; else the directory specified via **-p**; else */tmp* [deprecated]

**--help**
:   display this help and exit

**--version**
:   output version information and exit

AUTHOR
======

Written by Jim Meyering and Eric Blake.

REPORTING BUGS
==============

GNU coreutils online help: \<<http://www.gnu.org/software/coreutils/>\>\
 Report mktemp translation bugs to \<<http://translationproject.org/team/>\>

COPYRIGHT
=========

Copyright © 2014 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later \<<http://gnu.org/licenses/gpl.html>\>.\
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.

SEE ALSO
========

[mkstemp](http://localhost/cgi-bin/man/man2html?3+mkstemp)(3), [mkdtemp](http://localhost/cgi-bin/man/man2html?3+mkdtemp)(3), [mktemp](http://localhost/cgi-bin/man/man2html?3+mktemp)(3)

\
 Full documentation at: \<<http://www.gnu.org/software/coreutils/mktemp>\>\
 or available locally via: info aq(coreutils) mktemp invocationaq
