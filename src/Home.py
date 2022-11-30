import streamlit as st
import streamlit.components.v1 as components
from datetime import date
import pandas as pd
import pickle
from PIL import Image
import viz 
import seaborn as sns
import plotly.express as px


df = pd.read_csv("/Users/narea/Desktop/ironhack/project/final-project/data/gender_gap.csv")
sec = pd.read_csv("/Users/narea/Desktop/ironhack/project/final-project/data/industry_sectors.csv")


st.set_page_config(
     page_title="Gender inequality",
     page_icon="🚀",
     layout="wide",
)


# Title
st.title("Exploring gender inequlity around the 🌎")
st.subheader("1. Data")
# Display Images
 
# import Image from pillow to open images
# img = Image.open("/Users/narea/Desktop/ironhack/project/final-project/images/basket.png")
 
# display image using streamlit
# width is used to set the width of an image
# st.image(img, width=200)

#st.markdown(
#"""
#### The following list won't indent no matter what I try:
#- Item 1
# Item 2
#- Item 3
#"""
#)
