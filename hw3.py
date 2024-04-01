#!/usr/bin/env python
# coding: utf-8

# In[2]:


def get_fixed_price(discounted_price):
    return int(discounted_price/(1-rate/100))
rate=int(input('할인율은?'))
a_price=int(input('A 상품의 할인된 가격은?'))
a_fixed_price=get_fixed_price(a_price)
print('A 상품의 정가는',a_fixed_price,'원')

b_price=a_price=int(input('B 상품의 할인된 가격은?'))
b_fixed_price=get_fixed_price(b_price)
print('B 상품의 정가는',b_fixed_price,'원')


# In[ ]:




