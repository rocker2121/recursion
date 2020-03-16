#!/usr/bin/env python
# coding: utf-8

# In[5]:


# sum of digits
def sum_rec (number):
    if number/10<1:
        return number%10
    else:
        return number%10 + int(sum_rec(number/10))


# In[ ]:


#reversing stiring


# In[13]:


def rev_str(s):
    if len(s)==1:
        return s
    else:
        return s[-1]+rev_str(s[:-1])


# In[ ]:


#fibonacci problem


# In[34]:


d={}
def fib(n):
 
    if n<=1:
        return 1
    else:
        if n in d.keys():
            
            return d[n]
        else:
            d[n]=fib(n-1)+fib(n-2)
            return d[n]
        
        
        
        
        


# In[ ]:


#coin change problem


# In[46]:



def getmin (target,coin):
    if target==0:
        return 0
    else:
        n=int(target/coin[-1])
        return n + getmin(target-n*coin[-1],coin[:-1])
    


# In[ ]:




