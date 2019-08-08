


n = int(input("enter the number of maximum starts required:"))
def pat1(n):
    for i in range (n+1):
        print ('*'*i)
pat1(n)

def pat2(n):
    for x in range(n+1):
        c = n-x
        print (' '*c + '*'*x)
pat2(n)

def pat3(n):
    for z in range(n+1):
        c = n-z
        print (' '*c + '*'*z+' '+ '*'*z)
pat3(n)    

def pat4(n):
    r = n
    for i in range (n):
        print ('*'*r)
        r = r-1
pat4(n)

def pat5(n):
    v = n
    for i in range (n):
        print (' '*i+'*'*v)
        v = v-1
pat5(n)

