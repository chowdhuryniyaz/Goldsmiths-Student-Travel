import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pandas.api.types import CategoricalDtype

def loadData(path):
    """
    Load the data into a Pandas DataFrame. 
    Skip the first row (header) and rename the columns 
    Args:
        path: String path to dataset.
    Returns:
        df: Data as a Pandas DataFrame.
    """
    colnames = ['timestamp', 'postcode', 'accommodation_type', 'avg_journey_time', 
    'arr_monday', 'arr_tuesday', 'arr_wednesday', 'arr_thursday', 'arr_friday', 
    'dep_monday', 'dep_tuesday', 'dep_wednesday', 'dep_thursday', 'dep_friday', 'mode_of_transport',
    'why_public_transport', 'modes_pt', 'station', 'ticket_type',
    'why_motor_vehicle', 'driver_or_passenger', 'park_vehicle', 'consider_changes', 
    'why_walk', 'route', 'pedestrian_crossings', 'congested_route', 'walk_alone', 'well_maintained_pavements', 
    'litter_on_route', 'lighting_at_night', 'pavements_not_wide', 'feel_safe_walking', 
    'why_cycle', 'park_bike', 'bike_safety', 'feel_safe_cycling',
    'why_other', 
    'age', 'gender', 'level_of_study', 'year_of_study', 'region']
    
    df = pd.read_csv(path, names=colnames, header=None, skiprows=1, index_col=False)

    return df

def convertDataType(df):
    """
    Convert column data types to categorical
    Args:
        df: Dataset as a Pandas DataFrame.
    Returns:
        df: Data as a Pandas DataFrame, column data types converted to categorical
    """
    # set data type of postcode column as nominal
    postcode_type = CategoricalDtype(ordered=False, categories=['SE14', 'E14', 'NW4', 'SE8', 'N8', 'E4', 'NW1', 
    'other', 'E3', 'SE1', 'SW2', 'E10', 'N15', 'E2', 'SE18', 'N1', 'EC2', 'SE4', 'I would prefer not to say'])
    df['postcode'] = df['postcode'].map({'SE14 New Cross': 'SE14', 'Other': 'other', 'E14 Poplar': 'E14',
    'I would prefer not to say': 'I would prefer not to say', 'NW4 Hendon': 'NW4', 'SE8 Deptford': 'SE8', 'N8 Hornsey': 'N8',
    'E4 Chingford': 'E4', 'NW1 Head district': 'NW1', 'E3 Bow': 'E3', 'SE1 Head district': 'SE1', 
    'SW2 Brixton': 'SW2', 'E10 Leyton': 'E10', 'N15 South Tottenham': 'N15', 'E2 Bethnal Green': 'E2',
    'SE18 Woolwich': 'SE18', 'N1 Head district': 'N1', 'EC2 Bishopsgate': 'EC2', 'SE4 Brockley': 'SE4'}).astype(postcode_type)

    # set data type of accomodation_type column as nominal
    accommodation_types = CategoricalDtype(ordered=False, categories=['Rent', 'Own home', 'Halls of residence', 'With parents', 'other'])
    df['accommodation_type'] = df['accommodation_type'].map({'Living with parents/guardians during term time': 'With parents', 
    'Shared rental accomodation': 'Rent', 
    'Your own permanent residence (either owned or rented)': 'Own home',
    'Goldsmiths halls of residence': 'Halls of residence',
    'I would prefer not to say': 'other', np.NaN: 'other'}).astype(accommodation_types)

    # set data type of avg_journey_time column as ordinal
    journey_time_type = CategoricalDtype(ordered=True, categories=['Less than 15 minutes', '15 - 30 minutes', '31 - 45 minutes',
    '46 - 60 minutes', 'More than 60 minutes'])
    df['avg_journey_time'] = df['avg_journey_time'].astype(journey_time_type)

    # set data type of arrival time columns as ordinal
    arrival_time_type = CategoricalDtype(ordered=True, categories=['Before 08:00', '08:00 - 10:00', '10:01 - 12:00', 
    '12:01 - 14:00', '14:01 - 16:00', 'After 16:01', 'Did not come to Goldsmiths this day'])
    for col in ['arr_monday', 'arr_tuesday', 'arr_wednesday', 'arr_thursday', 'arr_friday']:
        df[col] = df[col].astype(arrival_time_type)
    
    # set data type of departure time columns as ordinal
    departure_time_type = CategoricalDtype(ordered=True, categories=['Before 12:00', '12:00 - 14:00', '14:01 - 16:00',
    '16:01 - 18:00', '18:01 - 20:00', 'After 20:01', 'Did not come to Goldsmiths this day'])
    for col in ['dep_monday', 'dep_tuesday', 'dep_wednesday', 'dep_thursday', 'dep_friday']:
        df[col] = df[col].astype(departure_time_type)
    
    # set data type for mode of transport as ordinal
    mode_type = CategoricalDtype(ordered=False, categories=['public transport', 'walking', 'motor vehicle', 'bicycle', 'other'])
    df['mode_of_transport'] = df['mode_of_transport'].map({'Public transport':'public transport', 'On foot': 'walking', 'Motor vehicle (car or motorcycle/scooter)':'motor vehicle', 'Bicycle':'bicycle', np.NaN:'other'}).astype(mode_type)

    # set data type of age column as ordinal (ordered categorical)
    age_type = CategoricalDtype(ordered=True, categories=['18 - 21', '22 - 25', '26 - 30', '31 - 40', 'Over 40', 'I would prefer not to say'])
    df['age'] = df['age'].astype(age_type)
    
    # set data type of gender column as nominal
    gender_cat = pd.unique(df.gender.values.ravel())
    gender_type = CategoricalDtype(ordered=False, categories=gender_cat)
    df['gender'] = df['gender'].astype(gender_type)

    # set data type of region column as nominal
    region_type = CategoricalDtype(ordered=False, categories=['UK', 'EU', 'overseas', 'other'])
    df['region'] = df['region'].apply(regionHelper).astype(region_type)

    # set data type of level of study as nominal
    level_of_study_type = CategoricalDtype(ordered=False, categories=['FT undergraduate', 'FT postgraduate', 'Foundation','PT undergraduate', 'PT postgraduate', 'not sure'])
    df['level_of_study'] = df['level_of_study'].apply(levelOfStudyHelper).astype(level_of_study_type)

    # create mode_of_study column to separate FT/PT students
    mode_of_study_type = CategoricalDtype(ordered=False, categories=['full time', 'part time', 'other'])
    df['mode_of_study'] = df['level_of_study'].map({'FT undergraduate': 'full time', 'FT postgraduate': 'full time', 'Foundation': 'full time', 'PT undergraduate': 'part time', 'PT postgraduate': 'part time', 'not sure': 'other'}).astype(mode_of_study_type)
    
    # set ordinal level of study category (foundation<undergrad<postgrad)
    level_type = CategoricalDtype(ordered=True, categories=['foundation','undergraduate', 'postgraduate', 'other'])
    df['level'] = df['level_of_study'].map({'FT undergraduate': 'undergraduate', 'FT postgraduate': 'postgraduate', 'Foundation': 'foundation', 'PT undergraduate': 'undergraduate', 'PT postgraduate': 'postgraduate', 'not sure': 'other'}).astype(level_type)
    
    # set data type of year of study column as ordinal
    year_of_study_type = CategoricalDtype(ordered=True, categories=['0', '1', '2', '3', '3+', 'other'])
    df['year_of_study'] = df['year_of_study'].map({'0 (Foundation only)': '0', '1 (UG)': '1', '2 (UG)': '2', '3 (UG)': '3', '3+': '3+', np.NaN: 'other'}).astype(year_of_study_type)

    return df

# assign easier to type values in region column
def regionHelper(x):
    """
    Convert column data types to categorical
    Args:
        x: string - value in a column
    Returns:
        x: modified string
    """
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

def getDemographics(df):
    """
    Get demographics section only
    Args:
        df: Pandas DataFrame
    Returns:
        demographics_df: Demographic data as a Pandas DataFrame.
    """
    demographics_df = df.loc[:, ['age', 'gender', 'level_of_study', 'year_of_study', 'region']]
    return demographics_df

def getSection1(df):
    """
    Get the first section only, containing general questions
    Args:
        df: Pandas DataFrame
    Returns:
        section1_df: Demographic data as a Pandas DataFrame.
    """
    section1_df = df.loc[:, ['postcode', 'accommodation_type', 'avg_journey_time', 
    'arr_monday', 'arr_tuesday', 'arr_wednesday', 'arr_thursday', 'arr_friday', 
    'dep_monday', 'dep_tuesday', 'dep_wednesday', 'dep_thursday', 'dep_friday', 'mode_of_transport']]
    
    return section1_df

