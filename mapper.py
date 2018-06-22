#!/usr/bin/python

import sys

def main(argv):
    word2count = {}
    line = sys.stdin.readline()
    try:
        while line:
            list = line.split(",")
            print('%s\t%s' % (list[1],list[5]))
            line = sys.stdin.readline()
    except "end of file":
        return None
if __name__=="__main__":
    main(sys.argv)