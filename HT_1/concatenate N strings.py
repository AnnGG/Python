#Write a script to concatenate N strings.

n = int(input("Enter number of lines: "))

result= ""

for i in range(n):

    s = input("Input your line: ")

    result += s

print("\nYour concatenated strings")
print(result)
    
