# Write unique lines to a file
import os.path
from os import path
def writeToFile(file, text):
    with open(file, 'a', encoding='utf-8') as newfile:
        newfile.write(text)
        newfile.close()

#o(n) space complexity, O(n^2) time complexity
def dupe_search(dir, res):
    dupe_counter = 0
    file = open(dir, 'r+', encoding='utf-8')
    if(file.read()[-1] != '\n'):
        file.write("\n")

    file = open(dir, 'r+', encoding='utf-8')
    file.read()
    with open(dir, 'r+', encoding='utf-8') as readfile:
        for line in readfile:
            if not path.exists(res):
                with open(res, 'w', encoding='utf-8') as createfile: #result file
                    createfile.close()

            file_contents = open(res, encoding='utf-8').read()
            if line in file_contents:
                dupe_counter += 1
            else:
                writeToFile(res, line)
    print("# of dupes:", dupe_counter)
    readfile.close()


if __name__ == '__main__':
    location = 'test.txt'
    result = 'test1.json'
    dupe_search(location, result)