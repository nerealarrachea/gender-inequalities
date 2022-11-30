import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import seaborn as sns
import plotly.express as px 
import sys
sys.path.append('/.../viz.py') 
sys.path.append('/.../cleaning.py') 
import viz
import cleaning as cl


st.set_page_config(
     page_title="Maternity & Inequality",
     page_icon="🚀",
     layout="wide",
)

sec = pd.read_csv("/Users/narea/Desktop/ironhack/project/final-project/data/industry_sectors.csv")
df = pd.read_csv("/Users/narea/Desktop/ironhack/project/final-project/data/gender_gap.csv")

not_at_school= cl.not_school()
at_school= cl.school()

fig = viz.bar(not_at_school, "Do you think that women should work outside the home full-time, part-time or not at all? <br><sup>With children under school age</sup>")
st.plotly_chart(fig, use_container_width=True)

fig2 = viz.bar(not_at_school, "Do you think that women should work outside the home full-time, part-time or not at all? <br><sup>With children on school age</sup>")
st.plotly_chart(fig2, use_container_width=True)

