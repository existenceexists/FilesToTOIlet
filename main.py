#!/usr/bin/env python3
import argparse
import os
import subprocess
import shutil
import time
parser=argparse.ArgumentParser(
  prog='FilesLinesInDirToToilet',
  description="""
Simple small CLI utility. This application gets each non-white-space character of each file in present working directory (exluding subdirectories) and create a colorful ascii art from it and output it to standart output (stdout). Each line of the ouput has the same width (number of characters (columns)). Width i.e. number of characters (columns) of each line may be set with the optional CLI argument '-w' (or '--width'). The CLI utility TOIlet is used and required to be installed so that it can be found in $PATH. This is a very simple wrapper around CLI utility TOIlet. Because this script is very small and simple it can be easily modified and played with. It is written in Python so it is portable. It works with Python 3 and probably with Python 2 also.
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
