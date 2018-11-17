import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import urllib.request
import json
from textwrap import wrap
from loadData import loadData, convertDataType
import googlemaps
from pandas.api.types import CategoricalDtype


def preprocess(df):

    key = 'AIzaSyCPW_wydntgl4BMzn5gqufzJplcCCawdlQ'

    # create a new dataframe by copying a few specific columns from the original dataframe
    #list indexing with .loc always returns a copy
    df1 = df.loc[:, ['postcode', 'avg_journey_time', 'mode_of_transport']]

    # respondents who refused an answer are not included in the analysis 
    df1 = df1[df1['mode_of_transport'] != 'other']

    # drop rows where NaN appears
    df1 = df1.dropna()

    #reset the index and avoid the old index being added as a column
    df1 = df1.reset_index(drop=True)

    #create googlemaps client
    gmaps = googlemaps.Client(key=key)

    # save the postcodes and mode of travel to a list
    postcodes = df1.postcode.tolist()
    modes = df1.mode_of_transport.tolist()

    # create lsit to save distances
    distance = []
    # for each postcode, mode pair calculate the distance from Goldsmiths
    for postcode, mode in zip(postcodes,modes):
        if postcode == 'other':
            result = np.NaN
            distance.append(result)
        else:
            # pass origin and destination variables to distance_matrix function
            # output in meters
            result = gmaps.distance_matrix('London {}'.format(postcode), 'SE14 6LS', mode=mode)["rows"][0]["elements"][0]["distance"]["value"]
            distance.append(result)

    # add the calculated distances to our dataframe (distance in meters)
    df1['distance'] = distance

    # fill na with mean of distances
    df1['distance'].fillna((df1['distance'].mean()), inplace=True)

    # create distance_cat column for distance categories (ordinal)
    distance_type = CategoricalDtype(ordered=True, categories=['0 - <1 km', '1-1.99 km', '2-4.99 km',
        '5-9.99 km', 'More than 10 km'])

    #convert distance values (in meters) to categories (distance range)
    df1['distance_cat'] = df1['distance']
    df1['distance_cat'] = df1['distance_cat'].apply(distanceHelper).astype(distance_type)

    # save preprocessed data 
    df1.to_csv('./data/distance_data.csv')

# to place values in appropriate distance range category
def distanceHelper(x):
    if x < 1000:
        return '0 - <1 km'
    elif x < 2000:
        return '1-1.99 km'
    elif x < 5000:
        return '2-4.99 km'
    elif x < 10000:
        return '5-9.99 km'
    else:
        return 'More than 10 km'

# load preprocessed data
