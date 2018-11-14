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
df.gender.cat.remove_categories('I would prefer not to say', inplace=True)
colours = ['#ffa600', '#ff6361', '#bc5090', '#58508d']

fig, ax = plt.subplots(figsize=(6, 4))

# create pie chart from gender column
ax.pie(df.gender.value_counts(),
        colors=colours,
        labels=df.gender.cat.categories,
        startangle=90,
        wedgeprops = {'linewidth': 0.5, 'edgecolor' : 'lightgrey', 'width':0.5},
        textprops={'size': 'small', 'weight':'heavy'},
        autopct='%.0f%%',
        pctdistance=0.75, 
        labeldistance=1.1)

# Equal aspect ratio ensures that pie is drawn as a circle.
ax.axis('equal')
plt.subplots_adjust(bottom=0.1)

# Put a legend below current axis
#plt.legend(df.gender.cat.categories,bbox_to_anchor=(0.5,0),loc="lower center", bbox_transform=fig.transFigure, ncol=2)
plt.title("Gender split", pad=30, weight='heavy')
plt.tight_layout()

# to save the chart as a png image, uncomment the line below
#plt.savefig("gender_split_pie.png", bbox_inches="tight", dpi=200)
plt.show()
