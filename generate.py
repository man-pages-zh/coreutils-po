#!/usr/bin/env python3

import os, re
from subprocess import check_output, call

docdir = "doc/"
srcdir = docdir + "en/"
tardir = docdir + "zh_CN/"
suffix = ".md"

if not os.path.exists(docdir):
    os.mkdir(docdir)

if not os.path.exists(srcdir):
    os.mkdir(srcdir)

poconf = "[po4a_langs] zh_CN\n"
poconf = poconf + "[po4a_paths] template/$master.pot $lang:po/$master.$lang.po\n"

for root, dirs, files in os.walk("raw"):
    if "man" in root:
        for filename in files:
            if re.match(".*\.[1-9]", filename):
                ifilepath = root+"/"+filename
                ofilepath = srcdir + filename + suffix
                

                if not os.path.exists(ofilepath):
                    print("[raw] Converting", ifilepath, "...",end="", flush=True)

                    print("html...", end="", flush=True)
                    html = check_output(["man2html", ifilepath], universal_newlines=True)

                    print("markdown...", end="", flush=True)
                    output = check_output(["pandoc","-f", "html", "-t", "markdown", "--no-wrap"],
                                          universal_newlines=True, input=html)
    
                    print("write...", end="", flush=True)
                    f = open(ofilepath, "w")
                    f.write(output)
                    f.close()
                    print("done", flush=True)
                    
                poconf = poconf + "[type: text] " + ofilepath + " zh_CN:" 
                poconf = poconf + ofilepath.replace(srcdir, tardir)
                poconf = poconf + ' opt:"-L UTF-8 -M UTF-8"' + "\n"

poconfpath = "/tmp/po.conf"
poconffd = open(poconfpath, "w")
poconffd.write(poconf)
poconffd.close()
print(check_output(["po4a", poconfpath], universal_newlines=True))
