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

df = pd.read_csv("gender_gap.csv")
sec = pd.read_csv("pages/data/industry_sectors.csv")

st.header("How does motherhood affect the gender gap?")
st.markdown('''
In the following tables we can see what citizen's from different countries think about working mothers with children 
under school age and on school age. This data was taken from the **International Social Survey Programme: Family and 
Changing Gender Roles** that's made by the **Leibniz Institute for the Social Science** and covers the opinion of different
people from different countries on family and gender 
related topics. 
''')

not_at_school= cl.not_school()
at_school= cl.school()

fig = viz.bar(not_at_school, "Do you think that women should work outside the home full-time, part-time or not at all? <br><sup>With children under school age</sup>")
st.plotly_chart(fig, use_container_width=True)

fig2 = viz.bar(at_school, "Do you think that women should work outside the home full-time, part-time or not at all? <br><sup>With children on school age</sup>")
st.plotly_chart(fig2, use_container_width=True)


#st.subheader("Hours spent on domestic labour by women")
#st.markdown('''
##### In the following graph we can see the amount of time women spend on domestic labour and their participation on the work force.
#''')

def main():
    html_ = """<div class='tableauPlaceholder' id='viz1669733320904' style='position: relative'>
    <noscript><a href='#'><img alt='Unpaid domestic labour by women and the effect on paid labour ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Un&#47;Unpaiddomesticlabour&#47;Hoja1&#47;1_rss.png' style='border: none' />
    </a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' />
     <param name='embed_code_version' value='3' /> <param name='site_root' value='' />
     <param name='name' value='Unpaiddomesticlabour&#47;Hoja1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' />
     <param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Un&#47;Unpaiddomesticlabour&#47;Hoja1&#47;1.png' /> 
     <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' />
     <param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='es-ES' /><param name='filter' value='publish=yes' />
     </object></div>                
     <script type='text/javascript'>                    
     var divElement = document.getElementById('viz1669733320904');                    
     var vizElement = divElement.getElementsByTagName('object')[0];                    
     vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    
     var scriptElement = document.createElement('script');                    
     scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    
     vizElement.parentNode.insertBefore(scriptElement, vizElement);                
     </script>"""
    components.html(html_, height=760)

#if __name__ == "__main__":    
#    main()


