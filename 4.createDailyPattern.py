import csv
import numpy as np
import os

for root, dirs, files in os.walk(os.curdir):
    for dir in dirs:
        for name in files:
            if name.endswith(".txt"):
                current = os.path.join(root, name)
                # print current
                # print 'redd-'+current[-9:]
                with open(current, 'rb') as f, open(dir+'/redd-'+current[-9:], 'wb') as out:
                    out.write(str(dir)+"\n")
                    for line in f:
                        if line.strip()==str(int(dir)+1)+" 60":
                            break
                        # print line
                        out.write(line)
