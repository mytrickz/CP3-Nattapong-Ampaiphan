userInput = int(input("Input : "))
print("--Output--")
for i in range(userInput):
    print(" "*(userInput-(i+1))+("*"*(i+1))+("*"*i))
