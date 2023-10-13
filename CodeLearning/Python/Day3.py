# Python数据类型转换

""" # int(x[,base]) 将x转换为一个整数
# class int(x, base = 10)
# x--字符串或数字，base--进制数，默认十进制

print(int())    # 不传参得到0
print(int(3))
print(int(3.5))
# 如果是带参数base的话，12要以字符串的形式进行输入，12为16进制
print(int("9", 16))
print(int("0xa", 16))
 """

""" # float()将整数和字符串转换为浮点数
# class float([x])
# x--整数或者字符串
print(float('123'))
print(float(23.1111)) """

""" # comlex()函数用于创建一个值为 real + imag * j 的复数
# 或者转化一个字符串或数为复数
# 如果第一个参数为字符产，则不需要指定第二个参数
# class complex([realm[,img]])
# real--int, long, float或字符串
# imag--int, long, float
print(complex(1, 2))
print(complex(1))
print(complex("1"))
# 不能再中间加空格，如果写成"i + 2j"会报错
print(complex("1+2j"))
 """

""" # str()函数将对象转化为适合人阅读的形式
# class str(object = "")
s = "run noob!"
print(str(s))
dict1 = {"one":"tencent", "two":"google", "three":"ali"}
print(str(dict1))
 """

""" # repr()将对象转化为供解释器读取的形式
# repr()——返回一个string格式
s = "runoob"
print(type(repr(s)))
print(repr(s))
dict2 = {"one":"tencent", "two":"google", "three":"ali"}
print(repr(dict2))
print(type(repr(dict2))) """

""" # eval(str)计算在字符串中的有效Python表达式，并返回一个对象
# eval()函数执行的代码具有潜在的安全风险，使用不受信任的字符串作为表达式可能导致代码注入漏洞
# 字符串表达式可以包含变量、函数调用、运算符和其他Python语法
# eval(expression[, blobals[, locals]])
# expression--表达式
# globals--变量作用域，全局命名空间，如果被提供，则必须为一个字典对象
# locals--变量作用域，局部命名空间，如果被提供，可以是任何映射对象
# eval()函数将字符串expression解析为Python表达式，并在指定的命名空间中执行它
x = 7
print(eval("3*x"))
print(eval("pow(2, 3)"))
namespace = {'a':2, 'b':10}
result = eval("pow(a, b)", namespace)
print(result)
 """

# tuple()序列->元组, list()序列->列表, set()转换为可变集合, frozenset()转换为不可变集合

# frozenset()，为什么需要为什么需要冻结的集合（即不可变的集合）呢？
# 因为在集合的关系中，有集合的中的元素是另一个集合的情况
# 但是普通集合（set）本身是可变的，那么它的实例就不能放在另一个集合中（set中的元素必须是不可变类型）。
# 所以，frozenset提供了不可变的集合的功能，当集合不可变时，它就满足了作为集合中的元素的要求，就可以放在另一个集合中了。

# chr()整数->字符, ord()字符->整数, hex()整数->十六进制, oct()整数->八进制

""" # dict()创建一个字典，d必须是一个(key, value)的元组序列
# 一般实例在Day1中的字典中体现

# 只使用关键字参数创建字典
numbers = dict(x = 5, y = 0)
print("numbers = ", numbers)
# 使用可迭代对象创建字典
numbers2 = dict([('x', 5), ('y', 6)], z = 7, w = 8)
print(numbers2)
# 使用映射来创建字典
numbers3 = {'x':4, 'y':5}
print(numbers3)
 """

""" # Python3 数据类型转换
# 隐式类型转换——自动完成，较低数据类型会被转为较高数据类型以避免数据丢失
# 显式类型转换——需要使用类型函数转换
num_int = 12
num_flo = 12.123
num_sum = num_int + num_flo
print(num_sum)
print(type(num_sum))

num_str = "456"
# print(num_flo + num_str) # 会出现报错，因为无法进行隐式转换
# 所以使用了显示转换
print(num_str + str(num_flo))
print(num_int + int(num_str)) """

 # 运算符
# 算术运算符
# +  -  *  /  %   **  //
# 加 减 乘 除 取余 幂 取整数

# 比较运算符
# ==    !=      >     <      >=         <=
# 相等  不等于  大于  小于   大于等于     小于等于

# 赋值运算符
# = 赋值; += 加法赋值; -= 减法赋值; *= 乘法赋值; /= 除法赋值
# %= 取模赋值; **= 幂运算赋值; //=取整除赋值;
# := 海象运算符，可在表达式内部为变量赋值
a = "100"
if (n := len(a)) < 10:
    print(f"a has {n}, and...") 

# 位运算符
# & 和; | 或; ^ 异或; ~ 取反; << 左移; >> 右移
# and 拥有更高优先级

# 逻辑运算符
# python 中的 and 从左到右计算表达式，若所有值均为真，则返回最后一个值，若存在假，返回第一个假值；
# or 也是从左到有计算表达式，返回第一个为真的值；
# 其中数字 0 是假，其他都是真；
# 字符 "" 是假，其他都是真；
a = 10; b = 20
print(a and b)
print(a or b)
print(not(a and b))
# not bool非; True返回False，False返回True

# 成员运算符
# in 是否在序列中，是就返回True，否则False；not in就反过来

# 身份运算符
# is 判断两个标识是否引用于一个对象，是就True，否就False
# is not 反过来

