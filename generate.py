#!/usr/bin/env python3

import os, re
from subprocess import check_output

poconf = "[po4a_langs] zh_CN\n"
poconf = poconf + "[po4a_paths] template/$master.pot $lang:po/$master.$lang.po\n"

for root, dirs, files in os.walk("raw"):
    if "man" in root:
        for filename in files:
            if re.match(".*\.[1-9]", filename):
                ifilepath = root+"/"+filename
                poconf = poconf + "[type: man] " + ifilepath + " zh_CN:" 
                poconf = poconf + ifilepath.replace("raw", "src")
                poconf = poconf + ' opt:"-L UTF-8 -M UTF-8"' + "\n"

poconfpath = "/tmp/po.conf"
poconffd = open(poconfpath, "w")
poconffd.write(poconf)
poconffd.close()
print(check_output(["po4a", poconfpath], universal_newlines=True))
