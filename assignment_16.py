print("welcome to mitchell's tiny adventure")

house=input("u rin a creepy house!would you like to go" '"upstairs"' "or into the" '"kitchen"\n')
if house=="kitchen":
    print('"refrigerator"' "or" '"cabinet"')
    kit=input()
    if kit=="refrigerator":
        print("eat food (yes or no)")
    elif kit=="cabinet":
        print("need salt")   
    food=input()
    if food=="yes":
        print("eat and be healthy")
    elif food=="no":
        print("die")
    
elif house=="upstairs":
    print("room , balcony")
    dff=input()
    if dff=="room":
        print("sleep")
    elif dff=="balcony":
        print("breath fresh air")






