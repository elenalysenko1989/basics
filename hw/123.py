from gettext import install
import colorama
from colorama import Fore, Back, Style


print(Back.GREEN)

what = input("What we gonna do? (+, -): ")

print(Back.CYAN)

a = float(input("Add first number: "))
b = float(input("Add second number: "))
print(Back.YELLOW)
if what == "+":
    c = a+b
    print("Result: " +str(c))
elif what == "-":
    c = a-b
    print("Result: " +str(c))
else:
    print("Wrong operation!")
    
input()
