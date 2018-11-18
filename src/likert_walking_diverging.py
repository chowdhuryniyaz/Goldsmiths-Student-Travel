import matplotlib.pyplot as plt
from  matplotlib.ticker import FuncFormatter
import pandas as pd
import numpy as np
from pandas.api.types import CategoricalDtype
from loadData import loadData, convertDataType
from textwrap import wrap

path = './data/survey_responses.csv'

df = loadData(path)
df = convertDataType(df)

df = df[df['mode_of_transport'] == 'walking']
df = df[['pedestrian_crossings',
        'congested_route',
        'walk_alone',
        'well_maintained_pavements',
        'litter_on_route',
        'lighting_at_night',
        'pavements_not_wide']]

df = df.rename(columns = {'pedestrian_crossings': 'Not enough pedestrian crossings',
                        'congested_route': 'Route is crossings',
                        'walk_alone': 'Often walk alone',
                        'well_maintained_pavements': 'Pavements are well maintained',
                        'litter_on_route': 'Too much litter',
                        'lighting_at_night': 'Not enough lighting at night',
                        'pavements_not_wide': 'Pavements are not wide enough'})

df = df.melt(var_name = 'Statement', value_name = 'Answer')
table = pd.crosstab(df['Statement'], df['Answer'], normalize = 'index') * 100
table = table[['Strongly disagree', 'Somewhat disagree', 'Neither agree nor disagree', 'Somewhat agree', 'Strongly agree']]
table = table.round(1)
print(table.head())
colours = ['white','#004c6d', '#247392', '#449cb7', '#66c7dc', '#8bf3ff']

middles = table[["Strongly disagree", "Somewhat disagree"]].sum(axis=1)+table["Neither agree nor disagree"]*.5
longest = middles.max()
complete_longest = table.sum(axis=1).max()
table.insert(0, '', (middles - longest).abs())


ax = table.plot.barh(color = colours, rot = 0, stacked = True, figsize=(8,4), legend=False)

z = plt.axvline(longest, linestyle='--', color='black', alpha=.5)
z.set_zorder(-1)

plt.xlim(-14.2, complete_longest*1.8)

plt.xticks([-14.2, 35.8, 85.8, 135.8, 185.8], [100, 50, 0, 50, 100])

handles, labels = ax.get_legend_handles_labels()
labels = [ '\n'.join(wrap(l, 14)) for l in labels ]
ax.legend(handles, labels, bbox_to_anchor=(1.0, 0.75), frameon=False)

ax.set_xlabel('Percentage %')
ax.set_ylabel('Statements')

plt.title("To what extent do reponders agree with the following", pad=20, weight='heavy')
plt.tight_layout()
plt.show()