        
n = int(input("Enter a range for Prime Numbers : "))
l = []
for i in range(2,n+1):
    l.append(i) 

for x in l :
    for y in l :
        if y%x==0 and y!=x:
            # if y!=x:
            l.remove(y)

print (l)