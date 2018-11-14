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
        startangle=90,
        autopct='%.0f%%')

# Equal aspect ratio ensures that pie is drawn as a circle.
ax.axis('equal')
plt.subplots_adjust(bottom=0.1)

# Put a legend below current axis
plt.legend(df.gender.cat.categories,bbox_to_anchor=(0.5,0),loc="lower center", bbox_transform=fig.transFigure, ncol=2)
plt.title("Gender split")
plt.tight_layout()
plt.show()
# to save the chart as a ong image, uncomment the line below
#plt.savefig("gender_split_pie.png", bbox_inches="tight")