#!/usr/bin/env python3
import argparse
import os
import subprocess
import shutil
import time
parser=argparse.ArgumentParser(
  prog='FilesCharsToTOIlet',
  description="""
Simple small CLI utility. This application gets each non-white-space character of each file in present working directory (exluding subdirectories) and create a colorful ascii art from it and output it to standart output (stdout). Each line of the ouput has the same width (number of characters (columns)). Width i.e. number of characters (columns) of each line may be set with the optional CLI argument '-w' (or '--width'). Run with the CLI argument '--help' to see description of this application and how to use its CLI argument. The CLI utility TOIlet is used and required to be installed so that it can be found in $PATH. This is a very simple wrapper around CLI utility TOIlet. Because this script is very small and simple it can be easily modified and played with. It is written in Python so it is portable. It works with Python 3 and it can be easily modified to work also in Python 2 by replacing the text "int(shutil.get_terminal_size((80,20))[0]/7)" in the source code with any integer number (e.g. 30) and also by replacing the call to 'subprocess.run' with another method from module subprocess in Python 2.
""")
parser.add_argument('-w','--width',type=int,default=int(shutil.get_terminal_size((80,20))[0]/7),help="""Number of characters that will be sent to TOIlet. Integer number value. It is originally intended to default to integer value so that the resulting effect is that all width of terminal emulator output area is filled, but the resulting effect is dependent on several attributes of desktop environment and the original intention will probably not be fulfilled on many devices. Defaults to width i.e. number of columns (characters) of terminal emulator as determined by the Python 3 expression "shutil.get_terminal_size((80,20))[0]/7". For example in my terminal emulator application settings I have set font size to value 9 and resulting width or number of characters (columns) of my terminal emulator is 274 and so my default value for this CLI argument is 39 because 274/7~=39.""")
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
