NAME
====

runcon - run command with specified security context

SYNOPSIS
========

**runcon** *CONTEXT COMMAND* [*args*]\
 **runcon** [ *-c* ] [*-u USER*] [*-r ROLE*] [*-t TYPE*] [*-l RANGE*] *COMMAND* [*args*]

DESCRIPTION
===========

Run COMMAND with completely-specified CONTEXT, or with current or transitioned security context modified by one or more of LEVEL, ROLE, TYPE, and USER.

If none of *-c*, *-t*, *-u*, *-r*, or *-l*, is specified, the first argument is used as the complete context. Any additional arguments after *COMMAND* are interpreted as arguments to the command.

Note that only carefully-chosen contexts are likely to successfully run.

Run a program in a different SELinux security context. With neither CONTEXT nor COMMAND, print the current security context.

Mandatory arguments to long options are mandatory for short options too.

CONTEXT
:   Complete security context

**-c**, **--compute**
:   compute process transition context before modifying

**-t**, **--type**=*TYPE*
:   type (for same role as parent)

**-u**, **--user**=*USER*
:   user identity

**-r**, **--role**=*ROLE*
:   role

**-l**, **--range**=*RANGE*
:   levelrange

**--help**
:   display this help and exit

**--version**
:   output version information and exit

AUTHOR
======

Written by Russell Coker.

REPORTING BUGS
==============

GNU coreutils online help: \<<http://www.gnu.org/software/coreutils/>\>\
 Report runcon translation bugs to \<<http://translationproject.org/team/>\>

COPYRIGHT
=========

Copyright © 2014 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later \<<http://gnu.org/licenses/gpl.html>\>.\
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.

SEE ALSO
========

Full documentation at: \<<http://www.gnu.org/software/coreutils/runcon>\>\
 or available locally via: info aq(coreutils) runcon invocationaq
