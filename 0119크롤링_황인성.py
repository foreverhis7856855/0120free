#!/usr/bin/env python
# coding: utf-8

# In[23]:


import pandas as pd
import numpy as np
import time

import re

from selenium import webdriver


# In[24]:


# 크롬창 띄우기
driver = webdriver.Chrome(r"C:\Users\forev\Desktop\SBA_re\chromedriver.exe")
driver.get("https://ratebeer.com/")
time.sleep(2)


# In[25]:


query_text = "cass"


# In[26]:


# 검색창에 검색어 입력 후 검색
element = driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div/div[2]/div/input')

element.send_keys(query_text)
time.sleep(2)


# In[28]:


driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div/div[2]/div[2]/a[1]/div/div[1]/img').click()


# In[30]:


beername = driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div/div/div/div[2]/div[1]/div/div[2]/div[1]/div/div[1]/div/div').text


# In[37]:


beername = driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div/div/div/div[2]/div[1]/div/div[2]/div[1]/div/div[1]/div/div')


# In[42]:


tmp = []


# In[41]:


beer = driver.find_elements_by_css_selector('.px-4.fj-s.f-wrap')
beer[0].text


# In[43]:


for i in range(len(beer)):
    tmp.append(beer[i].text)


# In[44]:


tmp


# In[31]:


beername


# In[34]:


beer_list = [beername]
beer_list


# In[35]:


tmp = pd.DataFrame(data=beer_list)
tmp


# In[36]:


tmp.to_excel('beer0119.xlsx')


# In[ ]:




