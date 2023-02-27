gender=input("what is your gender" "(M or F)")
fname=input("firSt name:")
lname=input("last name:")
age=int(input("age:"))
if gender=="M":
    if age>=20:
        print("mr.",fname+lname)   
    else:
        print(fname+lname)


elif gender=="F" and age>=20:
    yes=input("are you married" "(y or n)")
    if yes=="y":
        print("mrs.",lname) 
else:
    print(fname+lname)




