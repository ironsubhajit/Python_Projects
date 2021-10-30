'''
Python program to convert json data to html table
eg. like api responses
'''

import json
from json2html import *


jsonFile = "test1.json" # json file location
with open(jsonFile) as f:
    d = json.load(f) # load json file
    scanned_data = json2html.convert(json=d)

    htmlFileLoc = "output.html" # new html file location
    with open(htmlFileLoc, 'w') as htmlFile:
        htmlFile.write(str(scanned_data)) # write json data
        print("Conversion complete...")
