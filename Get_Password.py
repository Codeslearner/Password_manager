import pickle as pic
import pyperclip as clipboard
m_password = input("Enter Master password:  ")
if m_password == "sandeep":
    account_name = input("Enter account name:  ")
    with open("pass.man", "br") as readfile:
        info = pic.load(readfile)

    if account_name in info:
        clipboard.copy(info[account_name])
        print("Password Copied")
    else:
        print("Password not found")

else:
    print("Password doesn't match")