num=4
factorial=1
if num<0:
	print("factorial doesnt exist")
else:
	print("factorial exist")
for i in range(1,num+1):
	factorial=factorial*i
	
print("factorial of num is", factorial)
