#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#assignment 2
#create a loop that compares the list of numbers provided for the number 25 
#print over if it is over and under if it is under 
over_under_list = [1,45,32,21,5,15,43,93]
num = 25

for i in over_under_list:
    if i > num:
        print (str(i) +" over")
    else:
        print (str(i) +" under")

