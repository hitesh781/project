a=int(input("enter the no upto u want to print prime no:"))
for i in range(2,a+1):
    stop=int(i/2)+1
    for j in range(2,stop):
        if (a%j==0):
            #print(not prime no)
            break
    else:
        print(i  ,end='')