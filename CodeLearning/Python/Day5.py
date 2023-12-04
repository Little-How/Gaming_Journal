# 序列是Python中最基本的数据结构
# 序列的每个值都有对应的位置值，即索引
# Python中有6个序列的内置类型，但最常见啊的是列表和元组

# 列表：可以操作的是索引、切片、加、乘、检查成员
# 列表的索引值从开头起是0开始，从尾开始是从-1开始
list = ['googlr', 'tencent', 'runoob']
# append()在列表后添加列表项
# 队列是一种先进先出的数据结构，可以使用列表来实现队列的基本功能
list.append('baidu')
print(list)

queue = []
# 添加元素到队列末尾
queue.append('A')
queue.append('B')
queue.append('C')
print(queue)
print('The third one is '+ queue[2]+ ", right!")

# 从队列的开头删除元素
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))
print(queue)
# Python列表截取与拼接