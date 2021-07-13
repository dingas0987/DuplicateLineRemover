import os
from os import path

def combine_files(file_list, res):
    # create result file if it does not exist
    if not path.exists(res):
        with open(res, 'w', encoding='utf-8') as createfile: 
            createfile.close()
    for fname in file_list:
        # files to be copied over to result file
        with open(fname, 'r+', encoding='utf-8') as input_file:
            if(input_file.read()[-1] != '\n'):
                input_file.write("\n")
            # result file
            with open(res, 'a', encoding='utf-8') as output_file:
                for line in input_file:
                    output_file.write(line)

#if __name__ == '__main__':
#    files = ["text1.txt", "text2.txt", "text3.txt"]
#    result = "text_result.txt"
#    combine_files(files, result)
