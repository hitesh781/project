phonebook=dict()
n=int(input("enter total no of contact:"))
i=1
while i<=n:
    key=input("enter contact name:")
    value=input("enter phone number:")
    phonebook[key]=value
    i=i+1
    name=input("\nenter phone contect to delete:")
    l=phonebook.keys()
    flag=1
    for key in l:
        if key==name:
            flag=1
            del phonebook[name]
            break
        else:
            flage=0
    if flag==0:
        print("\n",name,"does not exit in dictionary\n")
    print("phonebook information\n")            
    print("name","t","phone number")
    for key in l:
        print(key,"\t",phonebook[key])