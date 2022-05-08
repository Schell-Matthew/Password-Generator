import random as rand
import colorama

from args import arg_list

colorama.init(autoreset=True)


def remove_duplicates(list1):
    result = []
    for i in list1:
        if i not in result:
            result.append(i)
        else:
            print(f"{colorama.Fore.YELLOW}[*] There are duplicate entries in the given characters. Did you mean to type "
                  f"something else?")
            exit(1)
    return result


if arg_list['chars'] is not None:
    chars = remove_duplicates([char for char in arg_list['chars']])

elif arg_list["wordlist"] is not None:
    pass

else:
    print("\033[91m[!] You must specify either the -c or -w option in order for this program to run properly.\033[0m")
    exit(1)
