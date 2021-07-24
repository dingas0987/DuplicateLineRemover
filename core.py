from combine_files import *
from unique_text_writer import *

if __name__ == '__main__':
    result = 'combined_comment_code_data_result.json'
    # files = ['comment_code_data1.json', 'comment_code_data2.json']
    # combine_files(files, result)

    no_dupe_res = 'no_dupe_comment_code_data_result.json'
    dupe_search_set(result, no_dupe_res)
    #dupe_search(result, no_dupe_res)