import numpy as np # linear algebra
import pandas as pd # for data preparation
import plotly.express as px # for data visualization
from textblob import TextBlob # for sentiment analysis

dff = pd.read_csv('netflix_titles.csv')
# print(dff.shape)
# print(dff.column)

def distribution_of_content_ratings():
    z = dff.groupby(['rating']).size().reset_index(name='counts')
    pieChart = px.pie(z, values='counts', names='rating', 
                    title='Distribution of Content Ratings on Netflix',
                    color_discrete_sequence=px.colors.qualitative.Set3)
    pieChart.show()

distribution_of_content_ratings()
