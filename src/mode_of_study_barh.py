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

# select mode_of_study column
df = df[['mode_of_study']]

# respondents who refused an answer are not included in the analysis 
df = df[df['mode_of_study'] != 'other']
df.mode_of_study.cat.remove_categories('other', inplace=True)

# calculate % from value counts
counts = df.apply(lambda x: x.value_counts() / len(x)*100).transpose()

fig, ax = plt.subplots()
# plot values as stacked bar
counts.plot(ax = ax,kind='barh', stacked=True, rot=0, width=0.05, color=['#3C8C1A','#70AD56'], legend=None)

# get width of each bar section
x1 = ax.patches[0].get_width()
x2 = ax.patches[1].get_width()
# add text
ax.text(0, 0.05, 'Mode of study', fontdict={'fontweight':'bold', 'fontsize':14})
ax.text(0, -0.05, 'Full time: {:.0f}%'.format(x1), fontdict={'color':'#3C8C1A', 'fontweight':'heavy', 'fontsize':12})
ax.text(x1-x2/2, -0.05, 'Part time: {:.0f}%'.format(x2), fontdict={'color':'#70AD56', 'fontweight':'heavy', 'fontsize':12})
# hide axis
plt.axis('off')
plt.tight_layout()
# to save the chart as a png image, uncomment the line below
#plt.savefig("mode_of_study_barh.png", bbox_inches="tight", dpi=200)
plt.show()