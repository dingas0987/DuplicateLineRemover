import os
from os import path

def combine_files(filelist, res):
    if not path.exists(res):
        with open(res, 'w', encoding='utf-8') as createfile: 
            createfile.close()
    with open(res, 'w', encoding='utf-8') as outfile:
        for fname in filelist:
            with open(fname, 'r+', encoding='utf-8') as input_file:
                if(input_file.read()[-1] != '\n'):
                    input_file.write("\n")
                    input_file.close()
            with open(fname) as infile:
                try:
                    for line in infile:
                        outfile.write(line)
                except Exception as error:
                    print(error)
                    print("couldn't write this:", line)
                    continue
    outfile.close()

def writeToFile(file, text):
    with open(file, 'a', encoding='utf-8') as newfile:
        newfile.write(text)
        newfile.close()

#if __name__ == '__main__':
#    files = ["test1.json", "test2.json" ]
#    result = "test_result.json"
#    combine_files(files, result)
