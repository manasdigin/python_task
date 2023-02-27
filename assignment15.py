print("two more questions baby")
print("think of something and i'll try to guess it!")

q1=input("Question 1) does it stay inside or outside or both:")
q2=input("Queastion 2) Is it a living thing:")

if q1=="inside" and q2=="alive":
    print("house plant")
if q1=="inside" and q2=="not alive":
    print("shower curtain")
if q1=="outside"and q2=="alive":
    print("bison")
if q1=="outside"and q2=="not alive":
    print("billiboard")
if q1=="both" and q2=="alive":
    print("dog")
if q1=="both" and q2=="not alive":
    print("cell phone")
if q1 not in "[inside,outside,both]" or q2 not in "[alive,not alive]":
    print("then what else could you be thinking of besides a python?!?")
