string = input("enter a string:")
def vow(string):
    vowels = ['a','e','i','o','u']
    count = 0
    for i in range (len(string)):
        if string[i] in vowels:
             count += 1
    print ("the number of vowels in string is", count) 

vow(string)

