#Daily Exercise 1/4
user_string = input("Please enter a string (10 characters long): ")
if len(user_string) < 10:
    print("String not long enough")
elif len(user_string) > 10:
    print("String too long")
else:
    print("Perfect string")
    print("First character:", user_string[0])
    print("Last character:", user_string [-1])
constructed_string = ""
for i in range(len(user_string)):
    constructed_string += user_string[i]
    print(constructed_string)


#Bonus