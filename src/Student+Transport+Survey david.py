
# coding: utf-8

# In[6]:


import pandas as pd


# In[61]:


import numpy as np


# In[56]:


df=pd.read_csv("Student Transport Survey.csv", index_col= 0)
df


# In[10]:


df.describe()


# In[11]:


df.info()


# In[15]:


df = pd.read_csv('Student Transport Survey.csv',
usecols=[15, 17, 18])
# Assign easier to type column names.
df.columns = ['reasons of commuting', 'station/bus stop', 'type of ticket']
df


# In[19]:


import matplotlib.pyplot as plt
import numpy as np


# In[22]:


people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
y_pos = np.arange(len(people))
performance = 3 + 10 * np.random.rand(len(people))
error = np.random.rand(len(people))

ax.barh(y_pos, performance, xerr=error, align='center',
        color='green', ecolor='black')
ax.set_yticks(y_pos)
ax.set_yticklabels(people)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('Performance')
ax.set_title('How fast do you want to go today?')

plt.show()


# In[29]:




get_ipython().run_line_magic('matplotlib', 'inline')

import matplotlib.pyplot as plt

pronouns = ['new cross gate', 'new cross', 'bus stop','peckham','dont make sense']
totals = ['55' , '30' , '5','5','5']

plt.pie(totals,
       labels= pronouns, autopct='%1.0f%%')
plt.show()


# In[32]:




get_ipython().run_line_magic('matplotlib', 'inline')

import matplotlib.pyplot as plt

pronouns = ['pay as you go', 'single day ticket', 'weekly travelcard','monthly travelcard','3 months travelcard','annual travel card']
totals = ['55' , '5' , '20','15','5','0']

plt.pie(totals,
       labels= pronouns, autopct='%1.0f%%')
plt.show()


# In[54]:



plt.ylabel("reason of commuting")
plt.xlabel("totals")
plt.title("why student commute by public transport")

# Make fake dataset
height = [2, 6, 2, 1, 4, 10, 1, 6, 3, 2, 8, 7]
bars = ('i dont have motor vehicle', 'its most cost effective way', 'more environment friendly', 'less stress than drving', 'i dont have driving licence', 'quickest way','i enjoy it','more flexibility','relax/study in journey','avoid conjestion','good transport','too long walking/cycling'
)
y_pos = np.arange(len(bars))
 
# Create horizontal bars
plt.barh(y_pos, height)
 
# Create names on the y-axis
plt.yticks(y_pos, bars)
 
# Show graphic
plt.show()

