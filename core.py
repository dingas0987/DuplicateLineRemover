from combine_files import *
from unique_text_writer import *

if __name__ == '__main__':
    files = ['text1.txt', 'text2.txt', 'text3.txt']
    result = 'text_result.txt'
    combine_files(files, result)

    no_dupe_res = 'no_dupe_text_result.txt'
    dupe_search(result, no_dupe_res)