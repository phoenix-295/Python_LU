# positional Arguments

import argparse

parser = argparse.ArgumentParser()

parser.add_argument("nikhil", type=int)

arg = parser.parse_args()

print(arg)
print(arg.nikhil)
