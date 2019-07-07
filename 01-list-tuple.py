#列表
List1 = ['张飞','赵云','马超','吕布']
pos = 1
value = List1[pos]
print('取出列表的第%d个值，它是%s' % (pos,value))

print('输出列表中所有元素')
pos = 0
for v in List1:
    print('取出列表中第%d个值，它是%s' % (pos,v))
    pos = pos + 1

#列表更新操作
print('\n-----cutitng line-------')
newvalue = '关羽'
List1[0] = newvalue
print('输出更新后的列表中所有元素')
pos = 0
for v in List1:
    print('取出列表中的第%d 个值，它是%s' % (pos,v))
    pos = pos + 1

#-------------------
tup1 = ('刘备','曹操','孙权')
pos = 1
value = tup1[pos]
print('取出列表的第%d个值，它是%s' % (pos,value))

print('输出列表中所有元素')
pos = 0
for v in tup1:
    print('取出列表中第%d个值，它是%s' % (pos,v))
    pos = pos + 1
#-------------------
print('\n-----cutitng line-------')
import random
for i in range(1,5):
    s = random.choice(List1)
    print(s)
