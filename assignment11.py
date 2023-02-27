weight=int(input("pleaase enter your current earth weight:"))

print("i have information for the following planets:")
print("1.venus      2.mars     3.jupiter")
print("4.saturn     5.uranus   6.neptune" )
planet=float(input("which planet are you visiting?"))
venus=0.78*weight
mars=0.39*weight
jupiter=2.65*weight
saturn=1.17*weight
uranus=1.05*weight
neptune=1.23*weight
if planet==1:
    print("your weight would be",venus,"punds on that planet")
elif planet==2:
    print("your weight would be" ,mars, "pounds on that planet")
elif planet==3:
    print("your weight would be",mars,"pounds on that planet")
elif planet==4:
    print("your weight would be",saturn,"pounds on that planet")
elif planet==5:
    print("your weight would be",uranus,"pounds on that planet")
else:
    print("your weight would be",neptune,"pounds on that planet")
    

