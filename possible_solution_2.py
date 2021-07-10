from itertools import islice

#location = "test_json1.json"
location = "test.txt"

# Current Status
# It deletes the lines
# Sometimes it doesn't
# The counter is not very accurate

#                #islice is used to start the iterator in a different spot
#                start_inner_loop = islice(inner_file, counter, None)
#                for line_num, dupe_line in enumerate(start_inner_loop, counter):
#                    if dupe_line == line:
#                        dupe_count +=1
#                        print("there is a dupe spotted")
#                        print("original line #:", counter)
#                        print("original line:", line)
#                        print("dupe line #",line_num)
#                        print("dupe line", dupe_line)
#                        line_num -=1
#                        # screw it using the stack overflow solution
#                        delete_line(directory, line_num)  
#                        print("removed") 
#                        print("current duplicates found:", dupe_count)
#                        continue

def search_dupe(directory):
    dupe_count = 0 
    inner_file_line = 0
    current_char_pos = 0
    with open(directory, "r+", encoding='utf-8', errors='ignore') as read_file:
        for line in read_file:
            current_char_pos = current_char_pos + len(line) + 1
            print("current char position:", current_char_pos)
            print("current line:", line)
            with open(directory, "r+", encoding='utf-8', errors='ignore') as inner_file:
                dupe_line = inner_file.readline()
                while dupe_line:
                    inner_file_pos = inner_file.tell()
                    print("current line in dupe file:", dupe_line)
                    print("inner file position:",inner_file_pos)
                    if (line == dupe_line) and (current_char_pos != inner_file_pos):
                        dupe_count +=1
                        print("there is a dupe spotted")
                        print("original line:", line)
                        print("dupe line", dupe_line)
                        #delete_line(directory, inner_file_line)
                    #inner_file_line+=1 
                    dupe_line = inner_file.readline()
                    inner_file_pos = inner_file.tell()
                    
        print("final dupe count:", dupe_count)
        if dupe_count == 0:
            print("there are no more dupes")
    read_file.close()
    
    
def delete_line(dir, lineno):
    fro = open(dir, "r", encoding='utf-8', errors='ignore')

    current_line = 0
    while current_line < lineno:
        fro.readline()
        current_line += 1
        
    #tells current file position
    seekpoint = fro.tell()
    frw = open(dir, "r+", encoding='utf-8', errors='ignore')
    frw.seek(seekpoint, 0)

    # read the line we want to discard
    fro.readline()

    # now move the rest of the lines in the file 
    # one line back 
    chars = fro.readline()
    while chars:
        frw.writelines(chars)
        chars = fro.readline()

    fro.close()
    frw.truncate()
    frw.close()

search_dupe(location)