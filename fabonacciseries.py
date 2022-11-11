n=int(input("enter number of term upto which fibonacci series is to printed:"))
print("fabonacci series....")
f=0
s=1
print(f,s,end=' ')
i=0
while i<n-2:
    t=f+s
    print(t,end=' ')
    f=s
    s=t
    i+=1
    
