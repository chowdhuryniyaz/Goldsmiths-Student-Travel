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
df.region.cat.remove_categories('other', inplace=True)

colours = ['#bc5090', '#003f5c', '#ffa600']

fig, ax = plt.subplots(figsize=(6, 4))

# create pie chart from gender column
patches, texts, autotexts = ax.pie(df.region.value_counts(),
        colors=colours,
        labels=df.region.cat.categories,
        startangle=50,
        wedgeprops = {'linewidth': 0.5, 'edgecolor' : 'lightgrey', 'width':0.5},
        textprops={'weight':'heavy'},
        autopct='%.0f%%',
        pctdistance=0.75, 
        labeldistance=1.1)

for t in autotexts:
        t.set_fontsize(14)


# Equal aspect ratio ensures that pie is drawn as a circle.
ax.axis('equal')
plt.subplots_adjust(bottom=0.1)

# Put a legend below current axis
#plt.legend(df.gender.cat.categories,bbox_to_anchor=(0.5,0),loc="lower center", bbox_transform=fig.transFigure, ncol=2)
plt.title("Region split", pad=30, weight='heavy')
plt.tight_layout()

# to save the chart as a png image, uncomment the line below
#plt.savefig("gender_split_pie.png", bbox_inches="tight", dpi=200)
plt.show()
