import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-pi", help="Pi value", action="store_const", const=3.14)
parser.add_argument("-F", action="store_true")
args = parser.parse_args()

print(args)

if args.pi:
    print(args.pi)

if args.F:
    print("Hello")
