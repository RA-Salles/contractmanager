"""
    Written by locust in 23/05/2023. Locust got no other known aliases.

    CLI: the command line interface handler.
        purpose: to start the system, keep it running and get user commands at will.
    functions and basic functioning:
        start():
            prints system functions available
        end():
            quits system
        get()
            from a list of possible functions, get user's command.
"""
from atmhandler import getdatabasepath as getdbp
K_GREETING = "hello"
FLAG_RESET = 0
K_COMMONFUNCS = {
    'func1': 'insert here a functionality imported from somewhere else!',
    'func2': getdbp #like so. This commonfuncs should contain all functions every single user can use
}
def func():
    print('hi')
def start():
    print(K_GREETING)
    print("use function 'log' to login ")
    get()
def get():
    pass
def end():
    pass
