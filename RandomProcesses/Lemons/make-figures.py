#!/usr/bin/python

filenames = [
    '4.1_maps'
]


command = ''
for name in filenames:
    command += "echo {}.svg --export-pdf={}.pdf;\n".format(name, name)
command = "({}) |\nDISPLAY= inkscape --shell".format(command)


import os
os.system(command)

