userInput = input("Enter a string:")
listInput = userInput.split()
counter = 0
for words in listInput:
    if words == words[::-1]:                
        counter += 1
print(f"Number of palindrome words found : {counter}")






    # if list(words) == list(reversed(words)):       (method 1)
    # method 2
