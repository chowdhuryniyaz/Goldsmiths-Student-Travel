
#%%
import pandas as pd
from pandas.api.types import CategoricalDtype
import matplotlib.pyplot as plt
import numpy as np


#%%
df = pd.read_csv('./Student Transport Survey/Student Transport Survey.csv')


#%%
df.rename(columns = {'What is your term time postcode?': 'Postcode',
                    'Which best describes your current term-time accommodation?': 'Type of accommodation',
                    'What is your average journey time from your home to Goldsmiths?': 'Average journey time',
                    'What time did you arrive at Goldsmiths each day last week? [Monday]': 'Time of arrival on Monday',
                    'What time did you arrive at Goldsmiths each day last week? [Tuesday]': 'Time of arrival on Tuesday',
                    'What time did you arrive at Goldsmiths each day last week? [Wednesday]': 'Time of arrival on Wednesday',
                    'What time did you arrive at Goldsmiths each day last week? [Thursday]': 'Time of arrival on Thursday',
                    'What time did you arrive at Goldsmiths each day last week? [Friday]': 'Time of arrival on Friday',
                    'What time did you leave Goldsmiths each day last week? [Monday]': 'Time of departure on Monday',
                    'What time did you leave Goldsmiths each day last week? [Tuesday]': 'Time of departure on Tuesday',
                    'What time did you leave Goldsmiths each day last week? [Wednesday]': 'Time of departure on Wednesday',
                    'What time did you leave Goldsmiths each day last week? [Thursday]': 'Time of departure on Thursday',
                    'What time did you leave Goldsmiths each day last week? [Friday]': 'Time of departure on Friday',
                    'How do you usually travel from home to Goldsmiths?': 'Travel type',
                    'Why do you commute by public transport?': 'Reason for public transport',
                    'Which modes of transportation do you normally use to travel to Goldsmiths?': 'Mode of public transport',
                    'Which station do you use to travel to Goldsmiths?': 'Exit station',
                    'What type of ticket do you use?': 'Type of ticket',
                    'Why do you travel by motor vehicle to Goldsmiths?': 'Reason for motor vehicle',
                    'Are you the driver or a passenger?':'Driver or Passenger',
                    'If you drive to Goldsmiths where do you normally park your vehicle?':'Location of parking for motor vehicle',
                    'What changes would encourage you to try an alternative mode of transport?': 'Changes need to use alternate modes of transport',
                    'Why do you walk to Goldsmiths?': 'Reason for walking',
                    'Which of these are on your route?': 'Seen on route',
                    'To what extent do you agree or disagree with the following statements?   [There is a lot of litter on my route]': 'There is too much litter',
                    'To what extent do you agree or disagree with the following statements?   [I walk most often alone]': 'Often walk alone',
                    'To what extent do you agree or disagree with the following statements?   [The pavements are well maintained]': 'Pavements are well maintained',
                    'To what extent do you agree or disagree with the following statements?   [There is not enough lighting at night]': 'Not enough lighting at night',
                    'To what extent do you agree or disagree with the following statements?   [The pavements are not wide enough]': 'Pavements are not wide enough',
                    'To what extent do you agree or disagree with the following statements?   [My route is too congested]': 'Route is congested',
                    'To what extent do you agree or disagree with the following statements?   [There are not enough pedestrian crossings]': 'Not enough pedestrian crossings',
                    'How safe do you feel when walking to Goldsmiths?': 'Safety level when walking',
                    'Why do you cycle to Goldsmiths?': 'Reason for cycling',
                    'Where do you park your bicycle at Goldsmiths?': 'Location of parking for bicycle',
                    'What cycling safety clothing and/or equipment do you use?': 'Safety clothing/equipment',
                    'How safe do you feel when cycling to Goldsmiths?': 'Safety level when cycling',
                    'Why do you travel this way to Goldsmiths?': 'Reason for other',
                    'What is your age?': 'Age range',
                    'Which gender do you identify most with?': 'Gender identity',
                    'Which of the following best describes your current level of study?': 'Current level of study',
                    'What year of study are you in?': 'Year of study',
                    'Which of the following statements best describes you?': 'Domicile'}, inplace = True)
df


#%%
on_foot_df = df[['Postcode', 'Type of accommodation', 'Average journey time', 'Seen on route']].where(df['Travel type'] == 'On foot')
on_foot_df.dropna(inplace = True)
on_foot_df


#%%
on_foot_df.describe()


#%%
seen_landmarks1 = on_foot_df['Seen on route'].str.split(';')
seen_landmarks1


#%%
seen_landmarks2 = on_foot_df['Seen on route'].str.split(';', expand = True)
seen_landmarks2


#%%
safe_on_foot_df = df[['Gender identity',
                      'Type of accommodation',
                      'Average journey time',
                      'Safety level when walking']].where(df['Travel type'] == 'On foot')
safe_on_foot_df.dropna(inplace = True)
safe_on_foot_df


#%%
safe_on_foot_df.describe()


#%%
tabled_safety = pd.crosstab(safe_on_foot_df['Gender identity'], safe_on_foot_df['Safety level when walking'])
tabled_safety


#%%
tabled_safety.describe()


#%%
ax = tabled_safety.plot.barh(color = [plt.cm.Reds(x)
                                       for x in
                                           (0.5 + i * 1.5/5
                                            for i in range(5))],
                               width = 1,
                               edgecolor = 'black')
ax.invert_yaxis()
ax.set_title('How safe do people feel walking to Goldsmiths')
ax.set_xlabel('Frequency')
fig_size = plt.rcParams["figure.figsize"]
#print ("Current size:", fig_size)
fig_size[0] = 15
fig_size[1] = 10
#plt.show()
plt.xticks()
plt.savefig('safety_on_foot', bbox_inches = 'tight')


#%%
opinions_on_foot_df = df[['There is too much litter',
                      'Often walk alone',
                      'Pavements are well maintained',
                      'Not enough lighting at night',
                      'Pavements are not wide enough',
                      'Route is congested',
                      'Not enough pedestrian crossings']].where(df['Travel type'] == 'On foot')
opinions_on_foot_df.dropna(inplace = True)
opinions_on_foot_df


#%%
opinions_on_foot_df.describe()


#%%
melted_opinions_on_foot_df = opinions_on_foot_df.melt(var_name = 'Situations',
                                            value_name = 'Answer')
melted_opinions_on_foot_df


#%%
tabled_opinions = pd.crosstab(melted_opinions_on_foot_df['Situations'], melted_opinions_on_foot_df['Answer'], normalize ='index') * 100

reorder_columns = tabled_opinions.columns.tolist()
reorder_columns = reorder_columns[4:] + reorder_columns[2:3] + reorder_columns[0:2] + reorder_columns[3:4]

tabled_opinions = tabled_opinions[reorder_columns]
tabled_opinions


#%%
tabled_opinions.describe()


#%%
ax = tabled_opinions.plot.barh(stacked = True,
                               color = [plt.cm.Greens(x)
                                       for x in
                                           (0.1 + i * 1.2/5
                                            for i in range(5))],
                               width = 1,
                               edgecolor = 'black')

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, bbox_to_anchor=(1.0, 1.0))
ax.set_xlabel('Percentage of responders')
ax.set_title('To what extent do responders agree with the following?')
#plt.show()
fig_size = plt.rcParams["figure.figsize"]
print ("Current size:", fig_size)
fig_size[0] = 15
fig_size[1] = 10
plt.savefig('opinion_on_foot', bbox_inches = 'tight', pad_inches = 1)



