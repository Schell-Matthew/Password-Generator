import argparse
import argparse as args

parser = args.ArgumentParser(description="Generate random passwords with certain rules you set")

# class CustomHelpFormatter(args.HelpFormatter):
#     def format_help(self):
#         filename = "help.txt"
#         with open(filename, 'r') as f:
#             for line in f:
#                 print(line, end='')


parser.add_argument('-c', '--chars', action="store", dest="chars", help=
                    "Only allow specific characters to be used in the password. If argument not present, all characters"
                    "will be used. Can't be used with --wordlist")
parser.add_argument('-w', '--wordlist', action="store", dest="wordlist", help=
                    "Pass a wordlist containing words that you want to go in your password. Can't be used with --chars")
parser.add_argument('-l', '--length', action="store", dest="length", type=int, help=
                    "Specify password length")
parser.add_argument('-n', '--number-of-passwords', action='store', dest="numPass", type=int, help=
                    "The number of passwords you want generated")

args = parser.parse_args()
if args.chars is not None and args.wordlist is not None:
    print("\033[91m[!] The --chars and --wordlist arguments can't be used together.\033[0m")
    exit(1)
arg_list = vars(args)
