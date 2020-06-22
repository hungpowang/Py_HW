import time
import os
import colorama

i = 1
colorama.init(True)
while True:
    os.system("cls")
    if 1<=i<=5:
        print(colorama.Back.RED+'  ')
        print(i)
    elif 6==i:
        print((i-5)*' ', end='')
        print(colorama.Back.YELLOW+'  ')
        print(i)
    elif 6<i<11:
        print((i-5)*' ', end='')
        print(colorama.Back.GREEN+'  ')
        print(i if i<10 else 0)
    time.sleep(1)
    i = i+1 if i<10 else 1
