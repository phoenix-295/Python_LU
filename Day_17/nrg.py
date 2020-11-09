import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-s", nargs=2, help="Sum of Numbers", type=int)
parser.add_argument("-sq", nargs='?', help="Add the multiple", type=int)
parser.add_argument("-m", nargs='*', help="Add the multiple", type=int)

args = parser.parse_args()

print(args)

if args.s:
    a, b = args.s
    print("Addition is", a+b)

if args.sq:
    a = args.sq
    print("Square is :", a**2)

if args.m:
    print(args.m)
