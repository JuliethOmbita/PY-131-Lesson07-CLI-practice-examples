import argparse
import random

"""
Exercise 
Write a python CLI that 
1. Randomly selects a number from 1 to 5 when --random flag is passed
2. When the random flag is not passed, use a positional argument to restrict the inputted number to be between 1 - 5
use https://docs.python.org/3/library/random.html to generate a number
    input:
        python3 cli-1.py --random 
    output:
        4 
    input:
        python3 cli-1.py 3
    output:
        3
    input:
        python3 cli-1.py 6
    output:
        Error: number must be between 1-5

"""


my_parser = argparse.ArgumentParser()
my_parser.add_argument("-n", "--number", type=int, choices=range(1, 6))
my_parser.add_argument(
    "-r", "--random", help="Random number between 1-5", action="store_true"
)

args = my_parser.parse_args()
# print(random.randint(1, 5))
if args.number:
    print(f"Inputted number: {args.number}")
if args.random:
    print(f"Random number: {random.randint(1, 5)}")


# print(random.randint(1, 5))
# print("kldfj")
# print('00error')
# print(args)
# print(vars(args))

"""
input
python3 excercise1_randon_number.py --random 
python3 excercise1_randon_number.py -r -n 4 
python3 excercise1_randon_number.py --random -n 4 
python3 excercise1_randon_number.py  -n 4 
"""
