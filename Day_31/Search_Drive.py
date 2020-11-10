import os
import re
import time
import argparse
import pickle
from threading import Thread


dict1 = {}
i = 1


def get_drives():
    resp = os.popen('wmic logicaldisk get caption')
    drive = resp.read()
    return drive.split()[1:]


def creating_Dict():
    global i
    list1 = get_drives()
    for each in list1:
        each = each + "\\"
        for root, dir, files in os.walk(each, topdown=True):
            dir = [each+">" for each in dir]
            files.extend(dir)
            for file in files:
                file = file.lower()
                if file in dict1:
                    file = file + "|" + str(i)
                    dict1[file] = root
                    i = i + 1
                else:
                    dict1[file] = root
            

def create_Index1():
    tnow = time.time()
    list1_th = []
    th1 = Thread(target=creating_Dict)
    th1.start()
    list1_th.append(th1)

    for th1 in list1_th:
        th1.join()

    fw = open("finder_index", "wb")
    pickle.dump(dict1, fw)
    fw.close()
    t2 = time.time()
    print("Time taken to Create Index :", t2-tnow)


def search(file1):
    t1 = time.time()
    fr = open("finder_index", "rb")
    data1 = pickle.load(fr)
    fr.close()
    for k, v in data1.items():
        k = k.split("|")[0]
        m = re.search(file1, k, re.I)
        if m:
            print(k, "\t", v)
    t2 = time.time()
    print("Total time to search :", t2-t1)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file_name", nargs='?')
    parser.add_argument("-c", help="Create Index", action='store_true')
    args = parser.parse_args()
    try:
        if args.c:
            create_Index1()
        else:
            if args.file_name == "" or args.file_name == None:
                print("Please enter a valid file name")
            else:
                search(args.file_name)
    except Exception as e:
        print(e)


main()
