import numpy as np # linear algebra
import pandas as pd # for data preparation
import plotly.express as px # for data visualization
from textblob import TextBlob # for sentiment analysis

dff = pd.read_csv('netflix_titles.csv')
print(dff.shape)
print(dff.columns)
# ()