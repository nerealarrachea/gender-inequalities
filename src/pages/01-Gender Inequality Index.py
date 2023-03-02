import streamlit as st
import streamlit.components.v1 as components
from datetime import date
import pandas as pd
import pickle
from PIL import Image
import viz 
import plotly.express as px


df = pd.read_csv("data/gender_gap.csv")
sec = pd.read_csv("data/industry_sectors.csv")

st.set_page_config(
     page_title="Gender inequality",
     page_icon="🚀",
     layout="wide",
)

# Title
st.title("Gender Inequality Index (GII)")
st.subheader("Around the world")
st.markdown('''
GII is a composite metric of gender inequality using four dimensions: Economic Participation and Opportunity, Educational Attainment, Health and Survival (including reproductive health) and
Political Empowerment. A low GII value indicates low inequality between women and men, and vice-versa.
''')

fig3 = viz.map(df,df["Gender Inequality Index (Rank)"], "GII by country", "Viridis")
st.plotly_chart(fig3, use_container_width=True)

df3 = df.nsmallest(10, 'Gender Inequality Index (Value)')
df2 = df.nlargest(10, 'Gender Inequality Index (Value)')
df3 = df3[["Country", "Gender Inequality Index (Value)"]]
df2 = df2[["Country", "Gender Inequality Index (Value)"]]


col1, col2 = st.columns(2)
col1.markdown("### Most equal countries")
col1.dataframe(df3)

col2.markdown("### Most unequal countries")
col2.dataframe(df2)

#st.dataframe(df2)

#st.dataframe(df3)
