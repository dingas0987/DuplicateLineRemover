location = 'test_json1.json'
result = 'tested_json1_result_1.json'

# Write unique lines to a file
# If two lines of text have different casing but is the same string
# it is not included into the resulting file

import os.path
from os import path

def writeToFile(file, text):
    with open(file, 'a', encoding='utf-8') as newfile:
        newfile.write(text)
        newfile.close()

def dupe_search(dir, res):
    dupe_counter = 0
    with open(dir, 'r', encoding='utf-8') as readfile:
            for line in readfile:
                if not path.exists(res):
                        with open(res, 'w', encoding='utf-8') as createfile:
                            createfile.close()
                if line.lower() in open(res, encoding='utf-8').read().lower():
                    dupe_counter += 1
                else:
                    writeToFile(res, line)
    print("# of dupes:", dupe_counter)
    readfile.close()

dupe_search(location, result)
