#while loop

i=1
while i<=5:
    print("P")
    i=i+1
    
i=50
while i<=100:
   print(i)
   i=i+1

j=1
while j<=10:
    print(3*j)
    j+=1

a=int(input("Write a number:"))
i=1
while i<=10:
    print(a*i)
    i+=1

num=[1,5,3]
indx=0                       
while indx<len(num):
    print(num[indx])
    indx+=1

info=(1,7,9,6)
X=9

i=0
while i<len(info):
    if(info[i]==X):
      print("found at ",i)
    else:
      print("not got")
    i=i+1

    i=0
    while i<=7:
       print(i)
       i+=1
       if(i==3):
         i=i+2

         continue
    


    #For loop
    str="Pranita"
    for char in str:
     
      print(char)
      if(char=='a'):
         print("I got a")
else:
         print("no")

         
         num=[4,6,8,6]
         X=6
         indx=0
         
         for el in  num:
            print(el)
            if(el==X):
                print("I got",indx)


                indx+=1
         
    

    #Range



for el in range(10):
        print(el)

for el in range(2,18,4):  #range(start,stop,step)
       print(el)


#Multiplication of n
n=int(input("Enter a number:"))
for el in range(n,11*n, n):

    print(el)
    #OR
#Methode 2

n=int(input("Enter a number:"))

for i in range(1,11):
    print(n*i)

 
