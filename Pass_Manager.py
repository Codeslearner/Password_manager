import random as unique
import pickle as pic

info = {}
with open("pass.man", "br") as readfile:
    info = pic.load(readfile)
s = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ@!&$"
len_password = int(input("Enter how many digits of password you required:  "))

password = "".join(unique.sample(s, len_password))
print(password)

answer = int(input("Would you like to save the password ? 1.YES  2.NO  :   "))
if answer == 1:
    account_name = input("Enter Account Name:  ")
    info[account_name] = password
    with open("pass.man", "bw") as save:
        pic.dump(info, save)
else:
    print("OK")
