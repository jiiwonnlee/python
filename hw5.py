#!/usr/bin/env python
# coding: utf-8

# In[11]:


def read_single_digit(n):
    korean_numbers=['영 ','일 ','이 ','삼 ','사 ','오 ','육 ','칠 ','팔 ','구 ']
    return korean_numbers[n]
def read_number(num):
    num_100=read_single_digit(num//100)
    num_10=read_single_digit((num%100)//10)
    num_1=read_single_digit(num%10)
    return num_100 + num_10 + num_1

number=int(input('세 자리 정수 입력:'))
result=read_number(number)
print(result)


# In[ ]:




