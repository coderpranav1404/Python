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
    


    