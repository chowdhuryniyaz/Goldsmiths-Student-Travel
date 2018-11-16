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

# term time accommodation
# respondents who refused an answer are not included in the analysis 
df = df[df['accommodation_type'] != 'other']
df.accommodation_type.cat.remove_categories('other', inplace=True)
df = df[['accommodation_type']]

# use visually equidistant colours
colours = ['#ffa600', '#ff6361', '#bc5090', '#58508d']

fig, ax = plt.subplots(figsize=(6, 4))

# create pie chart from accommodation_type column
patches, texts, autotexts = ax.pie(df.accommodation_type.value_counts(sort=False),
        colors=colours,
        #labels=df.accommodation_type.cat.categories,
        startangle=90,
        wedgeprops = {'linewidth': 0.75, 'edgecolor' : 'lightgrey', 'width':0.5},
        #textprops={'weight':'heavy'},
        autopct='%.0f%%',
        pctdistance=0.75, 
        labeldistance=1.1)

for t in autotexts:
        t.set_fontsize(12)

# Equal aspect ratio ensures that pie is drawn as a circle.
ax.axis('equal')
plt.subplots_adjust(bottom=0.1)

# Put a legend next to the chart, hide frame
plt.legend(df.accommodation_type.cat.categories,bbox_to_anchor=(1,0.5),loc="center left", frameon=False)
plt.title("Accommodation type", pad=30, weight='heavy')
plt.tight_layout()

# to save the chart as a png image, uncomment the line below
#plt.savefig("accomodation_donut.png", bbox_inches="tight", dpi=200)
plt.show()
