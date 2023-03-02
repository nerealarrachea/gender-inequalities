import streamlit as st
import pandas as pd
import sys
sys.path.append('/.../viz.py') 
import viz
import plotly.express as px 


st.set_page_config(
     page_title="Gender wage gap",
     page_icon="🚀",
     layout="wide",
)

df = pd.read_csv("data/gender_gap.csv")
sec = pd.read_csv("pages/data/industry_sectors.csv")

st.header("Do women really get a lower salary for the same job?")

st.markdown('''


''')

fig = viz.map(df,df["Mandatory equal remuneration by law"], "Mandatory equal remuneration by law", "Cividis")
st.plotly_chart(fig, use_container_width=True)

st.subheader("Calculating the gender wage gap by industry")

# Selection box
 
# first argument takes the titleof the selectionbox
# second argument takes options
job = st.selectbox("Job Title: ",
                     ['Total, full-time wage and salary workers',
 'Management, professional, and related occupations',
 'Management, business, and financial operations occupations',
 'Management occupations',
 'Chief executives',
 'General and operations managers',
 'Marketing managers',
 'Sales managers',
 'Computer and information systems managers',
 'Financial managers',
 'Purchasing managers',
 'Transportation, storage, and distribution managers',
 'Construction managers',
 'Education and childcare administrators',
 'Food service managers',
 'Medical and health services managers',
 'Property, real estate, and community association managers',
 'Social and community service managers',
 'Managers, all other',
 'Business and financial operations occupations',
 'Wholesale and retail buyers, except farm products',
 'Purchasing agents, except wholesale, retail, and farm products',
 'Claims adjusters, appraisers, examiners, and investigators',
 'Compliance officers',
 'Human resources workers',
 'Training and development specialists',
 'Project management specialists',
 'Management analysts',
 'Market research analysts and marketing specialists',
 'Business operations specialists, all other',
 'Accountants and auditors',
 'Financial and investment analysts',
 'Personal financial advisors',
 'Credit counselors and loan officers',
 'Professional and related occupations',
 'Computer and mathematical occupations',
 'Computer systems analysts',
 'Computer programmers',
 'Software developers',
 'Computer support specialists',
 'Computer occupations, all other',
 'Operations research analysts',
 'Other mathematical science occupations',
 'Architecture and engineering occupations',
 'Civil engineers',
 'Industrial engineers, including health and safety',
 'Engineers, all other',
 'Other engineering technologists and technicians, except drafters',
 'Life, physical, and social science occupations',
 'Medical scientists',
 'Physical scientists, all other',
 'Other life, physical, and social science technicians',
 'Community and social service occupations',
 'Educational, guidance, and career counselors and advisors',
 'Counselors, all other',
 'Social workers, all other',
 'Legal occupations',
 'Lawyers',
 'Paralegals and legal assistants',
 'Education, training, and library occupations',
 'Postsecondary teachers',
 'Elementary and middle school teachers',
 'Secondary school teachers',
 'Special education teachers',
 'Other teachers and instructors',
 'Teaching assistants',
 'Arts, design, entertainment, sports, and media occupations',
 'Graphic designers',
 'Other designers',
 'Producers and directors',
 'Healthcare practitioners and technical occupations',
 'Pharmacists',
 'Other physicians',
 'Physical therapists',
 'Registered nurses',
 'Clinical laboratory technologists and technicians',
 'Radiologic technologists and technicians',
 'Pharmacy technicians',
 'Miscellaneous health technologists and technicians',
 'Service occupations',
 'Healthcare support occupations',
 'Personal care aides',
 'Nursing assistants',
 'Medical assistants',
 'Protective service occupations',
 'Correctional officers and jailers',
 'Police officers',
 'Security guards and gambling surveillance officers',
 'Food preparation and serving related occupations',
 'Chefs and head cooks',
 'First-line supervisors of food preparation and serving workers',
 'Cooks',
 'Food preparation workers',
 'Bartenders',
 'Fast food and counter workers',
 'Waiters and waitresses',
 'Dining room and cafeteria attendants and bartender helpers',
 'Building and grounds cleaning and maintenance occupations',
 'First-line supervisors of housekeeping and janitorial workers',
 'Janitors and building cleaners',
 'Maids and housekeeping cleaners',
 'Personal care and service occupations',
 'Sales and office occupations',
 'Sales and related occupations',
 'First-line supervisors of retail sales workers',
 'First-line supervisors of non-retail sales workers',
 'Cashiers',
 'Retail salespersons',
 'Insurance sales agents',
 'Securities, commodities, and financial services sales agents',
 'Sales representatives of services, except advertising, insurance, financial services, and travel',
 'Sales representatives, wholesale and manufacturing',
 'Real estate brokers and sales agents',
 'Sales and related workers, all other',
 'Office and administrative support occupations',
 'First-line supervisors of office and administrative support workers',
 'Billing and posting clerks',
 'Bookkeeping, accounting, and auditing clerks',
 'Customer service representatives',
 'Receptionists and information clerks',
 'Couriers and messengers',
 'Dispatchers, except police, fire, and ambulance',
 'Postal service mail carriers',
 'Production, planning, and expediting clerks',
 'Shipping, receiving, and inventory clerks',
 'Secretaries and administrative assistants, except legal, medical, and executive',
 'Insurance claims and policy processing clerks',
 'Office clerks, general',
 'Office and administrative support workers, all other',
 'Natural resources, construction, and maintenance occupations',
 'Farming, fishing, and forestry occupations',
 'Miscellaneous agricultural workers',
 'Construction and extraction occupations',
 'Installation, maintenance, and repair occupations',
 'Production, transportation, and material moving occupations',
 'Production occupations',
 'First-line supervisors of production and operating workers',
 'Other assemblers and fabricators',
 'Bakers',
 'Food processing workers, all other',
 'Other metal workers and plastic workers',
 'Inspectors, testers, sorters, samplers, and weighers',
 'Packaging and filling machine operators and tenders',
 'Other production workers',
 'Transportation and material moving occupations',
 'Supervisors of transportation and material moving workers',
 'Bus drivers, school',
 'Bus drivers, transit and intercity',
 'Driver/sales workers and truck drivers',
 'Industrial truck and tractor operators',
 'Laborers and freight, stock, and material movers, hand',
 'Packers and packagers, hand',
 'Stockers and order fillers'], key='sel_key')
 

#industry = job["Dollars per cents"]
# print the selected job with the salary 
cents = sec[sec["Occupation"]==job]["Cents per dollar"]
annual = sec[sec["Occupation"]==job]["Annual Difference"]
monthly = sec[sec["Occupation"]==job]["Wage Difference"]

lst = cents.tolist()
lst2 = monthly.tolist()
lst3 = annual.tolist()


st.subheader(f"Women who work as {job} win {lst[0]} cents per every dollar a man earns.")

st.subheader(f"That means that they earn {lst2[0]} dollars less every week, which means they get {lst3[0]} dollars less every year for the same job 🤯")

st.markdown('''

''')
sec2 = sec[['Occupation','Cents per dollar']]
st.dataframe(sec2)