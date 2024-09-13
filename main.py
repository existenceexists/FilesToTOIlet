#!/usr/bin/env python3
import argparse
import os
import subprocess
import shutil
import shlex
import time
parser=argparse.ArgumentParser(
  prog='FilesCharsToTOIlet',
  description="""
Simple small CLI utility. This application gets each non-white-space character of each file in present working directory (exluding subdirectories) and create a colorful ascii art from it and output it to standart output (stdout). Each line of the ouput has the same width (number of characters (columns)). Width i.e. number of characters (columns) of each line may be set with the optional CLI argument '-w' (or '--width'). Run with the CLI argument '--help' to see description of this application and how to use its CLI arguments. The CLI utility TOIlet is used and required to be installed so that it can be found in $PATH. This is a very simple wrapper around CLI utility TOIlet. Because this script is very small and simple it can be easily modified and played with. It is written in Python so it is portable. It works with Python 3 and it can be easily modified to work also in Python 2 by replacing the text "int(shutil.get_terminal_size((80,20))[0]/7)" in the source code with any integer number (e.g. 30) and also by replacing the call to 'subprocess.run' with another method from module subprocess in Python 2.
""")
parser.add_argument('-w','--width',type=int,default=int(shutil.get_terminal_size((80,20))[0]/7),help="""Width of output. Number of characters that will be sent to TOIlet. Integer number value. It is originally intended to default to integer value so that the resulting effect is that all width of terminal emulator output area is filled, but the resulting effect is dependent on several attributes of desktop environment and the original intention will probably not be fulfilled on many devices. Defaults to width i.e. number of columns (characters) of terminal emulator as determined by the Python 3 expression "shutil.get_terminal_size((80,20))[0]/7". For example in my terminal emulator application settings I have set font size to value 9 and resulting width or number of characters (columns) of my terminal emulator is 274 and so my default value for this CLI argument is 39 because 274/7~=39.""")
parser.add_argument('-s','--sleep',type=float,default=0.1,help="""How fast this application will run. Time in seconds as a number with decimal point (i.e. floating point number) that specify the time that the script will wait (sleep) between output of each call to TOIlet. Default value is 0.1 (i.e. 0.1 seconds).""")
parser.add_argument('-d','--delimiter',type=str,default=" ",help="""How each line of each file will be separated from next line. Default value is " " i.e. an empty space. If you want each line of each file to be printed on a separate line then set this to "\n".""")
parser.add_argument('-c','--command',type=str,default="toilet --termwidth --filter gay",help="""Custom call to CLI utility TOIlet. Run the CLI command 'man toilet' and 'toilet --help' to see how to use it. Default value is 'toilet --termwidth --filter gay'. The input text for TOIlet will be automatically sent to each TOIlet call with this command via stdin (standart input).""")
parser.add_argument('dir',nargs='?',type=str,default=os.getcwd(),help="""Directory where to look for files to be processed. If not specified, the current working directory will be used.""")
args=parser.parse_args()
dir=os.path.abspath(args.dir)
if not os.path.isdir(dir):
  raise Exception("Error! The value given as positional argument 'dir' is not an existing directory. The value given was: '"+args.dir+"'")
c=shlex.split(args.command)
dl=len(args.delimiter)
adddelimiter=False
j=0
t=""
for f in os.listdir(dir):
  f=os.path.join(dir,f)
  if os.path.isfile(f):
    with open(f) as file:
      i=0
      newline=True
      while True:
        if i >= args.width:
          subprocess.run(list(c),input=t,text=True)
          time.sleep(args.sleep)
          i=0
          t=""
        if adddelimiter is True:
          if j == dl:
            adddelimiter=False
            j=0
            continue
          t=t+args.delimiter[j]
          j=j+1
          i=i+1
          continue
        char=file.read(1)
        if not char:
          break
        if newline is True:
          if char.isspace():
            continue
          newline=False
        if char=='\n':
          newline=True
          adddelimiter=True
          continue
        t=t+char
        i=i+1
