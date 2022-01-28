#Write a function that accepts two parameters:file name and number of characters.
#A list of three blocks should appear on the screen - characters from the beginning,
#middle and end of the file.
#The number of characters in the blocks is the one entered in the second parameter.
#Think for yourself how to handle the error, for example, when the number of characters
#is greater than in the file (for example, a file of two characters and
#you need to output one character, then what to display in place of the middle block
#of characters?)
#In the repository, add the files that were tested.
#How to determine the middle of the file (from which to take the necessary characters)
#- divide the number of characters in half, and the resulting "window"
#of characters centered relative to the middle of the file and take the required number.
#If you need to round one or both parameters - look at your discretion.
#Example:

#   █ █ █ ░ ░ ░ ░ ░ █ █ █ ░ ░ ░ ░ ░ █ █ █    - good
#                     ⏫ centr
#   █ █ █ ░ ░ ░ ░ ░ ░ █ █ █ ░ ░ ░ ░ █ █ █    - not good
#                     ⏫ centr

class user_er(Exception):

    pass

def middl_find(file_user, n):
    
    try:
        with open(file_user, 'r') as f:

            text_d = f.read()

            if len(text_d) < n*3:

                raise user_er

            left_block = text_d[0:n]

            right_block = text_d[-n:]

            if n % 2 == 0:

                central_block = text_d[(len(text_d)//2 - n//2):(len(text_d)//2 + n//2)]

            else:

                central_block = text_d[(len(text_d) // 2 - n // 2):(len(text_d) // 2 + n // 2 + 1)]


            print([left_block, central_block, right_block])

    except FileNotFoundError:

        print('Your file not found')

    except user_er:

        print('You entered too large a number')

middl_find('mandr.txt',3)
            





