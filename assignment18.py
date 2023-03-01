pin=12345
print("welcome to the bank of mitchell")
while tries<3:
    entry=int(input("enter your pin:"))
    tries=0

    tries+=1
    if  entry==pin:
      print("pin accepted now you have access to your account")
      break
    else:
      print("incorrct pin try again")
else:
     print("you have run out of tries")
