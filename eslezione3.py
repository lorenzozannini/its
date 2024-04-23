def stampad(d):
    for i in d:
        print(i,":",d[i])

def stampal(l):
    for i in l:
        print(i) 
"""
#4.1
pizze=["Margherita","Diavola","Crostino"]
stampal(pizze)
for i in pizze:
    print("Mi piace la piza",i)
print("I like ",pizze[0])
print("My favourite pizza is ",pizze[1])
print("I hate ",pizze[2])

#4.2
animals=["dog","cat","bunny"]
stampal(animals)
print("I like ",animals[0])
print("My favourite pets is ",animals[1])
print("I hate ",animals[2])
print("They are all pets")

#4.3
for i in range(1,21):
    print(i)

#4.4
numbers=[]
for i in range(1,1000000):
    numbers.append(i)
stampal(numbers)

#4.5
print(max(numbers))
print(min(numbers))
print(sum(numbers))

#4.6
n1_20=[]
for i in range(1,21):
    n1_20.append(i)
stampal(n1_20)
"""
#4.7
n3_30=[]
for i in range(3,31,3):
    n3_30.append(i)
stampal(n3_30)

#4.8
for i in range(1,11):
    print(i**3)

#4.9
cubes=[i**3 for i in range(1,11)]
print(cubes)

#4.10