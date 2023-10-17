# print("Run Noob!")
# 这个是注释

""" 缩进
 缩进会表示同一个代码块
 同一个代码块的不同的缩进会报错
 这是一个错误例子
if True:
    print("right")
else:
    print("worng")
   print("错误")

 """

""" Number数字类型
数字类型只有4种
int(长整型) bool float complex 
"""

""" 字符串的运用
str='123456789'
 
print(str)                 # 输出字符串
print(str[0:-1])           # 输出第一个到倒数第二个的所有字符
print(str[0])              # 输出字符串第一个字符
print(str[2:5])            # 输出从第三个开始到第六个的字符（不包含）
print(str[2:])             # 输出从第三个开始后的所有字符
print(str[1:5:2])          # 输出从第二个开始到第五个且每隔一个的字符（步长为2）
print(str * 2)             # 输出字符串两次
print(str + '你好')         # 连接字符串
 
print('------------------------------')
 
print('hello\nrunoob')      # 使用反斜杠(\n)转义特殊字符，换行了
print(r'hello\nrunoob')     # 在字符串前面添加一个 r，表示原始字符串，不会发生转义 
 """

""" # 记得终端要进入Python环境
# 之前运行报错，是因为没有进入Python环境
import sys;x = "Noob";sys.stdout.write (x + '\n')
 """

""" # print输出是默认换行的
#如果不想要默认换行可以加 end = " "
print("换")
print("行")
print("----------------")
print("不", end = " ")
print("换", end = "@")
print("行", end = "*") """

""" # 列表转换
# 这里是用空格作为分隔标志，列表内容可以修改
def reverseList(input):
    # 这一步是用空格把字符串分隔，每个单词分隔为列表
    inputWords = input.split(" ") 

    # 开头:步数:结尾
    # 逆向，从尾到头，中间的空格表示从-1到末尾得出反转列表
    inputWords = inputWords[-1: :-1]

    # 修改列表内容
    inputWords[1] = "改"

    #重新组合字符串
    output = " ".join(inputWords)
    return output

if __name__ == "__main__":
    input = "1 2 3 4 5 6 7 8"
    input_2 = "One Two Three"
    rw = reverseList(input)
    rw2 = reverseList(input_2)
    print(rw)
    print(rw2) """

""" Turple
# 列表是一种特殊的Turple(元组)，元组里面元素无法修改
# 但是可以添加可变的List(列表)
# 其他的索引与切片和List一致 """

""" # Set(集合)
# 无序，可变，集合内的元素不会重复
# 可以进行交集、并集、差集等常见的集合操作
# 空集合必须为: Set(), 而不是{}
BAT = {"Baidu", "Ali", "Tencent"}
print(BAT)

if "Runoob" in BAT:
    print("在集合BAT中")
else:
    print("不在集合中")

# 集合运算
a = set("abcd1234")
b = set("bcde3456")

# 差集
print(a - b)
# 并集
print(a | b)
# 交集
print(a & b)
# a与b中不同时存在的元素
print(a ^ b) """

""" # Dictionary(字典)
# List列表是有序对象的集合，字典是无需对象的集合
# 字典的对象是通过键来存取的，并非是通过偏移存取的
# 字典是映射的类型——>键值(Key):值(Value)
# 其中，键值不可变，同一个字典中键值必须唯一

# 空字典
dic = {}

dic["one"] = "1 - 这是Value"
dic[2] = "2 - 这是Value2"
dict_1 = dict(zip(["one", "two", "three"], [1, 2, 3]))  # 映射函数方式来构造字典
dict_2 = dict([("one", 1), ("two", 2), ("three", 3)])    # 可迭代对象方式来构造字典

print(dict_1)
print(dict_2)

tinydict = {"name":"runoobLearn", "code":"Python", "site":"1"}

print(dic["one"])   # 输出键为 "one" 的值 
print(dic[2])   # 输出键为 2 的值
print(tinydict) # 输出字典
print(tinydict.keys())  # 输出字典所有键值
print(tinydict.values())    # 输出所有值 """

""" # bytes 
# Python3中，bytess类型表示的是不可变的二进制序列
# bytes类型中的元素是整数值(0-255)，而不是Unicode字符
# 最常见的创建bytes对象的方式就是使用b前缀
# 也可以使用bytes()函数把其他类型的对象转换为bytes类型
# bytes与字符串类似，也可以进行切片、拼接、查找、替换等
# 由于bytes类型不可变，因此进行修改时需要创建一个新的bytes对象
x = b"hello"
y = x[1:3]  # 切片操作，得到"el"
z = x + b"word!" # 拼接操作
print(type(x))
print(y)
print(z)

if x[0] == ord("h"):
    print("The first elemnt is 'h'")
 """

# Python推导式
# 这是一种Python特有的特殊数据处理方式
""" # 列表推导式

# [表达式 for 变量 in 列表] 
# [out_exp_res for out_exp in input_list] 
# [表达式 for 变量 in 列表 if 条件]
# [out_exp_res for out_exp in input_list if condition]

name = ["Bob", "Tom", "alice", "Jerry", "Wendy", "Smith"]

# 这里是过滤掉长度小于等于3的字符串，并将剩下的转换为大写字母
# Upper()获取大写字母，len()返回长度
new_names = [name.upper() for name in name if len(name)>3]
print(new_names) 

# 计算30以内的可以被3整除的整数
multiples = [i for i in range(30) if i % 3 == 0]
print(multiples)
"""

""" # 字典推导式

# { key_expr: value_expr for value in collection }
# { key_expr: value_expr for value in collection if condition }

# 使用字符串及其长度创建字典
listdemo = ["Goole", "Baidu", "Tencnet"]
# 键值在一个字典里是唯一的，所以后一个覆盖了前一个
newdict1 = {len(key):key for key in listdemo}
newdict2 = {key:len(key) for key in listdemo}
print(newdict1)
print(newdict2)

dic1 = {x:x**2 for x in (2,4,6) if x > 2}
print(dic1)
print(type(dic1)) """

""" # 集合推导式
# { expression for item in Sequence }
# { expression for item in Sequence if conditional }

# 计算1，2，3的平方
setnew = {i**2 for i in (1,2,3)}
print(setnew)

# 判断不是abc的字母并输出
a = {x for x in "aabbccddxxdf" if x not in "abc"}
# 集合是无序的
print(a)
print(type(a)) """

""" # 元组推导式（生成器表达式）
# (expression for item in Sequence)
# (expression for item in Sequence if conditional)

# 以下是生成数字1到9的元组
a =  (x for x in range(1,10))
print(a)    #这里返回的是生成器对象
print(tuple(a)) # 使用 tuple() 函数，可以直接将生成器对象转换成元组 """