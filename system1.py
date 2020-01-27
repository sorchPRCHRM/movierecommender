import numpy as np
import pandas as pd


column_names=['user_id' ,'item_id' ,'rating', 'span']
df=pd.read_csv('moviedata.csv' ,names= column_names )

df=pd.DataFrame(df)
#print(df)
# movie_names=['item_id' , 'title']
Movie=pd.read_csv('Movie_Id_Title.csv')
Movie=pd.DataFrame(Movie)
#print(Movie.head())
df=pd.merge(df ,Movie ,on='item_id')
# print(df)
df2=df.groupby('title')['rating'].mean().sort_values(ascending=False)
# print(df2.head(100))
# print(df.groupby('title')['rating'] .count().sort_values(ascending=False))
df = df.groupby('title')['rating'].count().sort_values(ascending=False)
# print(df)
def weighted_rating(df, m=m, C=C):
    v =  df['vote_count']
    R = x['vote_average']
    # Calculation based on the IMDB formula
    return (v/(v+m) * R) + (m/(m+v) * C)
# df['score'] =
print(df2.sum)