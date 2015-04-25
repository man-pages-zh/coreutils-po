NAME
====

ptx - produce a permuted index of file contents

SYNOPSIS
========

**ptx** [*OPTION*]... [*INPUT*]... *(without -G)*\
 **ptx** *-G* [*OPTION*]... [*INPUT* [*OUTPUT*]]

DESCRIPTION
===========

Output a permuted index, including context, of the words in the input files.

Mandatory arguments to long options are mandatory for short options too.

**-A**, **--auto-reference**

output automatically generated references

**-G**, **--traditional**

behave more like System V 'ptx'

**-F**, **--flag-truncation**=*STRING*

use STRING for flagging line truncations

**-M**, **--macro-name**=*STRING*

macro name to use instead of 'xx'

**-O**, **--format**=*roff*

generate output as roff directives

**-R**, **--right-side-refs**

put references at right, not counted in **-w**

**-S**, **--sentence-regexp**=*REGEXP*

for end of lines or end of sentences

**-T**, **--format**=*tex*

generate output as TeX directives

**-W**, **--word-regexp**=*REGEXP*

use REGEXP to match each keyword

**-b**, **--break-file**=*FILE*

word break characters in this FILE

**-f**, **--ignore-case**

fold lower case to upper case for sorting

**-g**, **--gap-size**=*NUMBER*

gap size in columns between output fields

**-i**, **--ignore-file**=*FILE*

read ignore word list from FILE

**-o**, **--only-file**=*FILE*

read only word list from this FILE

**-r**, **--references**

first field of each line is a reference

**-t**, **--typeset-mode** - not implemented -

**-w**, **--width**=*NUMBER*

output width in columns, reference excluded

**--help**

display this help and exit

**--version**

output version information and exit

With no FILE, or when FILE is -, read standard input. Default is '-F /'.

AUTHOR
======

Written by F. Pinard.

REPORTING BUGS
==============

GNU coreutils online help: \<<http://www.gnu.org/software/coreutils/>\>\
 Report ptx translation bugs to \<<http://translationproject.org/team/>\>

COPYRIGHT
=========

Copyright © 2014 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later \<<http://gnu.org/licenses/gpl.html>\>.\
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.

SEE ALSO
========

Full documentation at: \<<http://www.gnu.org/software/coreutils/ptx>\>\
 or available locally via: info aq(coreutils) ptx invocationaq
