import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pandas.api.types import CategoricalDtype
from loadData import loadData, convertDataType
from textwrap import wrap

path = './data/survey_responses.csv'

# load and preprocess data
df = loadData(path)
df = convertDataType(df)

# create a new dataframe by copying a few specific columns from the original dataframe
# list indexing with .loc always returns a copy
df1 = df.loc[:, ['mode_of_transport', 'avg_journey_time']]

# respondents who refused an answer are not included in the analysis 
df1 = df1[df1['mode_of_transport'] != 'other']

# drop rows where NaN appears
df1 = df1.dropna()

df2 = pd.crosstab(df1['mode_of_transport'], df1['avg_journey_time'])
# save  data (margins = True here)

# to save crosstabulation data: mode vs time counts
#df3 = pd.crosstab(df1['mode_of_transport'], df1['avg_journey_time'], margins=True)
#df3.to_csv('./data/mode_vs_time.csv')

# use visually equidistant colours
cols = ['#003f5c', '#58508d', '#bc5090', '#ff6361', '#ffa600']
ax = df2.plot.barh(stacked=True, figsize=(8,4), color=cols)
handles, labels = ax.get_legend_handles_labels()
labels = [ '\n'.join(wrap(l, 20)) for l in labels ]
ax.legend(handles, labels, bbox_to_anchor=(1.0, 1.0), frameon=False)

plt.title('Mode of transport vs journey time', pad=20)
ax.set_xlabel("Number of students")
ax.set_ylabel("Mode of transport") 
plt.xticks([0,5,10,15,20])

ax.grid(which='both', axis='x',alpha=0.5)
plt.tight_layout()
plt.show()