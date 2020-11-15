# %%
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px


# %%
df=pd.read_csv('fatal-police-shootings-data.csv')

# %%
df.head()

# %%
df.info()

# %%
"""
deleting some columns
"""

# %%
df=df.drop(["signs_of_mental_illness","threat_level","flee","body_camera"], axis=1)

# %%
df.info()

# %%
"""
data grouping by moths and years
"""

# %%
df['month']=pd.to_datetime(df['date']).dt.month
df['year']=pd.to_datetime(df['date']).dt.year

# %%
df.info()

# %%
df=df.drop(columns='date')

# %%
df.info()

# %%
"""
NA handling
"""

# %%
df.race.unique()

# %%
df=df.dropna(axis=0, subset=['race'])

# %%
df.info()

# %%
df=df.dropna(axis=0, subset=['armed'])

# %%
df.info()

# %%


# %%
round(df[['age']].mean(axis=0, skipna=True),0)

# %%
df["age"].fillna(round(df[['age']].mean(axis=0, skipna=True),0),inplace=True)

# %%
df.info()

# %%
df=df.dropna(axis=0, subset=['gender'])

# %%
df.info()

# %%

fig = sns.catplot(x="race", 
            data=df, 
            aspect=2.5, 
            kind='count')


# %%
sns.catplot(x="race", 
            data=df[df['gender']=='M'], 
            order=df['race'].value_counts().index,
            kind='count')


# %%
sns.catplot(x="race", 
            data=df[df['gender']=='F'],
            kind='count',
           order=df['race'].value_counts().index,)

# %%
stany=df['state'].value_counts()
stany=stany.to_frame()
stany.reset_index(level=0, inplace=True)
stany.head()
stany=stany.rename(columns={'index': 'stan', 'state': 'ilosc'})
stany.info()
stany.head()

# %%


fig = px.choropleth(stany,
                    locations="stan",
                    color='ilosc',
                    hover_name="ilosc",
                    locationmode = 'USA-states')
fig.show()


