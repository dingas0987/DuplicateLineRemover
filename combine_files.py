import os
from os import path

def combine_files(filelist, res):
    if not path.exists(res):
        with open(res, 'w', encoding='utf-8') as createfile: 
            createfile.close()
    with open(res, 'w') as outfile:
        for fname in filelist:
            with open(fname, 'r+', encoding='utf-8') as input_file:
                if(input_file.read()[-1] != '\n'):
                    input_file.write("\n")
                    input_file.close()
            with open(fname) as infile:
                for line in infile:
                    outfile.write(line)
    outfile.close()

def writeToFile(file, text):
    with open(file, 'a', encoding='utf-8') as newfile:
        newfile.write(text)
        newfile.close()

#if __name__ == '__main__':
#    files = ["text1.txt", "text2.txt", "text3.txt"]
#    result = "text_result.txt"
#    combine_files(files, result)
