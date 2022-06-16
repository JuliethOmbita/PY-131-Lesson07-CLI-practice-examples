import argparse

my_parser = argparse.ArgumentParser()
my_parser.add_argument('-a', action='store', type=int, choices=range(1, 5))

args = my_parser.parse_args()

print(vars(args))
