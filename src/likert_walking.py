import matplotlib.pyplot as plt
from  matplotlib.ticker import FuncFormatter
import pandas as pd
import numpy as np
from pandas.api.types import CategoricalDtype
from loadData import *

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

colours = ['#004c6d', '#247392', '#449cb7', '#66c7dc', '#8bf3ff']
ax = table.plot.barh(color = colours, rot = 0, stacked = True)
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3, borderaxespad=0.)
ax.set_xlabel('Percentage %')
ax.set_ylabel('Statements')
plt.title("To what extent do reponders agree with the following", pad=20, weight='heavy')
plt.tight_layout()
plt.show()