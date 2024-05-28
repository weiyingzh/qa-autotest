# try:
#     open("a.txt","r")
# except FileNotFoundError as message:
#     print(message)
# finally:
#     print('无论有无异常，我都被执行！')

# try:
#     aa = '今天天气好晴朗！'
#     print(aa)
# except Exception as message:
#     print(message)
# else:
#     print('是啊 哈哈~')
# finally:
#     print('无论有无异常，我都被执行！')

from random import randint

number = randint(1,10)
if number % 2 == 0:
    raise NameError('%d is even.' %number)
elif number % 2 != 0:
    raise NameError('%d is odd' %number)