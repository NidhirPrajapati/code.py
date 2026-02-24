# # # welcome 
# # word=input("Enter any sentence : ")
# # if word=="" :
# #     print("Please enter a valid data")
# # else :
# #     wordsplit=word.split()
# #     len=len(wordsplit)
# #     print(len)
 
# # # here we can use split(" ") also but split() is more efficient beacause it will only count the spaces after words not 
# # # - unneccesary spaces 

# #problem 2 

# word=input("Enter any upper cased sentence : ")
# if word==" " :
#     print("Please Enter ")
# else :

#     word=word.lower()
#     print(word.replace(" ","-"))



# problem 3 

word=input("Enter any upper cased sentence with lot of spaces : ")

word=word.lower()
word=word.rstrip(" ")

word1=word.split(" ")

username="_".join(word1)



print(username)