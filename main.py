#!/usr/bin/env python3
# simple python3 script to ...
import os
import subprocess
l=os.listdir('.')
for f in l:
  if os.path.isfile(f):
    with open(f) as file:
      for line in file:
        subprocess.run(['toilet','--filter','gay',line.rstrip()])