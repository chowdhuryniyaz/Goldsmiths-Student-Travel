import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pandas.api.types import CategoricalDtype
from loadData import *

path = './data/survey_responses.csv'

# load and preprocess data
df = loadData(path)
df = convertDataType(df)

# respondents who refused an answer are not included in the analysis 
df = df[df['age'] != 'I would prefer not to say']
df.age.cat.remove_categories('I would prefer not to say', inplace=True)

# count the frequency for each category
counts = df['age'].value_counts(sort=False)

# calcuate percentages from counts
pct = counts / counts.sum() * 100

fig, ax = plt.subplots()
colours=['#4D962E', '#70AD56', '#90CC76', '#B8EFA0', '#D2FFBF']

# make bar chart of age data
pct.plot(kind='barh',
ax = ax,
color=colours,
rot=0)
ax.set_xlabel('%')
ax.set_ylabel('Age')
plt.title("Age of respondents", pad=20, weight='heavy')
plt.tight_layout()
plt.show()