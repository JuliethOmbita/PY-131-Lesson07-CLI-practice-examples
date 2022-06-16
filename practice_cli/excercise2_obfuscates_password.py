import argparse, sys
import pandas as pd

"""
Excersice 2
Write a python CLI that inputs a csv file, reads the file, obfuscates all the passwords (turns them into stars) and writes it to an ouput csv file.
    These file names should be specified as CLI options.
Here is some boiler plate to get you started
        parser = argparse.ArgumentParser()
        parser.add_argument('infile', type=argparse.FileType('r'),
                            default=sys.stdin)
        parser.add_argument('outfile', type=argparse.FileType('w'),
                            default=sys.stdout)
        parser.parse_args(['input.txt', 'output.txt'])


        parser.parse_args([])
to test your program, using Mock User Data
"""

parser = argparse.ArgumentParser()
parser.add_argument("infile", type=argparse.FileType("r"), default=sys.stdin)
parser.add_argument("outfile", type=argparse.FileType("w"), default=sys.stdout)

args = parser.parse_args()

file_input = pd.read_csv(args.infile)
file_input["password"] = [len(i) * "*" for i in file_input["password"]]
file_input.to_csv(args.outfile)


"""
input 
    # python3 excercise2.py mock_users_passwords.txt
    python3 excercise2.py mock_users_passwords.txt outfile.csv
    python3 excercise2_obfuscates_password.py mock_users_passwords_copy.txt outfile.csv
"""
