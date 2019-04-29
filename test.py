import pandas as pd
import os
import numpy
import matplotlib.pyplot as plt
import seaborn as sns
import json

def load_tmdb_movies(path):
    df = pd.read_csv(path)
    df['release_date'] = pd.to_datetime(df['release_date']).apply(lambda x: x.date())
    json_columns = ['genres', 'keywords', 'production_countries', 'production_companies', 'spoken_languages']
    for column in json_columns:
        df[column] = df[column].apply(json.loads)
    return df

print(load_tmdb_movies("train.csv"))