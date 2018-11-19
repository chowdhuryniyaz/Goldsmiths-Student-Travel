import matplotlib.pyplot as plt
from  matplotlib.ticker import FuncFormatter
import pandas as pd
import numpy as np
from pandas.api.types import CategoricalDtype
from loadData import loadData, convertDataType

path = './data/survey_responses.csv'

df = loadData(path)
df = convertDataType(df)

df = df[df['mode_of_transport'] == 'walking']
df = df[['feel_safe_walking', 'gender']]

# cross tabulate gender and feel_safe_walking columns, calculate percentage from counts
df = pd.crosstab(df['gender'], df['feel_safe_walking']).apply(lambda r: r/r.sum(), axis=1)


fig, ax = plt.subplots()
colours = ['#004c6d', '#247392', '#449cb7', '#66c7dc', '#8bf3ff']

df.plot(kind = 'barh',stacked=True,
                ax =ax,
                color = colours,
                rot = 0)

ax.set_xlabel('Percentage %')
ax.set_ylabel('Gender')
plt.xticks([0, 0.25, 0.5, 0.75, 1],[0,25,50,75,100])
plt.title("How safe do students feel walking to Goldsmiths", pad=20, weight='heavy')
ax.grid(which='both', axis='x',alpha=0.25)
ax.legend(bbox_to_anchor=(0.5, -0.2), frameon=False, ncol=3, loc="center")
plt.tight_layout()
plt.show()