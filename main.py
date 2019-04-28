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
Only id, budget, popularity, runtime, revenue belong to integer, so that's why it only has five columns here
1. All of them have 3000 rows, except the runtime (2998) - maybe drop the data with no runtime?
2. Budget: some movies have no budget (0) - need to examine the number later
3. Popularity: most numbers is around 0-10, but there are probably some outliners here
4. runtime: few movies show 0 or null(2) on runtime, it will need to be examined
5. revenue:  the range is quite wide, and it can be from 1 to more than 1000000000. some numbers show 1 may need to be exclded here
'''
# filter the budget = 0
df_budget_zero = df.query('budget == 0')
df_budget_zero.to_csv('movies_budget_zero.csv')
print(df_budget_zero.head())

'''
1. some movies actually has budget e.g. Police Academy 2: Their First Assignment (id = 171), so there may be some data missing here
2. need to check how many movies have no budget value 
'''

# calculate how many rows which has 0 budget
df_budget_0count  = df.groupby('budget').count()['id']
print(df_budget_0count.head())

'''
- 812 movies have budget = 0, so these numbers have to be kept
'''

