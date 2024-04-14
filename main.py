#!/usr/bin/env python3
import argparse
import os
import subprocess
import shutil
import time
parser=argparse.ArgumentParser(
  prog='FilesLinesInDirToToilet',
  description="""
Command line utility and simple wrapper around application and command line utility called TOIlet.
This application will get each line of each file in present working directory (exluding subdirectories) 
and send it to TOIlet to create colorful ascii art and output it to so-called stdout (i.e. standart output typically in type of applications called terminal emulators). 
This simple small application is written in Python 3 so it is portable.
""")
parser.add_argument('-w','--width',type=int,default=shutil.get_terminal_size((80,20))[0],help="""Number of characters that will be sent to 'toilet'. Defaults to width i.e. number of columns (characters) of terminal emulator (as determined by the Python 3 method 'shutil.get_terminal_size'.""")
args=parser.parse_args()
l=os.listdir('.')
t=""
for f in l:
  if os.path.isfile(f):
    with open(f) as file:
      i=1
      while True:
        if i >= args.width:
          subprocess.run(['toilet','--termwidth','--filter','gay',t])
          time.sleep(0.27)
          i=1
          t=""
        char=file.read(1)
        if not char.isspace() and not len(char) == 0:
          t=t+char
          i=i+1
        if not char:
          break
