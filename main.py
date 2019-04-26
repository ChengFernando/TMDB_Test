# all key library
import os
import pandas as pd
import numpy
import matplotlib.pyplot as plt
import seaborn


# pandas full display settings, this display can show all data and not be omitted by default

# pd.options.display.max_columns = 50  # None -> No Restrictions
# pd.options.display.max_rows = 200    # None -> Be careful with this
# pd.options.display.max_colwidth = 100
# pd.options.display.precision = 3

# list the top 5 rows of the raw data
df = pd.read_csv('train.csv')
print(df.head())

df.info()
'''
Basic info about the data

Null v.s. Non-null data
1. 3000 entries and 23 columns

2.1 columns with null : belong to collection / homepage /  tagline
2.2 have few null columns: genres / overview / poster_path / production_companies / production_countries / runtime / spoken_language / keywords / cast / crew / 
'''

print(df.describe())
# details = df.describe().to_csv('details.csv')

'''
Only id, budget, popularity, runtime, revenue belong to integer, so that's why it only has five column here
1. All of them have 3000 rows, except the runtime (2998) - maybe drop 
2. 
'''

