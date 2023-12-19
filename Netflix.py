import pandas as pd
import numpy as np
import os 
import matplotlib.pylab as plt
import plotly

path = os.getcwd()
print(path)

#lets list the files
files = os.listdir()
print(files)

#Lets load the data
df = pd.read_csv('netflix_titles.csv')
df.shape
df.head(100)
df.columns

#Lets check for nulls 
df.isna().sum()


#Lets see if Netflix focus more in Series or in Movies
df.value_counts('type')

#Lets plot the count of movies and TV shows
df['type'].value_counts().plot(kind='bar', title = 'Type of Shows on Netflix')

##Extract the top 10 directors by number of movies made from the dataset.
df.loc[df['type'] == 'Movie', 'director'].value_counts().reset_index().head(10)

df.type.unique()
df.loc[df['type'] == 'Movie','director'].value_counts().reset_index().head(10)

##https://www.kaggle.com/code/byteliberator/eda-of-netflix-dataset


#Lets check per country
##lest see how many countries are they
df.country.nunique()


Movies_per_country = df.loc[df['type'] == 'Movie','country'].value_counts().reset_index().head(10)
#Lets plot

Movies_per_country.plot(kind='bar',  y= 'count', x= 'country', title= 'Movies per Country')

#Lets see when the movies were release
movies_per_year = df.loc[df['type']=='Movie','release_year'].value_counts().reset_index()
movies_per_year.dtypes

# Filter the DataFrame for the last 10 years from now
last_10_years = movies_per_year[movies_per_year['release_year']>= pd.to_datetime('today').year -10]  
last_10_years
last_10_years['count'].sum()
#What is the tv show with maximum duration/seasons?
df.loc[df['type']== 'TV Show', ['duration']].value_counts().reset_index()
df.loc[df['duration']== '17 Seasons']


#How many movies were produced in the last 10 years?
df.loc[(df['type']== 'Movie') & (df['release_year']>2013)].shape[0]

#What is the most popular rating in TV shows?
df.loc[df['type']=='TV Show','rating'].value_counts().reset_index()

# In which year were the most Adult rated movies produced?
df.columns
Adult_movie = df.loc[(df['type'] == 'Movie')   & (df['rating'] == 'TV-MA' )]
Adult_movie.loc[:,'release_year'].value_counts().reset_index()


# Who is the most popular movie director from India?
Popular_director = df.loc[(df['type'] == 'Movie') & (df['country'] == 'India')]
Popular_director.loc[:,'director'].value_counts().reset_index()

#Which movie is the smallest movie ever made?
Smallest_movie = df.loc[(df['type'] =='Movie') & (df['duration'] =='8 min')]
Smallest_movie.reset_index()


#Did 2020 see any new TV shows being released? True/False?
df['type'].unique()
New_tv_shows_2020 = df.loc[(df['type'] == 'TV Show') & (df['release_year'] == 2020)]
New_tv_shows_2020.loc[:,'release_year'].value_counts().reset_index()

#How many categories of ratings exist?
category_of_rantings = df['rating'].nunique()

#Lets explore the USA market, Does United States make more movies or tv shows?
USA_market_Movies = df.loc[(df['country'] == 'United States') &  (df['type'] == 'Movie'),'title'].nunique()
USA_market_Movies

USA_market_TV_shows = df.loc[(df['country'] == 'United States') &  (df['type'] == 'TV Show'),'title'].nunique()
USA_market_TV_shows

USA_market = df.loc[(df['country'] == 'United States') ]

#Lets create a plot
USA_market['type'].value_counts().plot(kind='bar', title = 'TV Shows or Movie in USA')
