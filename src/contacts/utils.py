import os


def do_something_useful():
    print("Replace this with a utility function")

def clean():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
