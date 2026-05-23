numbers = [1,2,3,4,5,6]

even = [x for x in numbers if numbers if x %2==0]
print ("list of even numbers origanal",even)


MyDict = {str(x): x**2 for x in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]}
print (MyDict)

def square(n):
    return n*n
number = (1,2,3,4,5,6,7,8,9,10)
result = map(square, numbers)
print(list(result))

list1=[1,2,3,4,5]
list2=[6,7,8,9,10]
def add(x,y):
    return x+y

result=map(add,list1,list2)
print(list(result))