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
df = df[['level']]

# respondents who refused an answer are not included in the analysis 
df = df[df['level'] != 'other']
df.level.cat.remove_categories('other', inplace=True)

# calculate % from value counts
counts = df.apply(lambda x: x.value_counts() / len(x)*100).transpose()

fig, ax = plt.subplots()
# plot values as stacked bar
counts.plot(ax = ax,kind='barh', stacked=True, rot=0, width=0.05, color=['#3C8C1A','#70AD56', '#90CC76'], legend=None)

# get width of each bar section
x1 = ax.patches[0].get_width()
x2 = ax.patches[1].get_width()
x3 = ax.patches[2].get_width()

# add text
ax.text(0, 0.05, 'Level of study', fontdict={'fontweight':'bold', 'fontsize':14})
ax.text(0, -0.05, 'Undergraduate: {:.0f}%'.format(x1), fontdict={'color':'#3C8C1A', 'fontweight':'heavy', 'fontsize':12})
ax.text(x1, -0.05, 'Postgraduate: {:.0f}%'.format(x2), fontdict={'color':'#70AD56', 'fontweight':'heavy', 'fontsize':12})
ax.text(x1, -0.075, 'Foundation: {:.0f}%'.format(x3), fontdict={'color':'#90CC76', 'fontweight':'heavy', 'fontsize':12})
# ax.annotate('Postgraduate: {:.0f}%'.format(x2), xy=(x1+x2/2, -0.025), 
#             xytext=(x1-x1/3, -0.085), color='#70AD56', fontsize=12, fontweight='heavy',
#             arrowprops=dict(color='#70AD56', arrowstyle="->"))
# ax.annotate('Foundation: {:.0f}%'.format(x3), xy=(x1+x2+(x3/2), -0.025), 
#             xytext=(x1+5, -0.12), color='#90CC76', fontsize=12, fontweight='heavy',
#             arrowprops=dict(color='#90CC76', arrowstyle="->"))
# hide axis
plt.axis('off')
plt.tight_layout()
# to save the chart as a png image, uncomment the line below
#plt.savefig("mode_of_study_barh.png", bbox_inches="tight", dpi=200)
plt.show()
