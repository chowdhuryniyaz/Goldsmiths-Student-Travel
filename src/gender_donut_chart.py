from pandas.api.types import CategoricalDtype
from loadData import loadData, convertDataType
from make_donut import make_donut

path = './data/survey_responses.csv'

# load and preprocess data
df = loadData(path)
df = convertDataType(df)

# respondents who refused an answer are not included in the analysis 
df.gender.cat.remove_categories('I would prefer not to say', inplace=True)


#table = df.groupby(['gender', 'mode_of_transport'])['gender'].count().reset_index(name="count")
# to get value counts for crosstabulated data
#table2 = pd.crosstab(df['mode_of_transport'], df['gender'])
#table2.to_csv('gender_and_mode.csv')

# make donut chart and save result as png
make_donut(df, column='gender', title='Gender split')