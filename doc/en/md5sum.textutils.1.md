NAME
====

md5sum - compute and check MD5 message digest

SYNOPSIS
========

**md5sum** [*OPTION*]... [*FILE*]...

DESCRIPTION
===========

Print or check MD5 (128-bit) checksums. With no FILE, or when FILE is -, read standard input.

**-b**, **--binary**
:   read in binary mode

**-c**, **--check**
:   read MD5 sums from the FILEs and check them

**--tag**
:   create a BSD-style checksum

**-t**, **--text**
:   read in text mode (default)

The following four options are useful only when verifying checksums:
--------------------------------------------------------------------

**--quiet**
:   don't print OK for each successfully verified file

**--status**
:   don't output anything, status code shows success

**--strict**
:   exit non-zero for improperly formatted checksum lines

**-w**, **--warn**
:   warn about improperly formatted checksum lines

**--help**
:   display this help and exit

**--version**
:   output version information and exit

The sums are computed as described in RFC 1321. When checking, the input should be a former output of this program. The default mode is to print a line with checksum, a character indicating input mode ('\*' for binary, space for text), and name for each FILE.

BUGS
====

The MD5 algorithm should not be used any more for security related purposes. Instead, better use an SHA-2 algorithm, implemented in the programs [sha224sum](http://localhost/cgi-bin/man/man2html?1+sha224sum)(1), [sha256sum](http://localhost/cgi-bin/man/man2html?1+sha256sum)(1), [sha384sum](http://localhost/cgi-bin/man/man2html?1+sha384sum)(1), [sha512sum](http://localhost/cgi-bin/man/man2html?1+sha512sum)(1)

AUTHOR
======

Written by Ulrich Drepper, Scott Miller, and David Madore.

REPORTING BUGS
==============

GNU coreutils online help: \<<http://www.gnu.org/software/coreutils/>\>\
 Report md5sum translation bugs to \<<http://translationproject.org/team/>\>

COPYRIGHT
=========

Copyright © 2014 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later \<<http://gnu.org/licenses/gpl.html>\>.\
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.

SEE ALSO
========

Full documentation at: \<<http://www.gnu.org/software/coreutils/md5sum>\>\
 or available locally via: info aq(coreutils) md5sum invocationaq
