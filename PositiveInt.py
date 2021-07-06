n=int(input("Enter the length of the list"))
l=[]
while(n>0):
    l.append(int(input("Enter the number that will be included in the range")))
    n=n-1
print("The positive numbers are:")
for items in l:
    if(items>0):
        print(items)

