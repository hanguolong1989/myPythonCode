#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'koredragon'

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



# func = now
#
# func()
#
# print(now.__name__)

#
# def log(func):
#     def wrapper(*args,**kw):
#         print('call %s():' % func.__name__)
#         return func(*args,**kw)
#     return wrapper
#
#
# @log
# def now():
#     print('2017-4-14')
#
#
# now()



# def int2(x,base=2):
#     return int(x,base)
#
#
#
#
# t = int2('1010101')
# print(t)


# import functools
#
# int2 = functools.partial(int,base = 2)
#
# print(int2('100000',base = 12))

# from functools import partial
#
# def mod(n,m):
#     return n % m
#
# mod_by_100 = partial(mod,100)
#
# print(mod_by_100(7))

#
#
# def _private_1 (name):
#     return 'Hello,%s'  % name
#
# def _private_2(name):
#     return 'Hi ,%s' % name
#
# def greeting(name):
#     if len(name) > 6:
#         return _private_1(name)
#     else:
#         return _private_2(name)
#
#
#
# name = greeting('kore')
#
# print(name)

# from PIL import Image

# im = Image.open('/Users/koreadragon/Desktop/logo.png')
#
# im.thumbnail((200,100))
#
# im.save('/Users/koreadragon/Desktop/kora.png')

# import sys

# print(sys.path)

# std1 = {'name':'Michael','score':98}
# std2 = {'name':'Bob','score':81}
#
# def print_score(std):
#     print('%s: %s' % (std['name'], std['score']))
#
#
# print_score(std1)


# class Student(object):
#
#
#     def __init__(self,name,score):
#         self.__name = name
#         self.score = score
#
#     def print_score(self):
#          print('%s : %s' % (self.__name,self.score))
#
#     def get_grade(self):
#         if self.score >= 90:
#             return 'A'
#         elif self.score >= 60:
#             return 'B'
#         else:
#             return 'C'
#
#
#
# han = Student('Bar',98)
# kore = Student('Lisa',89)

# han.print_score()
# kore.print_score()
#
# class High_student(Student):
#
#     def to __init__(self,gender):
#         self.gender = gender
#
#     def make_love():
#         print('Make love for 3 minutes')
#
#
# Baoji = High_student('')


# print(han.get_grade())




# han.score = 43
#
# han.name = 'New_han'
#
# han.print_score()


# get_name = han.name
# print('getN %s'% get_name)


# class Animal(object):
#     def run(self):
#         print('Animal is running ...')
#
# big_animal = Animal()
#
# big_animal.run()
#
#
# class Dog(Animal):
#     def run(self):
#         print('A dog is running ')
#
#
# teddy = Dog()
# teddy.run()
#
# bool  =isinstance(teddy,Animal)
#
# # print(bool)
#
# # fun/cs = dir('ABC')
#
# # print('greafgre'.center(2))
#
#
# teddy.__setattr__('y',19)
#
# print(hasattr(teddy,'y'))
#
# f = getattr(teddy,'y',404)
# print(f)
#



# class Student(object):
#     # name = 'Student'
#     def __init__(self,name):
#         self.name = name
#
#
# s = Student('Bob')
# s.score = 90
# s.name = 'NewBob'
# print(s.score)
#
# print(s.name)


# print(Student.name)

# del s.name
# print(s.name)


# def set_age(self,age):
#     self.age = age
#
# from types import MethodType
#
# Student.set_age = set_age
#
# s.age = 5
#
# print(s.age)
#
# s2 = Student('St2')
#
# s2.set_age(432)
#
# print(s2.age)

# class Student(object):
#     @property
#     def score(self):
#         print('score is %s' % self._score)
#         return self._score
#
#     @score.setter
#     def score(self, value):
#         if not isinstance(value, int):
#             raise ValueError('score must be an integer!')
#         if value < 0 or value > 100:
#             raise ValueError('score must between 0 ~ 100!')
#         self._score = value
#
#
# s = Student()
#
# s.score = 43
# print(s.score)

# class Student(object):
#     def __init__(self,name):
#         self.name = name
#
#     def __str__(self):
#         return 'Student object (name:%s)' % self.name
#
#
# stu = Student('Micah')
#
# print(stu)

#枚举

# from enum import Enum,unique
# # Month = Enum('TwelveMonths', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
# #
# # for name,member in Month.__members__.items():
# #     print(name,'=>',member,',',member.value)
#
#
# @unique
# class Weekday(Enum):
#     Sun = 0
#     Mon = 1
#     Tue = 2
#     Wed = 3
#     Thu = 4
#     Fri = 5
#     Sat = 6
#
# # for name,member in Weekday.__members__.items():
# #     print(name,'=>',member,',',member.value)
#
# print(Weekday['Tue'])



# from Hello import Hello
#
# h = Hello()
#
# h.hello()

# def choose_class(name):
#     if name == 'foo':
#         class Foo(object):
#             pass
#         return Foo
#     else:
#         class Bar(object):
#             pass
#         return Bar
#
# MyClass = choose_class('foo')
# # print(MyClass)
#
#
#
# # print (type(ObjectCreator))
#
#
# MyShinyClass = type('MyShinyClass',(),{})
#
#
# # print(MyShinyClass)
#
# Foo = type('Foo',(),{'name':'Kid'})
#
# fooo = Foo()
#
# # print(fooo.name)
#
#
# FooBar = type("FooBar",(Foo,),{'age':12})
#
# smallTalk = FooBar()
#
# print(smallTalk.age,smallTalk.name)
# age = 23
# print(age.__class__.__class__)


# def upper_attr(future_class_name,future_class_parents,future_class_attr):
#     attrs = ((name,value) for name,value in future_class_attr.items() if not name.startswith('__'))
#     uppercase_attr = dict((name.upper() ,value) for name,value in attrs)
#
#     return type(future_class_name,future_class_parents,uppercase_attr)
#
#
# __metaclass__ = upper_attr
# class Foo():
#     bar = 'bip'
#
#
# print(hasattr(Foo,'bar'))
# print(hasattr(Foo,'BAR'))
#
# f = Foo()
# print(f.BAR)


#
# try:
#     print('try...')
#     r = 10 / 2
#     print('result:', r)
# except ZeroDivisionError as e:
#     print('except:', e)
# finally:
#     print('finally...')
# print('END')
#
# try:
#     print('try...')
#     r = 10 / int('0')
#     print('result:', r)
# except ValueError as e:
#     print('ValueError:', e)
# except ZeroDivisionError as e:
#     print('ZeroDivisionError:', e)
# finally:
#     print('finally...')
# print('END')


# file = open('/Users/koreadragon/Desktop/log.txt','r')


# with open('/Users/koreadragon/Desktop/logo.png','rb') as fie:
#     a = 1
#     for line in fie.readlines():
#         if a < 10:
#             print(line.strip())
#             a = a + 1
#
#         else:
#             print('不敢打印啦')
#             break


# f = open('/Users/koreadragon/Desktop/gbk.txt','w',encoding='gbk')
# f.write('Hello,world')
# f.close()
#
# from  io import StringIO
#
# f = StringIO('Hello!\nHi!\nGoodbye!')
#
# while True:
#     s = f.readline()
#     if s == '':
#         break
#     print(s.strip())



import os

# print(os.uname())

# print([x for x in os.listdir('.') if os.path.isdir(x)])



# import pickle
#
# d = dict(name='Bob',age = 20,score = 84)
# print(pickle.dumps(d))
#
# f = open('/Users/koreadragon/Desktop/pp.txt','wb')
# pickle.dump(d,f)
# f.close()
# print(d)


# import json
# #
# # d = dict(name = 'Bob',age = 20,score = 88)
# # print(json.dumps(d))
#
#
# json_str = '{"age": 20, "score": 88, "name": "Bob"}'
#
#
# print(json.loads(json_str))

#
#
# import os
#
# print('process (%s) start...' % os.getpid())
#
#
# pid = os.fork()
#
# if pid == 0:
#     print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
# else:
#     print('I (%s) just created a child process (%s).' % (os.getpid(), pid))



from multiprocessing import Pool

import os,time,random


#子进程要执行的代码

# def run_proc(name):
#     print('Run child process %s (%s)...' % (name, os.getpid()))
#
# if __name__=='__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Process(target=run_proc, args=('test',))
#     print('Child process will start.')
#     p.start()
#     p.join()
#     print('Child process end.')


# def long_time_task(name):
#     print('Run task %s (%s)...' % (name, os.getpid()))
#     start = time.time()
#     time.sleep(random.random() * 3)
#     end = time.time()
#     print('Task %s runs %0.2f seconds.' % (name, (end - start)))
#
# if __name__=='__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Pool(4)
#     for i in range(5):
#         p.apply_async(long_time_task, args=(i,))
#     print('Waiting for all subprocesses done...')
#     p.close()
#     p.join()
#     print('All subprocesses done.')

# import subprocess
#
# print('$ nslookup')
# p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
# print(output.decode('utf-8'))
# print('Exit code:', p.returncode)
# from multiprocessing import Process, Queue
# import os, time, random
#
# # 写数据进程执行的代码:
# def write(q):
#     print('Process to write: %s' % os.getpid())
#     for value in ['A', 'B', 'C']:
#         print('Put %s to queue...' % value)
#         q.put(value)
#         time.sleep(random.random())
#
# # 读数据进程执行的代码:
# def read(q):
#     print('Process to read: %s' % os.getpid())
#     while True:
#         value = q.get(True)
#         print('Get %s from queue.' % value)
#
# if __name__=='__main__':
#     # 父进程创建Queue，并传给各个子进程：
#     q = Queue()
#     pw = Process(target=write, args=(q,))
#     pr = Process(target=read, args=(q,))
#     # 启动子进程pw，写入:
#     pw.start()
#     # 启动子进程pr，读取:
#     pr.start()
#     # 等待pw结束:
#     pw.join()
#     # pr进程里是死循环，无法等待其结束，只能强行终止:
#     pr.terminate()



import re

#
# s = r'ABC/-001'
#
#
#
# test = 'ABC-001'
# if re.match(s, test):
#     print('ok')
# else:
#     print('failed')

# print('a b  few   c'.split(' '))

# from  datetime import  datetime
#
# now = datetime.now()
# print(now)
#
#
# da = datetime.now()
# stamp = da.timestamp()
#
# originTime = datetime.fromtimestamp(stamp)
#
# utcTime = datetime.utcfromtimestamp(stamp)
# print(originTime,'\n',utcTime)
#
# print(now.strftime('%a, %b %d %H:%M'))


from xml.parsers.expat import ParserCreate

class DefaultSaxHandler(object):
    def start_element(self, name, attrs):
        print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))

    def end_element(self, name):
        print('sax:end_element: %s' % name)

    def char_data(self, text):
        print('sax:char_data: %s' % text)




xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''

handler = DefaultSaxHandler()
parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
parser.Parse(xml)







