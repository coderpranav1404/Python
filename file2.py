#if ,else if (elif), else

color="yellow"
if(color=="green"):
    print("Its so green")

elif(color=="Purple"):
    print("My fav color")

else:
    print("I dont like any color")




#2nd example 
age=int(input("Enter your age:"))
""
if(age >= 18):
    a="You are eligible to vote"

if(age >=15 and age <18):    
    a="You have right to learn"

else:
    a="You are a child labour"

print("Your report is",a)

# Bro you finally did it. It worths after a limitless struggle for more than 2 yrs.
# Note:-elif statemwnt will run only when "if" statement becomes wrong.



#3rd example
num1=int(input("Enter first no."))
num2=int(input("second no."))

if(num1>=num2):
    print("num1 is greatest",num1)

else:
    print("num2 is greatest",num2)