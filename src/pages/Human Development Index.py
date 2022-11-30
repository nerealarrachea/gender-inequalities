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


st.header("Impact of HDI in gender inequality")


#heat = viz.heat(df_heatmap)
#st.pyplot(heat)

fig = viz.scatter(df, df['Gender Inequality Index (Value)'], df['Life expectancy at birth (F)'], df['Region'], 
           "Does gender inequality impact a countries HDI?<br><sup>Looking into Life expectancy</sup>")
st.plotly_chart(fig, use_container_width=True)


fig2 = viz.scatter(df, df['Gender Inequality Index (Value)'], df['Expected years of schooling (F)'], df['Region'], 
            "Does gender inequality impact a countries HDI?<br><sup>Looking into level of education</sup>")
st.plotly_chart(fig2, use_container_width=True)

fig3 = viz.scatter(df, df['Gender Inequality Index (Value)'], df['Estimated  gross national income per capita (F)'], 
                    df['Region'], 
                    "Does gender inequality impact a countries HDI?<br><sup>Looking into GDP per capita</sup>")
st.plotly_chart(fig3, use_container_width=True)





