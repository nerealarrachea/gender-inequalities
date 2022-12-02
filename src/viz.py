import pandas as pd
import numpy as np
import plotly.express as px

# Viz
import plotly.express as px 
import matplotlib.pyplot as plt
sns.set_theme(style="white", palette="Spectral")


def map(df, color, title, tones):
    fig = px.choropleth(df, locations = df["Economy Code"], color= color,  hover_name = df['Country'], 
    color_continuous_scale=tones, title=title, height = 550)
    return fig

def scatter(df, x, y, color, title):
    fig = px.scatter(df, x = x, y = y, color = color, hover_name = df['Country'], height=500, width=1000, 
    trendline="ols", trendline_scope="overall", title= title)
    return fig

def heat(df):
    np.triu(np.ones_like(df.corr()))
    fig, ax = plt.subplots(figsize=(19,18))
    mask = np.triu(np.ones_like(df.corr(), dtype=bool))
    heatmap = sns.heatmap(df.corr(), mask=mask, vmin=-1, vmax=1, annot=True, fmt=".2f", linewidth=1, linecolor='w', square=True)
    heatmap.set_title('Correlation between different variables: gender gap', fontdict={'fontsize':14}, pad=16)
    return plt.show()

def bar(not_at_school, title):
    fig = px.bar(not_at_school, x='variable',y='value', color='Country', barmode="group", text_auto=True,
    title = title,
    labels={"variable": "",
    "value": "Population's opinion"}, height=500) 
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    return fig

