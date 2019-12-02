## 类对象
### 类对象支持：属性引用和实例化
- 属性引用语法：obj.name
- 实例化： x = MyClass()
- 访问类的属性和方法： x.id、x.f()
### 类的构造方法
`__init__()`方法，该方法在类实例化时会自动调用
```
def __init__(self):
    self.data = []
```
带参数的`__init__()`方法
```
class Complex:
    def __init__(self, realpart, imagepart):
        self.r = realpart
        self.i = imagepart
x = Complex(3.0, -4.5)
print(x.r, x.i)
```
### self代表类的实例，而非类
类方法与普通的函数有一个特别的区别——它们必须有一个额外的第一个参数名称，按照惯例它的名称是self,self代表的是类的实例。
```
class people:
    # 定义基本属性
    name = ''
    age = 0
    # 定义私有属性，其在类外部无法直接进行访问
    __weight = 0
    # 定义构造方法
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w
    def spead(self):
        print("%s说：我%d岁。"%(self.name, self.age))

# 实例化类
p = people('runoob', 10, 30)
p.speak()
```
### 继承
- 支持多继承。
基类的顺序：若基类中有相同的方法名，而在子类使用时未指定，python从左至有搜素。
- 方法重写：
```
class Parent:
    def myMethod(self):
        print('调用父方法')

class Child(Parent):
    def myMethod(self):
        print('调用子类方法')
c = Child()
c.myMethod() # 子类调用重写方法
super(Child, c).myMethod() # 用子类对象调用父类已被覆盖的方法
```
### 类属性与方法
#### 类的私有属性
__private_attrs：两个下划线开头，声明该属性为私有，不能在类的外部被使用或直接访问。在类内部的方法中使用时self.__private_attrs
#### 类的方法
在类的内部，使用def关键字来定义一个方法，与一般函数定义不同，类方法必须包含参数self，且为第一个参数，self代表的是类的实例。
#### 类的私有方法
__private_method：只能在类的内部调用。self.__private_methods
#### 类的专有方法：
- __init__:构造函数，在生成对象时调用
- __del__:析构函数，释放对象时使用
- __repr__:打印，转换
- __setitem__:按照索引赋值
- __getitem__:按照索引取值
- __len__:获得长度
- __cmp__:比较运算
- __call__:函数调用
- __add__:加运算
- __sub__:减运算
- __mul__:乘运算
- __truediv__:除运算
- __mod__:求余运算
- __pow__:乘方
#### 运算符重载
Python同样支持运算符重载，我们可以对类的专有方法进行重载，实例如下：
```
class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def __str__(self):
        return 'Vector(%d, %d)' % (self.a, self.b)
    
    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)

v1 = Vector(2, 10)
v2 = Vector(5, -2)
print( v1 + v2)
# 执行结果如下：
# Vector(7, 8)
```
