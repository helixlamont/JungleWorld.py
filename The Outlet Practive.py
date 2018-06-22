# short text adventure rpg
# Andrew Brown
# 6/18/2018
import time
import sys
t = time.sleep
def endcredits():
    t(1)
    micro_delay_print("THE OUTLET")
    t(1)
    micro_delay_print("Made by Andrew Brown\n")
    t(1)
    micro_delay_print("...\n...\n...")
    t(1)
    micro_delay_print("Pt. 2 coming soon .....")


def macro_delay_print(text):
    for x in text:
        print(x, end="")
        sys.stdout.flush()
        t(0.45)


def micro_delay_print(text2):
    for y in text2:
        print(y, end="")
        sys.stdout.flush()
        t(0.04)


t(0.5)
micro_delay_print("Welcome To the Outlet\n")
t(1.2)
macro_delay_print("......\n")
t(0.5)
name = input("What will you call yourself?")
t(1)
name2 = input("How bout your girl?")
t(1)
micro_delay_print("Okay " + name + "\n")
t(1)
answer = input("Are you ready?(yes/no, then enter)")