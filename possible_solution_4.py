location = "comment_code_data1.json"
result = "comment_code_data1_result.json"

def write_unique_to_file(dir, res):
    # get set of unique lines
    with open(dir, 'r', encoding='utf-8') as fr:
        unique_lines = set(fr.readlines())
    # write the set of unique lines into file
    with open(res, 'w', encoding='utf-8') as fw:
        fw.writelines(unique_lines)
    fr.close()
    fw.close()

# 1 GB of Ram used
write_unique_to_file(location, result)     # 4 seconds for 1.5m line file