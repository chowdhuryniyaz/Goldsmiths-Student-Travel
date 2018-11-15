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
df = df[df['postcode'] != 'I would prefer not to say']
df.postcode.cat.remove_categories('I would prefer not to say', inplace=True)

# count the frequency for each category
counts = df['postcode'].value_counts(sort=True)
print(df['postcode'].value_counts())
# calcuate percentages from counts
pct = counts / counts.sum() * 100

fig, ax = plt.subplots()
colours=['#4D962E', '#70AD56', '#90CC76', '#B8EFA0', '#D2FFBF']
# Function to map the colors as a list from the input list of x variables (value counts)
def pltcolor(lst):
    cols=[]
    for l in lst:
        if l==7:
            cols.append('#4D962E')
        elif l==5:
            cols.append('#70AD56')
        elif l == 3:
            cols.append('#90CC76')
        elif l == 2:
            cols.append('#B8EFA0')
        else:
            cols.append('#D2FFBF')
    return cols
# Create the colors list using the function above
cols=pltcolor(df['postcode'].value_counts())

# make bar chart of postcode data
pct.plot(kind='barh',
ax = ax,
color=cols,
rot=0)
ax.set_xlabel('%')
ax.set_ylabel('Postcode')
plt.title("Term time postcode of respondents", pad=20, weight='heavy')
plt.tight_layout()
plt.show()