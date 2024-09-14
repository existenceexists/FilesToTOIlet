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
Small simple wrapper around the CLI (Command Line Interface) utility TOIlet. The original intention was to create a long-lasting stream of colorful ascii art filling the whole screen. This application tries to achieve it by reading all plain text files contained in a specified directory (excluding subdirectories) and converting them into colorful ascii art. Run the main script with the CLI argument '--help' to see description of this application and how to use its CLI arguments. The CLI arguments '--command', '--width', 'dir' are important and are expected to be always used and played with. The CLI utility TOIlet (https://github.com/cacalabs/toilet) is used by this application and is required to be installed and found in $PATH. Because this script is small and simple it can be easily modified and played with. It is written in Python 3 so it is portable.
""")
parser.add_argument('-w','--width',type=int,default=int(shutil.get_terminal_size((80,20))[0]/7),help="""Width of output. Number of characters that will be sent to TOIlet. Integer number value. This argument is important and is expected to be always used.""")
parser.add_argument('-s','--sleep',type=float,default=0.1,help="""How fast this application will run. The greater the number the slower the application will run. Delay in seconds. Default value is 0.1 (i.e. 0.1 seconds).""")
parser.add_argument('-d','--delimiter',type=str,default=" ",help="""How each line of each file will be separated from next line. Default value is " " i.e. an empty space. It may contain any number of characters.""")
parser.add_argument('-c','--command',type=str,default="toilet --termwidth --filter gay",help="""Custom call to CLI utility TOIlet. This argument is important and is expected to be always used and played with. It controls how the output will look like. You need to know how to use TOIlet. Run the CLI command 'man toilet' and 'toilet --help' to see how to use this argument. Default value is 'toilet --termwidth --filter gay'. There are many various fonts available on internet, see for example the following webpages:  https://github.com/xero/figlet-fonts/blob/master/Examples.md  ,  https://github.com/xero/figlet-fonts""")
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
        try:
          char=file.read(1)
        except UnicodeDecodeError as e:
          print("Error! Aborting. Tried to read the following file but it was not in utf-8 encoding: ")
          print("'"+f+"'")
          print()
          raise e
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
