#!/usr/bin/env python3
# simple python3 script to ...
import os
import subprocess
import time
l=os.listdir('.')
for f in l:
  if os.path.isfile(f):
    with open(f) as file:
      for line in file:
        line=line.rstrip().replace(' ','').replace('\t','')
        n=5
        for i in range(0,len(line),n):
          subprocess.run(['toilet','--filter','gay',line[i:i+n]])
          time.sleep(0.27)
