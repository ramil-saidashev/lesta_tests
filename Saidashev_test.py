# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


#Задание 1
def iseven(x):
        return x & 2 and True or False
    
#Преимущество данного варианта в скорости, тогда как заданный вами по умолчанию 
#проще понять

#Задание 2
#1
# Преимуществом приведенного ниже класса является простота использования
# и оптимальная скорость работы за счет numpy
# недостаток - очень громоздок
import numpy as np

class RingBuffer(object):
    def __init__(self, size, padding=None):
        self.size = size
        self.padding = size if padding is None else padding
        self.buffer = np.zeros(self.size+self.padding)
        self.counter = 0

    def append(self, data):
#время работы данной функции составляет О(n)
        data = data[-self.padding:]
        n = len(data)
        if self.remaining < n: self.compact()
        self.buffer[self.counter+self.size:][:n] = data
        self.counter += n

    @property
    def remaining(self):
        return self.padding-self.counter
    @property
    def view(self):
# время работы данной функции 0(1)
        return self.buffer[self.counter:][:self.size]
    def compact(self):
        
        print('compacting')
        self.buffer[:self.size] = self.view
        self.counter = 0

rb = RingBuffer(10)
for i in range(4):
    rb.append([1,2,3])
    print(rb.view)

rb.append(np.arange(15))
print(rb.view)

#2
#быстро работает, легко читается, прост в исполнении
#недостаток - нужно вручную задавать макимальную длину

import collections
class deque(object):
    def __init__(self, length):
        self.deque = collections.deque(maxlen = length)
        
    def append(self, num):
        self.deque.append(num)
        
    def extend(self, array):
        self.deque.extend(array)
    
    def get(self):
        print(self.deque)
        
        
        
d = deque(8)
d.extend([12,3,5,68,9,10,24,46])
d.append(93)
d.get()


#Задание 3
# Приведенная ниже сортировка является классическим примером быстрой сортировки
# c элиминацией хвостовой рекруссии, среднее время работы - nlogn
def partition(a):
    lss, eql, grt = [], [], []
    pvt = (a[0] + a[len(a)//2] + a[-1])//3
    for x in a:
        if x < pvt:
            lss.append(x)
        elif x == pvt:
            eql.append(x)
        else:
            grt.append(x)
    return lss, eql, grt

def quicksort(a):
    while len(a) > 1:
        lss, eql, grt = partition(a)
        if len(lss) < len(grt):
            first = quicksort(lss)
            return first + eql + quicksort(grt)
        elif len(lss) > len(grt):
            first = quicksort(grt)
            return quicksort(lss) + eql + first
        else:
            return quicksort(lss) + eql + quicksort(grt)
    return a

