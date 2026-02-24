# string methods 

# strings are immutable 

n="nidhir"
print(len(n))
print(n.upper())
print(n.lower())

b="nidhir!!!!!!" 
print(b.rstrip("!"))

c="nidhir123333nidhir111111" 
print(c.replace("nidhir","lambo"))

d="nidhir1prajapati11hirenkumar " 

print(d.split("1"))

#we can split by using anything but it should be in the string ,
#also we can only split by using 1 value and it can be anything like :
print("nidhir prajapati".split(" "))


# using capitalize 

a="nidhir prajapati"
print(a.capitalize())

# in grammar we have studided that after each sentence , the first letter of the sentence should be capital so ,
#similarly in python , to capitalize any first letter of a string we will use string.capitalize()


# another good thing about capitalize :

word1="nidhIr PrAjApatI"
print(word1.capitalize())

# output - Nidhir prajapati


# using center feature 


word2 = "Welcome to 100 days of code challenge"
print(word2.center(3*len(word2)))
#here i multiplied 
# or 

word3="Welcome to 100 days of code challenege" 
print(word3.center(150))

# here we wrote 150 for how much spaces further we have to center it, the value can be anything according to us


# using count feature 

x="My name is nidhir and nidhir is a good boy "

print(x.count("nidhir"))


# here we can use count feature to count any specific value in a string 


# using endswith function 

str1="nidhir111111111111"

print(str1.endswith("1"))

# or 

str2="nidhir1"

print(str2.endswith("1"))

# here , both output will be true also remember using endswith gives us only boolean datatype output 

#  also we can use endwihth function to know the end value between any specific index values 

# for example :
str2="nidhir to prajapati "
print(str2.endswith("to" , 4,9))

#output - true btw we can also overwrite any variables in python