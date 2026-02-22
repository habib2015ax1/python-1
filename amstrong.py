n=int(input("enter a number"))
temp=n
sum=0

while temp>0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10

if n== sum:
    print(n,"is an amstrong number")
    
else:
    print ("it is not an amstrong number")

 
