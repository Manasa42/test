def GCD(x,y):
    while(y): 
       x, y = y, x % y 
    return x 
a = 20
b= 30
print (GCD(20,30)) 
