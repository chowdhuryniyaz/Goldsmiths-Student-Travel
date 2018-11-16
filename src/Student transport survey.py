
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import numpy as np


# In[3]:


import matplotlib.pyplot as plt


# In[4]:


df = pd.read_csv('./data/survey_responses.csv', index_col=0)


# In[5]:


df


# In[6]:


#Rename columns I will be using
df.rename(columns={'Which best describes your current term-time accommodation?':'term accom'}, inplace=True)
df.rename(columns={'What is your age?':'Age group'}, inplace=True)


# In[7]:


df.columns


# In[8]:


accom_df = df[['term accom','Age group']] #New DataFrame with two columnms
accom_df.dropna(inplace=True) #Drop any NaN results from the DataFrame
accom_df


# In[9]:


accom_df['Age group'].astype('category') #Set Age group column data as catergory variables
accom_df['term accom'].astype('category') #Set term accom column data as category variables 
accom_df.info()


# In[10]:


accom_bar= accom_df['term accom'].value_counts().plot(kind='bar', title='Term time accommodation') # Shows the value for each acommodation types
accom_bar.set_ylabel('Quantity')


# In[11]:


accom_df


# In[12]:


accom_df['Age group'].value_counts().plot(kind='pie', title='Age group breakdown') #Pie chart showing the age groups of participants


# In[13]:


# Decided to use matplotlib as I am able to display the percentage for each category and provide a legend
values= accom_df['Age group'].value_counts()
labels= accom_df['Age group']
plt.pie(values, counterclock=False, autopct='%1.1f%%')
plt.title('Age range of participants')
plt.legend(labels, loc=3)
values


# In[14]:


group1 = accom_df.groupby(['term accom', 'Age group']).size().unstack() #Group data in the Age group column, by the term accom categories
group1.plot(kind='bar', stacked=True, title='Accommodation and age breakdown') # Plot the group data


# In[15]:


#Fix for the labelling issue for the pie chart showing the age range of participants
values= accom_df['Age group'].value_counts()
labels= accom_df['Age group'].unique() #Creates a list of unique objecs from the column
labels.sort() #Sorts the list
plt.pie(values, counterclock=False, autopct='%1.1f%%')
plt.title('Age range of participants')
plt.legend(labels, loc=3)

plt.show()

