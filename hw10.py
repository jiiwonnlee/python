#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import pickle

filename = 'score.bin'

def input_scores():
    scores = []
    i = 1
    while True:
        n = int(input(f'#{i}? '))
        i += 1
        if n > 0:
            scores.append(n)
        if n < 0:
            break
    return scores

def get_average(lst):
    total = sum(lst)
    return total / len(lst)

def show_scores(lst):
    for n in lst:
        print(n, end=' ')
    print()

def save_scores(scores):
    with open(filename, 'wb') as file:
        pickle.dump(scores, file)

def load_scores():
    if os.path.exists(filename):
        with open(filename, 'rb') as file:
            return pickle.load(file)
    return None

# 프로그램 시작
scores = load_scores()

if scores is not None:
    print('[파일 읽기]')
else:
    print('[점수 입력]')
    scores = input_scores()
    save_scores(scores)

print('[점수 출력]\n개인점수:', end=' ')
show_scores(scores)

avg = get_average(scores)
print(f'평균: {avg:.1f}')


# In[ ]:




