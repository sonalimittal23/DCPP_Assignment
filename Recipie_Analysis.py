#!/usr/bin/env python
# coding: utf-8

# In[39]:


import pandas as pd
import datetime
import seaborn as sns
#import chart_studio.plotly as py
import plotly.express as px
import dateutil
import matplotlib
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')
from matplotlib import pyplot as plt
matplotlib.style.use('ggplot')


# In[47]:


recipe = pd.read_csv('C:/Users/HP/Documents/Python/Project/Final_Dataset.csv')
#recipe.head(5)


# In[48]:


#Recipie with the maximum views
recipe["Views"] = pd.to_numeric(recipe["Views"])
max=recipe['Views'].argmax()
recipe.iloc[max]


# In[49]:


# Recipie with maximum protien content
recipe["Protein"] = pd.to_numeric(recipe["Protein"])
max_protien=recipe['Protein'].argmax()
recipe.iloc[max_protien]


# In[50]:


# Dish with max carbs and fat
recipe["Fat"] = pd.to_numeric(recipe["Fat"])
recipe["Carbs"] = pd.to_numeric(recipe["Carbs"])
sum_dish= recipe["Fat"] + recipe["Carbs"]
max_fat_carbs=sum_dish.argmax()
recipe.iloc[max_fat_carbs]


# In[51]:


# Dish with the maximum calorie content
recipe["Calorie"] = pd.to_numeric(recipe["Calorie"])
max_calorie=recipe['Calorie'].argmax()
recipe.iloc[max_calorie]


# In[52]:


#Dishes with max total time
recipe["Total_Time_In_Mins"] = pd.to_numeric(recipe["Total_Time_In_Mins"])
max_total_time=recipe['Total_Time_In_Mins'].argmax()
recipe.iloc[max_total_time]


# In[53]:


#Min total time 4-5 mins
min_total_time=pd.DataFrame()
min_total_time=recipe.sort_values('Total_Time_In_Mins')
min_total_time=min_total_time[min_total_time['Total_Time_In_Mins']!=0]
min_total_time=min_total_time[min_total_time['Total_Time_In_Mins']<=5]


# In[54]:


plt.figure(figsize=(10,6))
sns.barplot(x=min_total_time['Total_Time_In_Mins'],y=min_total_time['Recipe_Name'])

plt.xlabel('Total Time In Minutes')
plt.ylabel('Recipe Name')
plt.show()



# In[55]:


#Diabetic Friendly dishes
recipe.loc[recipe['Diet'] == "Diabetic Friendly"]['Recipe_Name'].tolist()


# In[56]:


# Most popular cuisine based on views
test=recipe
test=test[['Cuisine','Views']]
test=test.groupby(['Cuisine']).mean()
test=test.reset_index().sort_values(by='Views',ascending=False).head(10)
test['Views'] = test['Views'].astype(int)
test


# In[57]:


plt.figure(figsize=(30,6))
sns.barplot(x=test['Cuisine'],y=test['Views'])

plt.xlabel('Cuisines')
plt.ylabel('Average Views')
plt.show()


# In[58]:


# Veg vs non veg based on cook and prep time 
df_filtered=pd.DataFrame()
df_filtered = recipe[recipe['Diet'].isin(["Vegetarian","Non Vegeterian"])]


# In[59]:


figure = px.scatter(df_filtered,x='Cook_Time_In_Mins',y='Prep_Time_In_Mins',color='Diet',
                 color_discrete_sequence=['green','red'])
figure.show()

