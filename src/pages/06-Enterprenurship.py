import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import sys
sys.path.append('/.../viz.py') 
import plotly.express as px 



df = pd.read_csv("pages/data/gender_gap.csv")
sec = pd.read_csv("pages/data/industry_sectors.csv")
df1 = df.dropna(subset=['Share of woman inventors'])


st.set_page_config(
     page_title="Enterprenurship",
     page_icon="🚀",
     layout="wide",
)


# Title
st.title("How likely are women to own a business or create new products?")

fig = px.bar(df1, x = df1["Country"],y = df1["Share of woman inventors"], text_auto=True,
    title = "Percentage of women inventors per country",height=500) 
fig.update_layout(barmode='stack', xaxis={'categoryorder':'total descending'})
st.plotly_chart(fig, use_container_width=True)



