#!/usr/bin/python

import os

os.system('clear')

commix = ('''
gnome-terminal --hide-menubar --full-screen --title="THE CLEANER v1.0 | System Cleaning Utility" -x sh -c "echo "THE CLEANER v1.0 | System Cleaning Utiltity" && sudo apt-get install deborphan && clear && sudo apt-get clean && sudo apt-get autoclean && sudo apt-get autoremove && sudo apt-get check && sudo apt-get update && sudo deborphan | xargs sudo apt-get -y remove --purge && clear && echo FINISHED! && read && clear"
''')

commix = str(commix)

os.system(commix)

os.system('clear')
