import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-s", help="Square of Number", type=int)

args = parser.parse_args()

print(args)
if(args.s):
    a = args.s
    print(a**2)
