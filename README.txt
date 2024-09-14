$ python3 main.py --help
usage: FilesToTOIlet [-h] [-w WIDTH] [-s SLEEP] [-d DELIMITER] [-c COMMAND] [dir]

Small simple wrapper around the CLI (Command Line Interface) utility TOIlet. The original intention was to create a long-lasting stream of colorful ascii art filling the whole screen. This application tries to achieve it by reading all plain text files contained in a specified directory (excluding subdirectories) and converting them into colorful ascii art. Run the main script with the CLI argument '--help' to see description of this application and how to use its CLI arguments. The CLI arguments '--command', '--width', 'dir' are important and are expected to be always used and played with. The CLI utility TOIlet (https://github.com/cacalabs/toilet) is used by this application and is required to be installed and found in $PATH. Because this script is small and simple it can be easily modified and played with. It is written in Python 3 so it is portable.

positional arguments:
  dir                   Directory where to look for files to be processed. If not specified, the current working directory will be used.

options:
  -h, --help            show this help message and exit
  -w WIDTH, --width WIDTH
                        Width of output. Number of characters that will be sent to TOIlet. Integer number value. This argument is important and is expected to be always used.
  -s SLEEP, --sleep SLEEP
                        How fast this application will run. The greater the number the slower the application will run. Delay in seconds. Default value is 0.1 (i.e. 0.1 seconds).
  -d DELIMITER, --delimiter DELIMITER
                        How each line of each file will be separated from next line. Default value is " " i.e. an empty space. It may contain any number of characters.
  -c COMMAND, --command COMMAND
                        Custom call to CLI utility TOIlet. This argument is important and is expected to be always used and played with. It controls how the output will look like. You need to know how to use TOIlet. Run the CLI command 'man toilet' and 'toilet --help' to see how to use this argument. Default value is 'toilet --termwidth --filter gay'. There are many various fonts available on internet, see for example the following webpages: https://github.com/xero/figlet-fonts/blob/master/Examples.md , https://github.com/xero/figlet-fonts