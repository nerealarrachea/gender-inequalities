import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import sys
sys.path.append('/.../viz.py') 
sys.path.append('/.../cleaning.py') 
import viz
import seaborn as sns
import plotly.express as px 

st.set_page_config(
     page_title="HDI and Gender",
     page_icon="🚀",
     layout="wide",
)

sec = pd.read_csv("/Users/narea/Desktop/ironhack/project/final-project/data/industry_sectors.csv")
df = pd.read_csv("/Users/narea/Desktop/ironhack/project/final-project/data/gender_gap.csv")


st.header("Impact of gender inequality on HDI")


#heat = viz.heat(df_heatmap)
#st.pyplot(heat)

st.subheader("1. Health: life expectancy at birth")

fig = viz.scatter(df, df['Gender Inequality Index (Value)'], df['Life expectancy at birth (M)'], df['Region'], 
           "Does gender inequality impact a country's HDI?<br><sup>Looking into Life expectancy</sup>")
st.plotly_chart(fig, use_container_width=True)

st.subheader("2. Education: expected years of schooling")

fig2 = viz.scatter(df, df['Gender Inequality Index (Value)'], df['Expected years of schooling (M)'], df['Region'], 
            "Does gender inequality impact a country's HDI?<br><sup>Looking into level of education</sup>")
st.plotly_chart(fig2, use_container_width=True)

st.subheader("3. Production: GNI per capita")

fig3 = viz.scatter(df, df['Gender Inequality Index (Value)'], df['Estimated  gross national income per capita (M)'], 
                    df['Region'], 
                    "Does gender inequality impact a country's HDI?<br><sup>Looking into GDP per capita</sup>")
st.plotly_chart(fig3, use_container_width=True)





