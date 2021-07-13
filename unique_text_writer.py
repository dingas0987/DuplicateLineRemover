location = 'test_json1.json'
result = 'tested_json1_result_1.json'
#location = "comment_code_data1.json"
#result = "comment_code_data1_result_2.json"

# Write unique lines to a file

import os.path
from os import path

def remove_bottom_blank(file):
    with open(file, 'rb+') as file_out:
        file_out.seek(-2, os.SEEK_END)
        file_out.truncate()

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
    remove_bottom_blank(dir)
    readfile.close()

dupe_search(location, result)