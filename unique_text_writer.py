# Write unique lines to a file
import os.path
from os import path
import file_utils
import sys, logging
import time

logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s', datefmt='%Y-%m-%d %H:%M:%S', stream=sys.stderr, level=logging.CRITICAL)### CRITICAL ERROR WARNING INFO DEBUG NOTSET



def writeToFile(file, text):
    with open(file, 'a', encoding='ISO-8859-1') as newfile:
        newfile.write(text)
        newfile.close()


def dupe_search_set(dir, res):
    lines_seen = set() # holds lines already seen
    file_utils.add_newline_if_missing_big(dir, 'ISO-8859-1')
    outfile = open(res, "w", encoding = 'ISO-8859-1')
    for line in open(dir, "r", encoding = 'ISO-8859-1'):
        if line not in lines_seen: # not a duplicate
            outfile.write(line)
            lines_seen.add(line)
    outfile.close()

#o(n) space complexity, O(n^2) time complexity
def dupe_search(dir, res):
    dupe_counter = 0
    file_utils.add_newline_if_missing_big(dir, 'ISO-8859-1')
    file = open(dir, 'r+', encoding='ISO-8859-1')
    file.read()
    if not path.exists(res):
        with open(res, 'w', encoding='ISO-8859-1') as createfile: #result file
            createfile.close()
    logging.error("Starting main loop")
    hit_count = 0
    total_hit_count = 0
    cum_line = ""
    HIT_INCR = 50000
    with open(dir, 'r+', encoding='ISO-8859-1') as readfile:
        for line in readfile:
            logging.error("Current count: %d", hit_count)
            with open(res, encoding='ISO-8859-1') as res_file:
                if line in res_file.read():
                    dupe_counter += 1
                else:
                    hit_count = hit_count + 1
                    cum_line = cum_line + line
            logging.error("Dupe/hitcount updated")
            if(hit_count == HIT_INCR):
                total_hit_count = total_hit_count + HIT_INCR
                hit_count = 0
                logging.critical("Hit: %d", total_hit_count)
                writeToFile(res, cum_line)
                cum_line = ""
            logging.error("Wrote to file")
    logging.error("# of dupes: %d")
    readfile.close()


#if __name__ == '__main__':
#    location = 'test.txt'
#    result = 'test1.json'
#    dupe_search(location, result)