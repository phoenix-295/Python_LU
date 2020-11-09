import argparse

parser = argparse.ArgumentParser()
# Positional argument
# parser.add_argument("button", choices=['Like', 'Share', 'Subscribe'])
parser.add_argument(
    "-b", choices=['Like', 'Share', 'Subscribe'], default="Like", required=True)

args = parser.parse_args()

print(args)
