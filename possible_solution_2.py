from itertools import islice
import linecache

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
    current_char_pos_outside = 0
    current_char_pos_inside = 0
    inner_counter = 1
    outter_counter = 0
    with open(directory, "r+", encoding='utf-8', errors='ignore') as read_file:
        for line in read_file:
            current_char_pos_outside = current_char_pos_outside + len(line) + 1
            #current_char_pos = read_file.tell()
            print("outside line:", line)
            print("outside char position:", current_char_pos_outside)
            inner_file_curr_line = linecache.getline(location, inner_counter)
            while inner_file_curr_line != '':
                current_char_pos_inside = current_char_pos_inside + len(inner_file_curr_line) + 1
                print("inside line:", inner_file_curr_line)
                print("inside char position:", current_char_pos_inside)   
                if (inner_file_curr_line == line) and (current_char_pos_outside != current_char_pos_inside):
                    dupe_count += 1
                    print("-------------------------------------")
                    print("dupe spotted")
                    print("original line:", line)
                    print("inside line number", inner_counter)
                    print("duplicate line:", inner_file_curr_line)
                    delete_line(location, inner_counter - 1)
                    print("removed")
                    print("-------------------------------------")
                    print("\n")
                    inner_counter -= 2
                inner_counter += 1
                inner_file_curr_line = linecache.getline(location, inner_counter)
                if inner_file_curr_line == '':
                    break
            if line == '':
                break
            #current_char_pos_inside = 0
            #current_char_pos_outside = 0
            print("end")
            outter_counter += 1
            #counter = 1
            #inner_counter += 1
        print("final dupe count:", dupe_count)
    read_file.close()
    print("end")
    
    
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