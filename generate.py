#!/usr/bin/env python3

import os, re
from subprocess import check_output

for root, dirs, files in os.walk("raw"):
    if "man" in root:
        for filename in files:
            if re.match(".*\.[1-9]", filename):
                ifilepath = root+"/"+filename
                ofilepath = "build/" + filename + ".raw"
                
                print("[raw] Converting", ifilepath, "...",end="", flush=True)

                if not os.path.exists(ofilepath):
                    # pipe
                    html = check_output(["man2html", ifilepath], universal_newlines=True)
                    print("html...", end="", flush=True)
                    output = check_output(["pandoc","-f", "html", "-t", "markdown"],
                                          universal_newlines=True, input=html)
                    print("markdown...", end="", flush=True)
                    # write to file
                    f = open(ofilepath, "w")
                    f.write(output)
                    f.close()
                    print("write...", end="", flush=True)
                    
                print("done", flush=True)
