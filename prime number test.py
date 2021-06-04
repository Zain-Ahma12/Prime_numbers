'''
date            9-05-2021
Programe to test a number is prime 
'''


def prime(n):
    s=0
    if n in [1,2,3,5,7,11,13]:
        return("Prime")
    elif n in [0,4,6,8,9,10,12,14,15,16]:
        return("Not prime")
    else:
        a=int(n**0.5)
        for i in range(2,a+1):
            if n%i!=0:
                s+=1
            else:
                continue
    if s==a-1:
        return("Prime")
    else: 
        return("Not Prime")   



num=int(input("Enter a number: "))
l=[]
for i in range(num+1):
    z=prime(i)
    if z=="Prime":
        l.append(i)
print(f"The list of all Prime numbers in range 0 to {num}")
print(l)
print("Total Prime numbers =",len(l))
print(f'Thier sum = {sum(l)}')


