import matplotlib.pyplot as plt
from pandas.api.types import CategoricalDtype
from loadData import loadData, convertDataType
from textwrap import wrap

path = './data/survey_responses.csv'

# load and preprocess data
df = loadData(path)
df = convertDataType(df)

# count the frequency for each category
counts = df['avg_journey_time'].value_counts(sort=False)

# calcuate percentages from counts
pct = counts / counts.sum() * 100

fig, ax = plt.subplots()
colours=['#004c6d', '#247392', '#449cb7', '#66c7dc', '#8bf3ff']

# make bar chart of avg_journey_time data
pct.plot(kind='barh',
ax = ax,
color='#004c6d',
rot=0)
ax.set_xlabel('%')
ax.set_ylabel('Journey time')
plt.title("Average journey time to reach Goldsmiths", pad=20, weight='heavy')
plt.tight_layout()
plt.show()

# to get summary table of average journey time
table = df.groupby(['avg_journey_time'])['avg_journey_time'].count().reset_index(name="Number of responses")
table['Percentage'] = pct.values
#table.to_csv('avg_journey_time.csv')

#table = df.groupby(['avg_journey_time', 'mode_of_transport'])['avg_journey_time'].count().reset_index(name="count")
# to get vlue counts for subgroups
#table2 = pd.crosstab(df['avg_journey_time'], df['mode_of_transport'])
#table2.to_csv('gender_and_mode.csv')