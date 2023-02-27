print("two questions:")
print("think of an object,and i'll try to guess it")
print("Question1) Is it animal,vegetable,or mineral")
q1=input()

print("(Question2) is it bigger than a breadbox?")
q2=input()

if q1=='animal':
    if q2=="no":
        print("my guess is that  u r thinking of a mouse")
    else:
        print("my guess is that you are thinking  of a squirrel")
elif q1=='vegetable':
    if q2=="yes":
        print("my guess is that you are thinking of a watermelon")
    else:
        print("my guess is that you are thinking of a carrot")

elif q1=="mineral":
    if q2=="yes":
        print("my guess that you're thinking of a camero")
    else:
        print("my guess is that you are thinking of a paperclip")






    
