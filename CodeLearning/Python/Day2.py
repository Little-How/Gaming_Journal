# Python迭代器与生成器
# 迭代器
""" 这是一个可以记住遍历的位置的对象
迭代器对象从集合的第一个元素开始访问，
直到所有元素被访问完结束，迭代器只能
往前不会往后
"""

""" # 迭代器有两个基本方法iter()和next()
listdemo1 = [1, 2, 3, 4, 5, 6]
iterdemo0 = iter(listdemo1)
iterdemo1 = iter(listdemo1)
iterdemo2 = iter(listdemo1)
print(iterdemo0)
# 将其转换为元组,列表等
print(tuple(iterdemo1))
print(set(iterdemo2))
print(next(iterdemo0))
print(next(iterdemo0))
for x in iterdemo0:
    print(x, end = " ")

import sys
listdemo2 = [1, 3, 5, 7]
iterdemo3 = iter(listdemo2)
while True:
    try:
        print(next(iterdemo3))
    except StopIteration:
        sys.exit() """

""" 面向对象复习
# 类Class：用来描述具有相同属性和方法的对象的集合。对象是类的实例
# 方法：类中定义的函数
# 类变量： 类变量在整个是实例化的对象中是公用的。类变量通常不作为实例变量使用
# 数据成员： 类变量或者实例用于处理类以及实例对象的相关数据
# 方法重写：override，父类的方法不能满足子类的需求，就可以进行改写
# 局部变量：定义在方法中的变量，只用于当前实例的类
# 实例变量：在类的声明中，属性是用变量来表示的，这种变量就被称为实例变量，用Self修饰
# 继承：派生类derived class继承基类base class的字段和方法。
# 继承也允许把一个派生类的对象作为一个基类对象对待
# 实例化：创建一个类的实例，类的具体对象
# 对象：通过类定义的数据结构实例。对象包括两个数据成员（类变量和实例变量）和方法 """