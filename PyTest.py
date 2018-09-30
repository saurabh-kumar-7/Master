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

my_detail = { 'Name' : { 'First' : 'Saurabh', 'Last' : 'Kumar' } , 'Age' : 30 , 'Address' : { 'Addr1' : '7611 Knox Ave S' , 'Addr2' : 'Apt 318' , 'City' : 'Richfield' , 'State':'MN' } }
print ("My details are " + str(my_detail) )

my_detail['Address']['Country'] = 'USA'

print(my_detail)

print(5/2)
print(5//-2)