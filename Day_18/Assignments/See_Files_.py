import os
import re
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    "-ri", help="Search in recursive manner", action="store_true")
parser.add_argument(
    "-si", help="Search in Root dir", action="store_true")
parser.add_argument("txt", nargs='?', help="Takes input as string to search")
parser.add_argument("path", nargs="?", help="Takes input as path to search")

args = parser.parse_args()


def rec(txt, path):
    print(path)
    d2 = []
    for r, d, f in os.walk(path, topdown=True):
        for files in f:
            s = r + "\\" + files
            d2.append(s)

    for each in d2:
        file_r = open(each, "r")
        for num, line in enumerate(file_r, 1):
            if txt.lower() in line.lower():
                print("Line :", num, "\t", each)
        file_r.close()


def sf(txt, path):
    yourpath = path
    for r, d, f in os.walk(yourpath, topdown=False):
        for files in f:
            if r == yourpath:
                f1 = (os.path.join(r, files))
                file_r = open(f1, "r")
                for num, line in enumerate(file_r, 1):
                    if txt.lower() in line.lower():
                        print("Line :", num, "\t", f1)
                file_r.close()


if args.ri:
    txt = args.txt
    path = args.path
    rec(txt, path)
elif args.si:
    txt = args.txt
    path = args.path
    sf(txt, path)
