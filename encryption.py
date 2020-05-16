#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import binascii
import math


# In[2]:


string = "qwerty"
bin = ''.join(format(ord(x), 'b').zfill(8) for x in string)
len(bin)


# In[3]:


m = 5
stop = int(len(bin)/m)
lst = []
j = 0
for i in range(stop+1):
    if j+m < len(bin):
        lst.append(bin[j:j+m])
        j = j+m
    else:
        lst.append(bin[j:])
lst


# In[4]:


n = 2


# In[5]:


for i in range(len(lst)-1):
    lst[i] = '00' + lst[i]
lst[-1] = '0000' + lst[-1]


# In[6]:


lst


# In[7]:


for i in range(len(lst)): 
    con = str(random.randrange(0,2))
    lst[i] = lst[i][:n] + con + lst[i][n:]
lst


# In[8]:


def str_to_bin(a):
    sum = 0
    for i in range(len(a)):
        sum += int(a[-1-i]) * math.pow(2, i)
    return int(sum)


# In[9]:


for i in range(len(lst)):
    lst[i] = str_to_bin(lst[i])
lst


# In[10]:


lst = [chr(x) for x in lst]


# In[11]:


lst


# In[12]:


out = [format(ord(x), 'b').zfill(8) for x in lst]
out


# In[13]:


for i in range(len(out)): 
    out[i] = out[i][:n] + out[i][n+1:]
out


# In[14]:


for i in range(len(out)):
    out[i] = out[i][len(out[i])-m:]
out


# In[15]:


opstr = ''
for i in out: 
    opstr = opstr + i
opstr


# In[16]:


decrypt = []
j = 0
while j<len(opstr):
    decrypt.append(opstr[j:j+8])
    j = j+8
    if(len(decrypt[-1])<8):
        decrypt.remove(decrypt[-1])
decrypt
for i in range(len(decrypt)):
    decrypt[i] = str_to_bin(decrypt[i])
decrypt
output = [chr(x) for x in decrypt]
output


# In[ ]:




