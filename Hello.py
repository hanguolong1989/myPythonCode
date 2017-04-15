
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def func(self,name='world'):
    print('Hello,%s' % name)

Hello = type('Hello',(object,),dict(hello = func))