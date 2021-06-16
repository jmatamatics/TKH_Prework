#!/usr/bin/env python
# coding: utf-8

# In[1]:


#assignment 5
#Create a functione that takes the below list of names and seperates them into lists, 
#one of the names with an even number of letters and one with an odd numer of letters
names_list =["bob","jimmy","max b","bernie","jordan","future hendrix"]
even = []
odd = []
def lcount(x):
    for i in x:
        if len(i)%2==0:
            even.append(i)
        else:
            odd.append(i)

lcount(names_list)           

#take the first letter of each of the names in the even list andmake it the letter'b'
#take the last letter in each of the names in the odd list and make them a 'c'
odd_c =[]
even_b =[]
for i in range(len(odd)):
    odd_c.append(odd[i][:-1] +"c")   
for i in range(len(even)):
    even_b.append("b"+ even[i][1:])
#print both lists and return the even one to a variable named even_list and print it again
print(odd_c)
print(even_b)
evens_list = even_b
print(evens_list)


# In[ ]:




