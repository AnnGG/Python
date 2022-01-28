#Програма-світлофор.
#Створити програму-емулятор світлофора для авто і пішоходів.
#Після запуска програми на екран виводиться в лівій половині - колір автомобільного, а в правій - пішохідного світлофора.
#Кожну секунду виводиться поточні кольори. Через декілька ітерацій - відбувається зміна кольорів - логіка така сама як і в звичайних світлофорах.
#Приблизний результат роботи наступний:
#      Red        Green
#      Red        Green
#      Red        Green
#      Red        Green
#      Yellow     Green
#      Yellow     Green
#      Green      Red
#      Green      Red
#      Green      Red
#      Green      Red
#      Yellow     Red
#      Yellow     Red
#      Red        Green

import time

def traffic_lights(sequence_color):

    i_sequence_color = 0

    traffic_light = []

    while True:

        if  i_sequence_color == len(sequence_color):

            i_sequence_color = 0

        else:

            traffic_light+= [sequence_color[0]+"     "+sequence_color[2]]*4
            
            traffic_light+= [sequence_color[1]+"   "+sequence_color[2]]*2
            
            traffic_light+= [sequence_color[2]+"   "+sequence_color[0]]*4
            
            traffic_light+= [sequence_color[1]+"   "+sequence_color[0]]*2

            for color in traffic_light:

                yield color

                time.sleep(1)

            i_sequence_color += 1
        


iterable_color = traffic_lights(["red","yelow","green"])

while True:

    print(*next(iterable_color))
