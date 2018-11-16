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

# use visually equidistant colours
colours = ['#ffa600', '#ff6361', '#bc5090', '#58508d']
#table = df.groupby(['gender', 'mode_of_transport'])['gender'].count().reset_index(name="count")
# to get value counts for crosstabulated data
#table2 = pd.crosstab(df['mode_of_transport'], df['gender'])
#table2.to_csv('gender_and_mode.csv')

fig, ax = plt.subplots(figsize=(6, 4))

# create pie chart from gender column
patches, texts, autotexts = ax.pie(df.gender.value_counts(sort=False),
        colors=colours,
        #labels=df.gender.cat.categories,
        startangle=60,
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
plt.legend(df.gender.cat.categories,bbox_to_anchor=(1,0.5),loc="center left", frameon=False)
plt.title("Gender split", pad=30, weight='heavy')
plt.tight_layout()

# to save the chart as a png image, uncomment the line below
#plt.savefig("gender_split_donut.png", bbox_inches="tight", dpi=200)
plt.show()
