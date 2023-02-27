import datetime
def daynumber1():
    print("weekday1:monday")
def daynumber2():
    print("weekday2:tuesday")
def daynumber3():
    print("weekday3:wednesday")
def daynumber4():
    print("weekday4:thursday")
def daynumber5():
    print("weekday5:friday")
def daynumber6():
    print("weekday6:saturday")
def daynumber7():
    print("weekday7:sunday")
def today():
    today=datetime.datetime.now()
    weekday=today.strftime("%A")
    print("today is:",weekday)


day=int(input("write"))

if day==1:
    daynumber1()
elif day==2:
    daynumber2()
elif day==3:
    daynumber3()
elif day==4:
    daynumber4()
elif day==5:
    daynumber5()
elif day==6:
    daynumber6()
elif day==7:
    daynumber7()
else:
    print("error:",day)
    today()

