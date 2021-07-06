n=int(input("Enter the number till which Fibonacci series will be displayed"))
a=0
b=1
c=a+b
print(a)
print(b)
while(c<=n):
    c=a+b
    print(c)
    a=b
    b=c
    
    
