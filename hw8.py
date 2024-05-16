#!/usr/bin/env python
# coding: utf-8

# In[3]:


shopping_bag={}
print('[구입]')
while True:
    item=input('상품명?')
    
    if item=='':
        break
    else:
        num=input('수량은?')
        shopping_bag[item]=num
        print(f'장바구니에 {item} {num}개가 담겼습니다.\n')
print('\n>>> 장바구니 보기:',shopping_bag)

print('\n[검색]')
p=input('장바구니에서 확인하고자 하는 상품은?')
if p not in shopping_bag:
    print(f'장바구니에 {p}은(는) 없습니다.')
else:
    u_num=int(shopping_bag[p])
    print(f'{p}은(는) {u_num}개 담겨 있습니다.')


# In[ ]:




