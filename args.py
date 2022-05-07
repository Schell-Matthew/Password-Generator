import argparse as args

parser = args.ArgumentParser(description="Generate random passwords with certain rules you set")

# class CustomHelpFormatter(args.HelpFormatter):
#     def format_help(self):
#         filename = "help.txt"
#         with open(filename, 'r') as f:
#             for line in f:
#                 print(line, end='')

def validate_args(arguments):
    pass

parser.add_argument('-c', '--chars', action="store", help=
                    "Only allow specific characters to be used in the password. If argument not present, all characters"
                    "will be used. Can't be used with --wordlist")
parser.add_argument('-w', '--wordlist', action="store", help=
                    "Pass a wordlist containing words that you want to go in your password. Can't be used with --chars")
parser.add_argument('-l', '--length', action="store", type=int, help=
                    "Specify password length")
parser.add_argument('-n', '--number-of-passwords', action='store', type=int, help=
                    "The number of passwords you want generated")


