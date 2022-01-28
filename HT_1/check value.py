# Write a script to check whether a specified value is contained in a group of values.
# Test Data :
# 3 -> [1, 5, 8, 3] : True
# -1 -> (1, 5, 8, 3) : False

value = input("Input your value: ")

group_values = input("Input your group_values: ")

print(value in group_values)

