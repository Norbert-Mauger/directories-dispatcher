import sys
import os
import getopt
import string
import random
from createdummyfiles import create_dummy_files
from createsubdirs import create_subdirs
import time


def main(argv):
    n_files = 100
    try:
        opts, args = getopt.getopt(argv, "hn:", ["numfile="])
    except getopt.GetoptError:
        print('filemovetest.py -n <number of files>')
        sys.exit(2)
    if len(opts) == 0:
        print('filemovetest.py -n <number of files>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('filemovetest.py -n <number of files>')
            sys.exit()
        elif opt in ("-n", "--n"):
            n_files = arg

    try:
        n_files = int(n_files)
    except:
        print('filemovetest.py -n <number of files>')
        sys.exit()

    print('Number of files to create: ', n_files)

    dir = "d:/tmp/"
    try:
        os.stat(dir)
    except:
        os.mkdir(dir)
    res_create = create_dummy_files(n_files, dir)
    res_move = create_subdirs(dir)

    print(res_create)
    print(res_move)



if __name__ == "__main__":
    main(sys.argv[1:])
