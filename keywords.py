import os
import pandas as pd
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

def load_tmdb_credits(path):
    df = pd.read_csv(path)
    json_columns = ['cast', 'crew']
    for column in json_columns:
        df[column] = df[column].apply(json.loads)
    return df

def pipe_flatten_names(keywords):
    return '|'.join([x['name'] for x in keywords])

credits = load_tmdb_credits("train.csv")
movies = load_tmdb_movies("train.csv")

print(credits)

del credits['title']
df = pd.concat([movies, credits], axis=1)

df['genres'] = df['genres'].apply(pipe_flatten_names)

liste_genres = set()
for s in df['genres'].str.split('|'):
    liste_genres = set().union(s, liste_genres)
liste_genres = list(liste_genres)
liste_genres.remove('')

# key part
df_reduced = df[['title','release_date','runtime','budget','revenue']].reset_index(drop=True)
for genre in liste_genres:
    df_reduced[genre] = df['genres'].str.contains(genre).apply(lambda x:1 if x else 0)
df_reduced[:5]

df_reduced.head()
