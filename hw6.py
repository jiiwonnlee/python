#!/usr/bin/env python
# coding: utf-8

# In[1]:


def display_multiplication_table():
    for i in range(1, 10):
        for j in range(2, 6):
            print(f'{j} x {i} = {j * i:2d}', end='\t')
        print()
    print()
    for i in range(1, 10):
        for j in range(6, 10):
            print(f'{j} x {i} = {j * i:2d}', end='\t')
        print()

display_multiplication_table()


# In[ ]:



