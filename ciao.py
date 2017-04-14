# print('hello')
#
# print("你好，世界")

# name = input('please enter your name')
# print('hello,',name)

# classmates =('Michael','Bob','Tracy')
# print(classmates[-1])

# t = (1,2)
# print(t)

# t =(t) (1,)
#
# print

# t = ('a','b',['A','B'])
#
# t[2][0] = 'X'
#
# t[2][1] = 'Y'
#
# print(t)


# age = 3
# if age >= 18:
#    print('your age is ',age)
#    print('adult')
# elif age >= 6:
#     print('your age is ',age)
#     print('teenager')
# else:
#     print('kid')



# s = input('birth: ')
#
# birth = int(s)
# if birth < 2000:
#     print('00前')
# else:
#     print('00后')


# s = list(range(101))
#
# sum = 0
# for x in s:
#     sum = sum + x
#
# print(sum)


# d = {'Michael':95,'Bob':75,'Tracy':85}
#
#
# d['Adam'] = 43
#
# d['Adam'] = 34
#
# existAKid = d.get('Michael')
#
# if existAKid:
#     print('Michael\'s score is %d' % d['Michael'] )
#
# else:
#     print('Michael is not in the class')

# abs(100)
# print(abs(-100))
#
# a = abs
# print(a(-1))

# print(hex(100))

#求绝对值函数
# def my_abs(x):
#     if x > 0 :
#         return x
#     else:
#         return -x
#
# # print(my_abs(-100))
#
# #求平方函数
# def power(x):
#     return x*x
#
#
# print(power(73643643))

# def powerNew(x,n = 2):
#     s = 1
#     while n>0:
#         n = n-1
#         s = s * x
#     return s
#
# print(powerNew(5,3))
#
# def fact(n):
#     if n == 1:
#         return 1
#     return n * fact(n-1)
#
# print(fact(9))

#
# L = []
#
# n = 1
#
# while n <= 99:
#     L.append(n)
#     n = n + 2
#
#
# print(L)
#
# r = L[1:5]
#
# print(r)


# L = list(range(100))
# print(L)
#
# print(L[::5])

# dic = {'a':1,'b':2,'c':3}
#
# # for key,value in dic.items():
# #     print(key,value)
#
# for ch in 'ABC':
#     print(ch)


# from collections import Iterable
#
# s = isinstance('avx',Iterable)
#
# print(s)
#
#
# for i,value in enumerate(['A','B','C']):
#
#     print(i,value)
#
#
# L = [x * x for x in range(1,11)]
#
# print(L)
#
# # import os#导入模块
# #
# # print([d for d in os.listdir('.')])
#
#
# M = ['Hello','World','IBM','Apple']
#
# dd =  [s.lower() for s in M]
#
# print(dd)






# g = (x * x for x in range(10))
#
# for n in g:
#     print(n)
#
#
# def fib(max):
#     n,a,b = 0,0,1
#     while n < max:
#         print(b)
#         a,b = b,a + b
#         n = n + 1
#
# fib(12)




# f = abs
#
# re = f(-20)
# print(re)


# def add(x, y, f):
#     s = f(x) + f(y)
#     print(s)
# add(3,-3 ,abs)

# def f(x):
#     return x * x
#
# r = map(f,[1,2,3,4,5,6,7,8,9])
# a = list(r)
#
# print(a)
#
# b = list(map(str,[1,2,3,4,5,6,7,8,9]))
# print(b)

# from functools import reduce
#
# def fn(x,y):
#
#     return x * 10 + y
#
# # a = reduce(fn,[1,3,5,7,9])
# #
# # print(a)
#
# def char2num(s):
#     return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
#
# d = reduce(fn,map(char2num,'125325'))
#
# print(d)

#filter

# def is_odd(n):
#     return n % 2 == 1
#
#
# f = list(filter(is_odd,[1,2,3,4,5,6,8,9]))
#
#
# print(f)

# sort = sorted([4234,-43,-4,4,-43])
#
# print(sort)
#
# fo = sorted([35,5,-4,43,-5],key=abs)
#
# print(fo)

#sort
# sortByLetter = sorted(['bob', 'about', 'Zoo', 'Credit'],key = str.lower,reverse = True)
#
# print(sortByLetter)






# def lazy_sum(*args):
#     def calc_sum():
#         ax = 0
#         for n in args:
#             ax = ax + n
#         return ax
#     return calc_sum
# # def lazy_sum(*args):
# #     def sum():
# #         ax = 0
# #         for n in args:
# #             ax = ax + n
# #         return ax
# #     return sum
#
# f = lazy_sum(1,3,5,7,9)
# # print(f)
#
# re = f()
# print(re)

# block = lambda x : x * x
# f =  list(map(block,[1,2,3,4,5,6,7,8,9]))
# print(f)

# def build (x,y):
#     return lambda : x * x + y * y
#
# rf = build(3,5)
# print(rf())


def now():
    print('2017-4-14')


func = now

func()

























































































































































