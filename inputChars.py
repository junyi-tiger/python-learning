import re
line = input()
try:
    num = eval(line)
    print(num*num)
except Exception:
    print('输入有误')