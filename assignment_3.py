#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#assignment 3
#Create a script that loops through a list of names, comparing the length of each name to the length of all other names in the list 
#printing out only the largest name
names_list =["bob","jimmy","max b","bernie","jordan","future hendrix"]
longest_name = ""
for i in names_list:
    if len(i) > len(longest_name):
        longest_name = i
    else:
        longest_name = longest_name
print("The longest name is " + longest_name +".")

