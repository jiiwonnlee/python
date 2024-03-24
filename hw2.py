#!/usr/bin/env python
# coding: utf-8

# In[4]:


def exchange(sum):
    m_500=sum//500
    sum%=500
    m_100=sum//100
    sum%=100
    m_50=sum//50
    sum%=50
    m_10=sum//10
    print('500원 동전의 개수:',m_500)
    print('100원 동전의 개수:',m_100)
    print('50원 동전의 개수:',m_50)
    print('10원 동전의 개수:',m_10)
def get_integer(prompt):
    res=int(input(prompt))
    return res
n=get_integer('동전으로 교환하고자 하는 금액은?')
exchange(n)


# In[ ]:




