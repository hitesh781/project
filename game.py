from operator import truediv
import random
count=3
ans='y'
win=False
possible_action=["rock","paper","scissor"]
computer_action=random.choice(possible_action)    
while ans=='y':
    num1=random.choice(possible_action)
    guess=input("enter your choice:")
if guess==rock and num1==paper:
    print("u loss")
    wwin=true
else:
    print("u win")    
    count-=1
    print("computer_action was",num1)
if guess==paper and num1==rock:
    print("u win")
else:
    print("u loss")
    count-=1
if guess==scissor and num1==rock:
    print("u loss")
else:
    print("u win")
