# Welcome to mini-app made by nidhir prajapati 
print("Welcome to mipp - a mini app !".center(100))

# feature 1 - Smart text analyser 
word=input("Enter any paragraph : ")

user=int(input("Now, choose options -\n1) - Count words\n2) - Covert to Lowercase\n3) - Convert to Uppercase\n4) - Replace word\n5) - Generate Username (first two words)\n(enter number) "))

if user== 1 :
    word1=word.lower()
    word2=word1.rstrip(" ")
    a=word2.split()
    print(len(a) )