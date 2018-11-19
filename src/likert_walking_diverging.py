import matplotlib.pyplot as plt
from  matplotlib.ticker import FuncFormatter
import pandas as pd
import numpy as np
from pandas.api.types import CategoricalDtype
from loadData import loadData, convertDataType
from textwrap import wrap
# Heiberger, Richard M., and Naomi B. Robbins. "Design of diverging stacked bar charts for Likert scales and other applications." 
# Journal of Statistical Software 57.5 (2014): 1-32.
# diverging stacked bar chart
# The key mechanism is to add in an invisible buffer at the start.
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
                        'congested_route': 'Route is congested',
                        'walk_alone': 'Often walk alone',
                        'well_maintained_pavements': 'Pavements are well maintained',
                        'litter_on_route': 'Too much litter',
                        'lighting_at_night': 'Not enough lighting at night',
                        'pavements_not_wide': 'Pavements are not wide enough'})

df = df.melt(var_name = 'Statement', value_name = 'Answer')
table = pd.crosstab(df['Statement'], df['Answer'], normalize = 'index') * 100
table = table[['Strongly disagree', 'Somewhat disagree', 'Neither agree nor disagree', 'Somewhat agree', 'Strongly agree']]
table = table.round(1)

colours = ['white','#004c6d', '#247392', '#449cb7', '#66c7dc', '#8bf3ff']

# calculate the width of the left two columns ('Strongly disagree', 'Somewhat disagree') 
# and half of the middle column 'Neither agree nor disagree'
middles = table[["Strongly disagree", "Somewhat disagree"]].sum(axis=1)+table["Neither agree nor disagree"]*.5
# find the longest column and use its width to calculate the difference needed for the other columns
longest = middles.max()
# the maximum of the sum of all the lines (i.e., the length of the longest line)
complete_longest = table.sum(axis=1).max()
# insert this new buffer column into the first column position with a blank title - not the most elegant solution
table.insert(0, '', (middles - longest).abs())


ax = table.plot.barh(color = colours, rot = 0, stacked = True, figsize=(8,4), legend=False)

# add a vertical line (axvline) behind the middle of the middle bar
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