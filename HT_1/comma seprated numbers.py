# Write a script which accepts a sequence of comma-separated numbers from user
# and generate a list and a tuple with those numbers.
# Sample data : 1, 5, 7, 23
# Output :
# List : [‘1', ' 5', ' 7', ' 23']
# Tuple : (‘1', ' 5', ' 7', ' 23')

list_numbers = input("Input some numbers: ").split(",")

tuple_numbers = tuple(list_numbers)

print("List: ", list_numbers)

print("Tuple: ", tuple_numbers)
