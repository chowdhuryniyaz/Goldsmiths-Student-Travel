import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pandas.api.types import CategoricalDtype
from loadData import *

def preprocess(df):
    """
    Set data type as categorical (nominal or odinal) 
    Args:
        df: Pandas DataFrame
    Returns:
        df: Pandas DataFrame, with data types set as cetegorical
    """
    # set data type of age column as ordinal (ordered categorical)
    age_type = CategoricalDtype(ordered=True, categories=['18 - 21', '22 - 25', '26 - 30', '31 - 40', 'Over 40', 'I would prefer not to say'])
    df['age'] = df['age'].astype(age_type)
    
    # set data type of gender column as nominal
    gender_type = CategoricalDtype(ordered=False, categories=['Female', 'Male', 'Prefer to self-describe', 'Non-binary / third gender', 'I would prefer not to say'])
    df['gender'] = df['gender'].astype(gender_type)

    # set data type of region column as nominal
    region_type = CategoricalDtype(ordered=False, categories=['UK', 'EU', 'overseas', 'other'])
    df['region'] = df['region'].apply(regionHelper).astype(region_type)

    # set data type of level of study as nominal
    level_of_study_type = CategoricalDtype(ordered=False, categories=['FT undergraduate', 'FT postgraduate', 'PT undergraduate', 'PT postgraduate', 'Foundation', 'not sure'])
    df['level_of_study'] = df['level_of_study'].apply(levelOfStudyHelper).astype(level_of_study_type)

    # create mode_of_study column to separate FT/PT students
    mode_of_study_type = CategoricalDtype(ordered=False, categories=['full time', 'part time', 'other'])
    df['mode_of_study'] = df['level_of_study'].map({'FT undergraduate': 'full time', 'FT postgraduate': 'full time', 'PT undergraduate': 'part time', 'PT postgraduate': 'part time', 'Foundation': 'full time', 'not sure': 'other'}).astype(mode_of_study_type)

    # set data type of year of study column as ordinal
    year_of_study_type = CategoricalDtype(ordered=True, categories=['0', '1', '2', '3', '3+', 'other'])
    df['year_of_study'] = df['year_of_study'].map({'0 (Foundation only)': '0', '1 (UG)': '1', '2 (UG)': '2', '3 (UG)': '3', '3+': '3+', np.NaN: 'other'}).astype(year_of_study_type)

    return df

# assign easier to type values in region column
def regionHelper(x):
    if x == 'I am a UK citizen studying in the UK':
        return 'UK'
    elif x == 'I am an international student from within the EU studying in the UK':
        return 'EU'
    elif x == 'I am an international student from outside the EU studying in the UK':
        return 'overseas'
    else:
        return 'other'

def levelOfStudyHelper(x):
    if x == 'Full-time undergraduate student':
        return 'FT undergraduate'
    elif x == 'Full-time postgraduate student':
        return 'FT postgraduate'
    elif x == 'Part-time postgraduate student':
        return 'PT postgraduate'
    elif x == 'Part-time undergraduate student':
        return 'PT undergraduate'
    elif x == 'Foundation':
        return 'Foundation'
    else:
        return 'not sure'

path = './data/survey_responses.csv'
# load data into pandas dataframe
df = loadData(path)
# get demorgraphic data
df = getDemographics(df)
#preprocess data - change dtypes to category
data = preprocess(df)