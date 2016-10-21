#!/usr/bin/env python

# the purpose of this script is to set up a set of terminals in my i
# screencasting box ( that is a good screencasting size )

# set one
# the I want these to go to 'monitor 2' in the upper left hand corner
#

import os
#                                (COLSxROWS+X+Y)
os.system("gnome-terminal --geometry=71x37+1920+0 ")
os.system("gnome-terminal --geometry=71x17+2563+0 ")
os.system("gnome-terminal --geometry=71x17+2563+360 ")
#os.sys("gnome-terminal")
