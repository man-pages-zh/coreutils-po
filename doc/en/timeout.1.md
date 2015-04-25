NAME
====

timeout - run a command with a time limit

SYNOPSIS
========

**timeout** [*OPTION*] *DURATION COMMAND* [*ARG*]...\
 **timeout** [*OPTION*]

DESCRIPTION
===========

Start COMMAND, and kill it if still running after DURATION.

Mandatory arguments to long options are mandatory for short options too.

**--preserve-status**

exit with the same status as COMMAND, even when the

command times out

**--foreground**

when not running timeout directly from a shell prompt,

allow COMMAND to read from the TTY and get TTY signals; in this mode, children of COMMAND will not be timed out

**-k**, **--kill-after**=*DURATION*

also send a KILL signal if COMMAND is still running

this long after the initial signal was sent

**-s**, **--signal**=*SIGNAL*

specify the signal to be sent on timeout;

SIGNAL may be a name like 'HUP' or a number; see 'kill **-l**' for a list of signals

**--help**

display this help and exit

**--version**

output version information and exit

DURATION is a floating point number with an optional suffix: 's' for seconds (the default), 'm' for minutes, 'h' for hours or 'd' for days.

If the command times out, and **--preserve-status** is not set, then exit with status 124. Otherwise, exit with the status of COMMAND. If no signal is specified, send the TERM signal upon timeout. The TERM signal kills any process that does not block or catch that signal. It may be necessary to use the KILL (9) signal, since this signal cannot be caught, in which case the exit status is 128+9 rather than 124.

BUGS
====

Some platforms don't curently support timeouts beyond 2038

AUTHOR
======

Written by Padraig Brady.

REPORTING BUGS
==============

GNU coreutils online help: \<<http://www.gnu.org/software/coreutils/>\>\
 Report timeout translation bugs to \<<http://translationproject.org/team/>\>

COPYRIGHT
=========

Copyright © 2014 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later \<<http://gnu.org/licenses/gpl.html>\>.\
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.

SEE ALSO
========

[kill](http://localhost/cgi-bin/man/man2html?1+kill)(1)

\
 Full documentation at: \<<http://www.gnu.org/software/coreutils/timeout>\>\
 or available locally via: info aq(coreutils) timeout invocationaq
