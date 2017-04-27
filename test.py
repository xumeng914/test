#coding:utf-8
#from numpy import mat
import numpy
ss=numpy.mat([1,2,7])
print(ss*ss.T)

a = arange(15).reshape(3, 5)
type(a)

b = array([6, 7, 8])
type(b)

 A = array( [[1,1],[0,1]] )
B = array( [[2,0],[3,4]] )
A*B
dot(A,B)


a = ones((2,3), dtype=int)
b = random.random((2,3))
a*=3
b += a


b = arange(12).reshape(3,4)
b.sum(axis=0)
b.min(axis=1)


a= arange(10)**3
a
a[2]
8
a[2:5]
array([ 8, 27, 64])
a[:6:2] = -1000    # equivalent to a[0:6:2] = -1000; from start to position 6, exclusive, set every 2nd element to -1000
a
array([-1000,     1, -1000,    27, -1000,   125,   216,   343,   512,   729])
a[ : :-1]                                 # reversed a
a

for i in a:
    print(i**(1/3.))



def f(x,y):
    return 10*x+y
b = fromfunction(f,(5,4),dtype=int)
b[0:5, 1]
b[ : ,1]
b[1:3, : ]
###########################
import pandas
s=pandas.Series([1,3,5,numpy.nan,6,8])
date=pandas.date_range('20130101',periods=6)
df=pandas.DataFrame(numpy.random.randn(6,4),index=date,columns=list("ABCD"))
df.head()
df.tail()
df.describe()
df.T
df.T.describe()
df.sort(columns='A')
df.A
df.iloc[1:3,1:2]
df.loc[date[0],['A','B']]
