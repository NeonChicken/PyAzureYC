#!/usr/bin/env python
# coding: utf-8

# In[93]:


import pandas as pd
import matplotlib.pyplot as plt
import matplotlib


# In[94]:


pd.__version__


# In[95]:


matplotlib.__version__


# In[64]:


data = pd.read_csv("Food_composition_dataset.csv", encoding='latin-1', sep=';', decimal=',')


# In[65]:


data.head()


# In[66]:


data[['COUNTRY']]


# In[67]:


data[:5]


# In[68]:


data[:500].mean()


# In[69]:


data[:1000].describe()


# In[70]:


data.columns


# In[71]:


data['COUNTRY'].unique()


# In[72]:


data['COUNTRY'] == 'Netherlands'


# In[73]:


data_nl = data[data['COUNTRY'] == 'Netherlands']
data_nl


# In[74]:


data_nl['NUTRIENT_TEXT'].unique()


# In[75]:


data_new = data_nl.copy()
data_new.columns = ['FOOD_ID', 'code', 'COUNTRY', 'efsaprodcode2', 'name',
       'level1', 'level2', 'level3', 'NUTRIENT_ID', 'voedingsstof', 'UNIT',
       'mg/100g']


# In[76]:


data_new.head()


# In[77]:


data_new['UNIT'].unique()


# In[78]:


data_val = []
for idx, row in data_new.iterrows():
    if row['UNIT'].startswith('Microgram'):
        data_val.append(row['mg/100g'] / 1000)
    else:
        data_val.append(row['mg/100g'])


# In[79]:


data_copy = data_new.copy()
data_copy['mg/100g'] = data_val
data_copy[:3]


# In[80]:


data_new.describe()


# In[81]:


data_copy.describe()


# In[83]:


data_drop = data_copy.drop(columns=['FOOD_ID', 'code', 'COUNTRY', 'efsaprodcode2', 
       'level1', 'level2', 'level3', 'NUTRIENT_ID', 'UNIT'
       ])
data_drop[:3]


# In[84]:


data_drop.set_index('name')


# In[87]:


data_pivot = data_drop.pivot_table(index='name', columns='voedingsstof', values='mg/100g')
data_pivot[:3]


# In[88]:


data_pivot.columns.name


# In[90]:


data_pivot.columns.name = 'mg/100g'
data_pivot[:3]


# # Visualisatie

# In[100]:


plt.plot(range(10, 20))
plt.show()


# In[105]:


plt.plot(range(len(data_pivot)), data_pivot['Calcium (Ca)'])
plt.show()


# In[107]:


plt.plot(range(len(data_pivot)), data_pivot['Calcium (Ca)'])
plt.ylabel('Calcium (mg/100g)')
plt.xlabel('Index')
plt.title('Hoeveelheid calcium per product')
plt.show()


# In[110]:


plt.hist(data_pivot['Calcium (Ca)'])
plt.title('Verdeling Ca in voedingsstoffen')
plt.ylabel('Aantal voedingsmiddelen')
plt.xlabel('Ca (mg/100g)')
plt.show()


# In[118]:


plt.hist(data_pivot['Calcium (Ca)'], log=True, bins=50)
plt.title('Verdeling Ca in voedingsstoffen')
plt.ylabel('Aantal voedingsmiddelen')
plt.xlabel('Ca (mg/100g)')
plt.show()


# In[119]:


data_pivot.columns


# In[124]:


plt.bar(data_pivot.columns, data_pivot.mean())
plt.ylabel("Hoeveelheid (mg/100g)")
plt.xlabel('Voedingsstof')
plt.xticks(rotation=-90)
plt.show()


# In[126]:


plt.barh(data_pivot.columns, data_pivot.mean())
plt.xlabel("Hoeveelheid (mg/100g)")
plt.ylabel('Voedingsstoffen')
plt.show()


# In[134]:


data[data['NUTRIENT_TEXT'] == 'Calcium (Ca)'][['COUNTRY', 'LEVEL']].groupby('COUNTRY').mean()
x = data[data['NUTRIENT_TEXT'] == 'Calcium (Ca)'][['COUNTRY', 'LEVEL']].groupby('COUNTRY').mean().index
y = data[data['NUTRIENT_TEXT'] == 'Calcium (Ca)'][['COUNTRY', 'LEVEL']].groupby('COUNTRY').mean().values


# In[142]:


plt.bar(x, y.reshape(len(y)))
plt.title("Gemiddelde Calcium waardes per land")
plt.xlabel("Landen")
plt.xticks(rotation=-80)
plt.ylabel("Ca (mg/100)")
plt.show()
# Als je als png wil opslaan
# plt.savefig('Gemiddeld-Calcium-Per-Land')

# In[ ]:




