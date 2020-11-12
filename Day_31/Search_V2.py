import os
import re
import time
import sys
import argparse
import pickle
from threading import Thread
from colorama import init, Fore, Back, Style
import subprocess
dict1 = {}
i = 1


def get_drives():
    resp = os.popen('wmic logicaldisk get caption')
    drive = resp.read()
    return drive.split()[1:]


def creating_Dict(dr):
    global i
    for root, dir, files in os.walk(dr, topdown=True):
        dir = [each+">" for each in dir]
        files.extend(dir)
        for file in files:
            file = file.lower()
            if file in dict1:
                pass
            else:
                dict1[file] = root + "\\" + file


def create_Index1():
    tnow = time.time()
    list1_th = []
    list1 = get_drives()
    for each in list1:
        each = each + "\\"
        th1 = Thread(target=creating_Dict, args=(each,))
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
    file_to_be_searched = file1.lower()
    file_to_be_searched = r'{}'.format(file_to_be_searched)
    list1 = []
    print("")
    print(Fore.GREEN + "All files :")
    print("")
    for k in data1:
        if re.search(file_to_be_searched, k, re.I):
            str1 = data1[k]
            list1.append(str1)
    list1.sort()
    if list1:
        list3 = []
        for each in list1:
            if each.endswith(">"):
                pass
            else:
                list3.append(each)
        list1 = list3
    for index, item in enumerate(list1):
        str1 = item.rsplit("\\")
        print(Fore.WHITE+"", index + 1, " ", item.split("|")[0])
        print(Fore.YELLOW + "-"*90)

    t2 = time.time()
    print(Fore.GREEN + Style.BRIGHT + "Total time to search :", t2-t1)
    print("Total files are", len(list1))
    print()
    print("Press F to open File or D to open Directory")
    cho = input()
    cho = cho.lower()
    if cho == 'f':
        print(Fore.WHITE + "Enter Number :")
        num = int(input())
        file_open(list1[num - 1])
    elif cho == 'd':
        print(Fore.WHITE + "Enter Number :")
        num = int(input())
        dir_open2(list1[num - 1])


def search_folder(file1):
    t1 = time.time()
    fr = open("finder_index", "rb")
    data1 = pickle.load(fr)
    fr.close()
    folder_to_be_searched = file1.lower()
    list1 = []
    print("")
    print(Fore.GREEN + "All files :")
    print("")
    for k in data1:
        if re.search(folder_to_be_searched, k):
            str1 = data1[k]  # + "/" + k.split("|")[0]
            list1.append(str1)
    list1.sort()
    if list1:
        list3 = []
        if True:
            for each in list1:
                if each.endswith(">"):
                    list3.append(each)
                list1 = list3
        for index, item in enumerate(list1):
            if item.endswith(">"):
                print(Fore.WHITE + " ", index + 1, " ",
                      item.split("|")[0].rstrip(">"))
                print(Fore.YELLOW + "-"*90)
            else:
                print(Fore.WHITE + " ", index + 1, " ", item.split("|")[0])
                print(Fore.YELLOW + "-"*90)
    t2 = time.time()
    print(Fore.GREEN + Style.BRIGHT + "Total time to search :", t2-t1)
    print("Total Folders are", len(list1))
    if len(list1) == 0:
        sys.exit()
    print()
    print(Fore.WHITE + "Enter Number :")
    num = int(input())
    dir_open(list1[num - 1])


def dir_open(path1):
    folder_path = path1.split(">")[0]
    os.chdir(folder_path)
    subprocess.Popen(r'explorer /E,"." ')


def dir_open2(path):
    file1 = path.rsplit("\\")[:-1]
    k3 = "\\"
    k3 = k3.join(file1)
    os.chdir(k3)
    subprocess.Popen(r'explorer /E,"." ')


def file_open(path):
    file_name = path.rsplit("\\")[-1]
    file1 = path.rsplit("\\")[:-1]
    k3 = "\\"
    k3 = k3.join(file1)
    os.chdir(k3)
    os.startfile(file_name)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file_name", nargs='?')
    parser.add_argument("-c", help="Used to build index", action='store_true')
    parser.add_argument(
        "-f", nargs=1, help="Takes one argument as <folder_name>")
    args = parser.parse_args()
    try:
        if args.c:
            create_Index1()
        elif args.f:
            search_folder(args.f[0])
        else:
            if args.file_name == "" or args.file_name == None:
                print("Please enter a valid file name")
            else:
                fr = open("finder_index", "rb")
                if fr == False:
                    create_Index1()
                else:
                    search(args.file_name)
    except Exception as e:
        print(e)


main()
