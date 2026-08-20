#lists are mutable means can be changed i.e replace
marks= [44, 77, 99, 56, 89]
print(marks[2])

marks[2]=95
print(marks)

#Slicing i.e Sublist
print(marks[1:4]) # last wala not include

#sorting
num=[1,9,5,3]
num.sort() #sort arrange it in assending order.
print(num) 

num.sort(reverse=True)
print(num) #It arrange it in descending order.
#you can arrange words also 

num.insert(0,7) #Insert helps to add another no. in any place means here 7 will be added on 0 position
print(num)

#tuple is immutable
num=(1,4,6)
#all work same as string

#question by pranita converting strings to listsa
a=input("first movie")
b=input("second movie")

c=[a,b]
print(c)
c.insert(0,3)
print(c)
print(c[2])
print(c[1:2])

