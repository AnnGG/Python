#Write a script to sum of the first n positive integers

n = int(input("Input a number: "))

res = sum(range(n+1))

print("Sum first", n ,"positive integers:",res)
