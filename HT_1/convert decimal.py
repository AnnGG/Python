#Write a script to convert decimal to hexadecimal
#Sample decimal number: 30, 4
#Expected output: 1e, 04

def toHex(dech_nums):

   digits = "0123456789ABCDEF"

   x = (dech_nums % 16)

   res = dech_nums // 16

   if (res == 0):

       return digits[x]

   return toHex(res) + digits[x]


print("Input your decimal numbers:")

list_nums = list(map(int, input().split()))

print("\nHexadechimal numbers:")

for x in list_nums:

   print(toHex(int(x)), end = " ")




