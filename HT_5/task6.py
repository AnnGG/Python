# Всі ви знаєте таку функцію як <range>.
# Напишіть свою реалізацію цієї функції.
# P.S. Повинен вертатись генератор.

def our_range(firstParam, secondParam=None, thirdParam=None):

    if secondParam is None:

        start = 0

        stop = int(firstParam)

        step = 1
        
    elif thirdParam is None:

        start = int(firstParam)

        stop = int(secondParam)

        step = 1

    else:

        if thirdParam == '0':

            raise ValueError("<step> argument cannot be equal 0")

        start = int(firstParam)

        stop = int(secondParam)

        step = int(thirdParam)
    
    
    if step > 0:
        
        if stop - start < stop - start - step:

            return None
        
        
        i = start
    
        
        while i < stop:

            yield i
            
            i += step
    else: 
        
        
        if start - stop > start - stop - step:

            return None
        
        
        i = start
        
        
        while i > stop:

            yield i

            i += step

print("Enter three parameters if you want to specify the start of the range,the end of the range, and the step.")

print("Enter one parameter if you only want to specify the end of the range.")

print("Enter two parameters if you only want to specify the start and end of the range.")

print("Input first parametr")

user_start = int(input())

print("Input second parametr")

user_stop = input()

if not user_stop:

    user_stop = None

print("Input third parametr")

user_step = input()

if not user_step:

    user_step = None

print(list(our_range(user_start, user_stop, user_step)))
