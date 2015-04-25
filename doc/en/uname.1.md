NAME
====

uname - print system information

SYNOPSIS
========

**uname** [*OPTION*]...

DESCRIPTION
===========

Print certain system information. With no OPTION, same as **-s**.

**-a**, **--all**
:   print all information, in the following order, except omit **-p** and **-i** if unknown:

**-s**, **--kernel-name**
:   print the kernel name

**-n**, **--nodename**
:   print the network node hostname

**-r**, **--kernel-release**
:   print the kernel release

**-v**, **--kernel-version**
:   print the kernel version

**-m**, **--machine**
:   print the machine hardware name

**-p**, **--processor**
:   print the processor type or "unknown"

**-i**, **--hardware-platform**
:   print the hardware platform or "unknown"

**-o**, **--operating-system**
:   print the operating system

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
 Report uname translation bugs to \<<http://translationproject.org/team/>\>

COPYRIGHT
=========

Copyright © 2014 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later \<<http://gnu.org/licenses/gpl.html>\>.\
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.

SEE ALSO
========

[arch](http://localhost/cgi-bin/man/man2html?1+arch)(1), [uname](http://localhost/cgi-bin/man/man2html?2+uname)(2)

\
 Full documentation at: \<<http://www.gnu.org/software/coreutils/uname>\>\
 or available locally via: info aq(coreutils) uname invocationaq
