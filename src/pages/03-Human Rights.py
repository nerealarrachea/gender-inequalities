import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import sys
sys.path.append('/.../viz.py') 
import viz
import seaborn as sns
import plotly.express as px 

# st.video('https://youtu.be/FVsvrFAWDTM') 

st.set_page_config(
     page_title="Human rights",
     page_icon="🚀",
     layout="wide",
)


sec = pd.read_csv("/Users/narea/Desktop/ironhack/project/final-project/data/industry_sectors.csv")
df = pd.read_csv("/Users/narea/Desktop/ironhack/project/final-project/data/gender_gap.csv")


st.header("Are women allowed to do the same as men?")

fig2 = viz.map(df,df["Equity in signing a contract"], "Equity in signing a contract", "Cividis")
st.plotly_chart(fig2, use_container_width=True)

fig3 = viz.map(df,df["WB&L: Parenthood Indicator"], "Facilities to be a mother and continue working", "Blues")
st.plotly_chart(fig3, use_container_width=True)

fig4 = viz.map(df,df["Requirement of obeying husband"], "Legal requirement of obeying your husband", "Cividis")
st.plotly_chart(fig4, use_container_width=True)
