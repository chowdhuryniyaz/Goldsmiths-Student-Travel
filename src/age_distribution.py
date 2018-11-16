import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pandas.api.types import CategoricalDtype
from loadData import *
from textwrap import wrap

path = './data/survey_responses.csv'

# load and preprocess data
df = loadData(path)
df = convertDataType(df)

# respondents who refused an answer are not included in the analysis 
df = df[df['age'] != 'I would prefer not to say']
df.age.cat.remove_categories('I would prefer not to say', inplace=True)

fig, ax = plt.subplots()

# plot distribution of age data
#use the cat.codes method to access the underlying numerical values representing the ordered categories
time_codes = df['age'].cat.codes 
time_codes.name = 'Students'
ax = time_codes.plot.box() 
ax.set_ylabel('Age (years)')
ax.set_yticks([0, 1, 2, 3, 4])
ax.set_yticklabels(labels=df.age.cat.categories)
plt.title('Distribution of respondents age', pad=30, weight='heavy')
plt.tight_layout()
plt.show()
