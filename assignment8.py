name=input("hey,what is your name?" )
age=int(input("ok,{}, how old r u?".format(name)))
if age<16:
    print("you can't drive,{}".format(name))
elif age==16 or age==17:
    print("you can drive but you can't vote,{}".format(name))
elif age==18 or age<=24:
    print("you can vote but you can't rent a car,{}".format(name))
else:
    print("you can do pretty much anything,{}".format(name))



