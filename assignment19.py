import random
number=random.randint(1,100)
guess_count=0
max_guesses=7


while guess_count<max_guesses:
    guess=int(input("try guessing"))
    guess_count=guess_count+1

    if guess==number:
        print("awesome")
    elif guess<number:
        print("too low")
    else:
        print("too high")

if  guess_count==max_guesses:
    print("stopped,number is,",number)



