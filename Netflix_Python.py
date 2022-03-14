#!/usr/bin/env python
# coding: utf-8

# In[8]:


#Import Libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import os


# In[11]:


files = os.listdir('C:\\Users\\fyevenes\\OneDrive - ARCHER Systems LLC\\Documents\\Python Scripts\\Fun Projects\\Netflix data')
print(files)


# In[12]:


df = pd.read_csv('netflix_titles.csv')


# In[13]:


#Quick look 
df.head()


# In[14]:


df.shape


# In[15]:


df.columns


# In[16]:


#Lets calculate the missing data / in terms of percentage looking at the whole dataframe
for i in df.columns:
    null_rate = df[i].isna().sum()/len(df)*100
    if null_rate >0:
        print("{} --missing percentage: {}%".format(i,round(null_rate,2)))


# In[17]:


#Lets replace the missing data for 'No data'
df['country'] = df['country'].fillna(df['country'].mode()[0])
df['cast'].replace(np.nan,'No data', inplace =True )
df['director'].replace(np.nan,'No data', inplace =True )
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)


# In[18]:


#Lets double check the missing data in every column
for i in df.columns:
    null_rate = df[i].isna().sum()/len(df)*100
    if null_rate >0:
        print("{} --missing percentage: {}%".format(i,round(null_rate,2)))
    if null_rate ==0:
        print("{} --Theres no missing data compadre".format(i,round(null_rate,2)))


# In[19]:


#lets separate the data column into Month / month name / year
df['date_added'] = pd.to_datetime(df['date_added'])
df['month_added'] = df['date_added'].dt.month
#df['month_name_added'] = df['month_added'].dt.month_name().str.slice(stop=3)
#df['month'] = df.index.month_added()
#df['year_added'] = df['date_added'].dt.year()


# In[20]:


#lets get the year
df['year'] = pd.DatetimeIndex(df['date_added']).year


# In[21]:


df.dtypes


# In[22]:


df.head()


# In[23]:


#ok, now lets create the visualization 
x = df.groupby(['type']).count()
y = len(df)
r = ((x/y)).round(2)
mf_ratio = pd.DataFrame(r).T


# In[24]:


x


# In[25]:


r


# In[26]:


Transport = pd.DataFrame(x).T
Transport


# In[27]:


#Lets separate the country by the first name that 
df['first_country'] = df['country'].apply(lambda x:x.split(",")[0])
df['first_country']


# In[31]:


df.head(5)


# In[32]:


#lets group by country all the movies and TV shows
df['count']=1 #helper column
Movies_tv_by_country = df.groupby('first_country')['count'].sum().sort_values(ascending=False)[:10]


# In[33]:


Movies_tv_by_country


# In[40]:


Movies_tv_by_country.to_frame()


# In[34]:


S =Movies_tv_by_country


# In[45]:


# plotting a barchart
p1 = S.plot(kind='barh', title='Movies and TV Shows per country', yticks=[100,150,500, 1000,2500,3500,4500], color='r', alpha=1)
#alpha control the descolorization of color


# In[36]:


#lets filter only to Movies
Movies_only = df[df['type']=='Movie']


# In[37]:


Movies_only['count_movie']=1 #helper column
Movies_only = df.groupby('first_country')['count'].sum().sort_values(ascending=False)[:10]


# In[46]:


#lets plot only the movies 
p2 = Movies_only.plot(kind='barh', title='Movies and TV Shows per country', yticks=[100,150,500, 1000,2500,3500,4500], color='b', alpha=1)
p2


# In[ ]:




