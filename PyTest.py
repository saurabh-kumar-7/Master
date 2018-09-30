import os
import sysconfig
import xmlrpc 
import matplotlib.pyplot as plt
import numpy
from textwrap import indent


print ("This is my first file")
#plt.plot([1,2,3,4])
#plt.ylabel('some numbers')
#plt.show()

my_detail = { 'Name' : { 'First' : 'Author', 'Last' : 'Life' } , 'Age' : 30 , 'Address' : { 'Addr1' : '8888 Abc Ave S' , 'Addr2' : 'Apt 77' , 'City' : 'Abcd' , 'State':'Ab' } }
print ("My details are " + str(my_detail) )

my_detail['Address']['Country'] = 'USA'

print(my_detail)

print(5/2)
print(5//-2)