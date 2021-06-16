#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#assignment 4
#Refactor Assignment 3 as a function that takes a list of names and returns the largest one

names_list =["bob","jimmy","max b","bernie","jordan","future hendrix"]
#longest_name =""
def lname(x):
    longest_name = ""
    for i in names_list:
        if len(i) > len(longest_name):
            longest_name = i
    return longest_name

lname(names_list)
#Then save it to the variable big_name and print it to the console. 
big_name = lname(names_list)
print("The longest name is " + big_name +".")
        
        

