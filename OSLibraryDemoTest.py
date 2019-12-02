# 本文件对os库的一些基础函数进行展示

# 路径操作
import os.path

# os.path.abspath(path):该函数返回path在当前系统中的绝对路径
os.path.abspath(path="file.txt")
# os.path.normpath(path):归一化path的表示形式，统一用\\分隔路径
os.path.normpath("D:\\file.txt")
# os.path.relpath(path):返回当前程序与文件之间的相对路径(relative path)
# os.path.dirname(path):返回path中的目录名称
# os.path.basename(path):返回path中最后的文件名称
# os.path.join(path, paths):组合path和paths，返回一个路径字符串
# os.path.exists(path):判断path对应文件或目录是否存在，返回True或False
# os.path.isfile(path):判断path对应的是否是一个文件
# os.path.isdir(path):判断path对应得是否是一个目录
# os.path.getatime(path):返回对应文件或目录上一次的访问时间(access)
# os.path.getmtime(path):返回path对应文件或目录最近一次的修改时间(modify)
# os.path.getctime(path):返回path对应文件或目录的创建时间(create)
# os.path.getsize(path):返回path对应文件或目录的大小

# 进程管理
import os
os.system("C:\\Windows\\System32\\calc.exe")

# 环境参数
# 获取或改变系统环境信息
# os.chdir(path):修改程序当前的工作目录
# os.getcwd():返回程序当前的工作目录
# os.getLogin():获得当前系统登录用户名称
# os.urandom(n):获得n个字节长度的随机字符串，通常用于加解密运算
os.urandom(10) #不能打印的字符将16进制表示

# 针对日常的文件和目录管理任务，shutil模块提供了一个易于使用的高级接口：
'''
>>> import shutil
>>> shutil.copyfile('data.db', 'archive.db')
>>> shutil.move('/build/executables', 'installer')
'''
# glob模块提供了一个函数用于从目录通配符搜索中生成文件列表：
'''
>>> import glob
>>> glob.glob('*.py')
['primes.py', 'random.py', 'quote.py']
'''
# 获取执行脚本附加的命令行参数：sys.argv
'''
在命令行中执行"python demo.py one two three"后得：
>>> import sys
>>> print(sys.argv)
['demo.py', 'one', 'two', 'three']
'''

# 错误输出重定向和程序终止
'''
sys还要stdin, stdout, stderr属性，即使在stdout被重定向时，后者也可以用于显示警告和错误信息
>>> sys.stderr.write('Warning, log file not found, starting a new one\n')
Warning, log file not found, starting a new one
程序终止：
>>> sys.exit()
'''