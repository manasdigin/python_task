password=12345
tries=0

print("welcome to the bank of mitchell")
while tries<3:
    entry=int(input("enter your pin"))
    tries+=1
    if entry==password:
        print("pin accepted now you have access to your account")
        break
    else:
        print("incorrect pin try again")

    