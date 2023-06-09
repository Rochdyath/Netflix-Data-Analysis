import numpy as np # linear algebra
import pandas as pd # for data preparation
import plotly.express as px # for data visualization
from textblob import TextBlob # for sentiment analysis

dff = pd.read_csv('netflix_titles.csv')

def distribution_of_content_ratings():
    z = dff.groupby(['rating']).size().reset_index(name='counts')
    pieChart = px.pie(z, values='counts', names='rating',
                    title='Distribution of Content Ratings on Netflix',
                    color_discrete_sequence=px.colors.qualitative.Set3)
    pieChart.show()

def top_5_directors():
    filtered_cast=dff['director'].str.split(',',expand=True).stack()
    filtered_cast=filtered_cast.to_frame()
    filtered_cast.columns=['director']
    z = filtered_cast.groupby(['director']).size().reset_index(name='counts')
    z = z.sort_values(by = 'counts', ascending = True)
    top5 = z.tail(5)
    fig = px.bar(top5, x='counts', y='director', title='Top 5 Directors on Netflix')
    fig.show()

def top_5_actors():
    filtered_cast=dff['cast'].str.split(',',expand=True).stack()
    filtered_cast=filtered_cast.to_frame()
    filtered_cast.columns=['actor']
    z = filtered_cast.groupby(['actor']).size().reset_index(name='counts')
    z = z.sort_values(by = 'counts', ascending = True)
    top5 = z.tail(5)
    fig = px.bar(top5, x='counts', y='actor', title='Top 5 Actors on Netflix')
    fig.show()

def trend_production():
    dfx = dff[['type','release_year']]
    dfx = dfx.groupby(['release_year','type']).size().reset_index(name='counts')
    dfx = dfx[dfx['release_year']>=2010]
    dfx = dfx.rename(columns={"release_year": "Release Year"})
    fig = px.line(dfx, x="Release Year", y="counts", color='type',title='Trend of content produced over the years on Netflix')
    fig.show()

def sentiment_of_content():
    dfx=dff[['release_year','description']]
    feels = []
    for _,row in dfx.iterrows():
        testimonial = TextBlob(row['description'])
        p = testimonial.sentiment.polarity
        if p == 0:
            sent = 'Neutral'
        elif p > 0:
            sent = 'Positive'
        else:
            sent = 'Negative'
        feels.append(sent)
    dfx['Sentiment'] = feels
    dfx=dfx.groupby(['release_year','Sentiment']).size().reset_index(name='counts')
    dfx = dfx[dfx['release_year']>=2010]
    dfx = dfx.rename(columns={"release_year": "Release Year"})
    fig = px.line(dfx, x="Release Year", y="counts", color='Sentiment',title='Sentiment of content on Netflix')
    fig.show()
    # fig = px.bar(dfx, x="Release Year", y="counts", color="Sentiment", title="Sentiment of content on Netflix")
    # fig.show()