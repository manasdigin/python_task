print("welcome to mitchell's tiny adventure")
print("u r in a creepy house would you like to go 'kitchen' or 'upstairs'")
house=input()
if house=="kitchen":
    print("go 'refrigerator' or 'cabinet'?")
    kitchen=input()
    if kitchen=="refrigerator":
        print("will you eat food (yes or no)")
        food=input()
        if food=="yes":
            print("eat and be healthy")
        else:
            print("die of starvation")
    elif kitchen=="cabinet":
        print("need salt")
elif house=="upstairs":
    print('room or balcony')
    ans2=input() 
    if ans2=="room":
        print("sleep")
    elif ans2=="balcony":
        print("breath fresh air") 
