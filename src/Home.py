import streamlit as st
import streamlit.components.v1 as components
from datetime import date
import pandas as pd
import pickle
from PIL import Image
import viz 
import plotly.express as px


df = pd.read_csv("final-project/data/gender_gap.csv")
sec = pd.read_csv("./pages/data/industry_sectors.csv")

st.set_page_config(
     page_title="Gender inequality",
     page_icon="🚀",
     layout="wide",
)


# Title
st.title("Exploring gender inequality around the 🌎")
st.subheader("Data")
st.markdown('''
I created a dataframe with data from different sites, such as: **The World Bank, The OECD, United Nations Development Programme (UNDP), ILOSTAT and The World Economic Forum.** 
You can explore it here and look for different interesting parameters on gender gap for more than 180 countries in the world.
''')

st.dataframe(df)


