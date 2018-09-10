#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 22:35:29 2018

@author: juank
"""

x = 2 + 2
print x

x = -1      # int
y = 3.14    # float
z = 1 + 2j  # complex

print type(x)
print type(y)
print type(z)

a = 21
b = a/6

print b

print type(b)

b = a/6.0
print b
print type(b)

x = complex(-1)
print x

y = float("3.14")
print y

z = int(-1.0)
print z

b = True
print type(b)

a = "Hello, World!"
print a[1] 

print a[0:5], " everybody"

s = a[0:5] + " everybody"
print s

s = "%s everybody... and look, %d is an integer, %f is a float, and %.2f is a prettier float."% (a[0:5], 5, 5.67, 1.6180)
print s

s = "   Hello, World!  "
print s
s = s.strip()
print s
print s.lower()
print s.upper()
print s.replace("H", "J")
print s.split(",")

print "Who are you?"
name = input()
print "Hi there, " + name + "!"

x = 3.14
y = 1.62

print x+y 

print x-y

print x*y

print x/y

print x%y #Modulus

print x**y #Exponentiation

x += 3
print x

x -= 3
print x

x *= 3
print x

x /= 3
print x

x **= 3
print x

x %= 3
print x

x = 3.14
y = 1.62

print x == y
print x != y
print x > y
print x < y
print x >= y
print x <= y

x = 3.14
y = 1.62

print x<5 and y<10
print x<5 or y>4
print not(x<5 and y<10)

list1 = [5, 12, 13, 14]
print list1

list2 = ['red', 'blue', 'green']
print list2

list3 = [1, 'red', 5.2]
print list3

list3 = [1, 'red', 5.2]
list3[0] = 24

print list3
print len(list3)

thislist = [] #empty list

thislist.append("apple")
print thislist

thislist.insert(1, "cherry")
print thislist

item = thislist.pop()
print thislist
print item

otherlist = ["banana", "orange"]
thislist.extend(otherlist)
print thislist

print thislist.index("banana")

thistuple = ("apple", "banana", "cherry")
print(thistuple)

print thistuple + ("orange", "grapes") 
print thistuple*3

s = "hey there"
print s[0]
print s[-1]
print s[1:3]
print s[5:]
print s[:-3]

x = 3.14
y = 1.62

if x > y: 
  print("x is greater than y")
  
x = 3.14
y = 4.62

if x > y: 
  print("x is greater than y")
else:
  print("y is greater or equal than x")
  
  
x = 3.14
y = 10.62

if x > y: 
  print("x is greater than y")
elif x < y:
  print("y is greater than x")
else:
  print("y and x are equal")

i = 1
while i < 6:
  print(i)
  i += 1
  
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1 
  
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

for x in range(6):
  print(x)
  
import math
print dir(math)

help(math.sin)

print math.sin(math.pi)

from math import pi, e

print e
print pi


import numpy as np # No error means it's alright

print np.arange(5)

a = np.array([2, 3, 4])
print a
print type(a)
print a.dtype
b = np.array([1.2, 3.5, 4])
print b.dtype

b = np.array([(1.5,2,3), (4,5,6)])
print b
print b.shape

zero_array = np.zeros( (3,4) ) # shape
print zero_array

one_array = np.ones( (2,3,4), dtype=np.int8 ) # dtype can also be specified
print one_array

empty_array = np.empty( (2,3) ) # uninitialized, output may vary
print empty_array

print np.arange(0, 2, 0.3) # from, to, step
print np.linspace(0, 2, 9) # from, to, out length

b = np.arange(24)
b = b.reshape(2,3,4) # 3D array

print b

a = np.array([20, 30, 40, 50])
b = np.arange(4)
print b

c = a - b
print c

print b**2

print a < 35

a = np.array([2, 7.1, 4.2, 5.4, 8.3, 9.1]).reshape(2,3)
b = np.arange(9).reshape(3,3)
c = np.arange(3)

print a*c
print a.dot(c) 
print np.dot(a,b) # another way of computing matrix product

a = np.array([2, 7.1, 4.2, 5.4, 8.3, 9.1]).reshape(2,3)

print a.sum()
print a.max()
print a.var()

a = np.array([2, 7.1, 4.2, 5.4, 8.3, 9.1]).reshape(2,3)

print a
print a.sum(axis=0) 
print a.sum(axis=1) 
print a.cumsum(axis=0)

a = np.arange(10)**3
print a

print a[2:5] 
print a[:6:2] # equiv. to a[0:6:2] (from start to pos. 6, exclusive, every 2nd element)
print a[3: :2] # equiv. a[3:10:2]
print a[ : :-1] # reversed a


b = np.random.random((3,4))
print b

print b[2,3]
print b[:2, 1]
print b[:, 0]
print b[:,(0,2)]

print b[-1] # equiv. b[-1,:] the last row

b = np.random.random((3,4))

for row in b:
  print row


for element in b.flat:
  print element

a = np.round(np.random.random((3,4)), 2)
print a

print a.shape

print a.T # transpose matrix

print a.reshape(6,2)

print a.ravel() # returns the array, flattened

print a.reshape(4, -1) # dim 2 is automatically calculated.

a = np.round(np.random.random((3,4)), 2)
print a

a.resize((2,6))
print a

a = np.round(np.random.random((2,2)), 2)
b = np.round(np.random.random((2,2)), 2)

print a
print b

print np.vstack((a,b))
print np.hstack((a,b))
print np.concatenate((a,b), axis=0)
print np.concatenate((a,b), axis=1)

a = np.round(np.random.random((2,12)), 2)

print a
print np.hsplit(a, 3) # split into 3 
print np.hsplit(a, (3,8)) # split ater 3rd and 8th column

def times(x, y):
  return x*y

print times(2,3)