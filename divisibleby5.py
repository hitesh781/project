from unittest import skip


l1=[12,75,150,180,145]
for i in l1:
    for j in l1:
        if j>150:
            continue
         
        print(j)    
    
    if i%5==0:
        print(i)

