def most_frequency(s):
    nl=[]
    s=s.lower()
    kl=[]
    d={}
    character=[chr(i) for i in range(ord('a'), ord('z') + 1)]
    for item in character:
        c=0
        for m in s:
            if(item==m):
                c=c+1
        if(c>0):
            nl.append(c)
            
            kl.append(item)
    x=len(nl) 
    c=0
    while(x>0):
        d[kl[c]]=nl[c]
        c=c+1
        x=x-1
    sort_orders=sorted(d.items(),key=lambda x: x[1], reverse=True) 
    for i in sort_orders:
        print(f'{i[0]} : {i[1]}')
name=input("Enter the word")
most_frequency(name)
