import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import sys
sys.path.append('/.../viz.py') 
sys.path.append('/.../cleaning.py') 
import viz
import plotly.express as px 

st.set_page_config(
     page_title="HDI and Gender",
     page_icon="🚀",
     layout="wide",
)

df = pd.read_csv("/Users/narea/Desktop/ironhack/project/final-project/data/gender_gap.csv")


st.header("Impact of gender inequality on HDI")
st.markdown('''
I wanted to see if countries that are more unequal towards woman have a lower Human Development than those that are more equal. For that purpose
I explored the correlation between the 3 indicators that measure HDI and the Gender Inequality Index.''')

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

st.subheader("Bonus")

st.markdown('''
I already had the correlation of GII with health, economics and education. I wanted to do an extra one to see its relationship
with politics, so I did the next scatterplot to show the correlation between the share of seats in parliament that women occupy 
and GII. Something really interesting we can see, is that Rwanda is the top country with more women on the pairlament, this is due 
to the change on demographics the country had after a genocide that took place in 1994. (you can learn more about it here:
https://www.inclusivesecurity.org/how-women-rebuilt-rwanda/)''')

fig4 = viz.scatter(df, df['Gender Inequality Index (Value)'], df["Share of seats in parliament"], 
                    df['Region'], 
                    "Does gender inequality impact a country's HDI?<br><sup>Looking into GDP per capita</sup>")
st.plotly_chart(fig4, use_container_width=True)




