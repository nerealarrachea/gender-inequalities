
import pandas as pd
import numpy as np

# cleaning sectors
def sec(sector):
    sector['Median weekly earnings  (M)'] = sector['Median weekly earnings  (M)'].replace('–', np.nan)
    sector['Median weekly earnings (W)'] = sector['Median weekly earnings (W)'].replace('–', np.nan)
    sector['Median weekly earnings'] = sector['Median weekly earnings'].replace('–', np.nan)
    sector['Median weekly earnings  (M)'] = sector['Median weekly earnings  (M)'].astype(np.float64)
    sector['Median weekly earnings (W)'] = sector['Median weekly earnings (W)'].astype(np.float64)
    sector['Median weekly earnings'] = sector['Median weekly earnings'].astype(np.float64)
    sector = sector.set_index('Occupation')
    sector["Wage Difference"] = sector["Median weekly earnings  (M)"] - sector["Median weekly earnings (W)"]
    sector["Annual Difference"] = sector["Wage Difference"]*52
    sector["Cents per dollar"] = (sector["Median weekly earnings (W)"]/sector["Median weekly earnings  (M)"])*100
    sector["Cents per dollar"] = sector["Cents per dollar"].round(decimals=2)
    sector["Gender Gap"] = ((sector["Median weekly earnings  (M)"] - sector["Median weekly earnings (W)"])/sector["Median weekly earnings  (M)"])*100
    return sector

# merging 4 dataframes
def merge(wb, gender, financial, inventors, region):
    wb.rename(columns={'Economy': 'Country'}, inplace=True, errors='raise')
    df = pd.merge(gender, wb, on=["Country"], how="left")
    df = pd.merge(df, financial, on=["Country"], how="left")
    df = pd.merge(df, inventors, on=["Country"], how="left")
    df = pd.merge(df, region, on=["Country"], how="left")
    return df

# cleaning df
def clean_all(df):
    df.rename(columns={'Proportion of time spent on unpaid domestic and care work, female (% of 24 hour day)': 'Unpaid domestic and care work (F)',
                   'Proportion of time spent on unpaid domestic and care work, male (% of 24 hour day) ': 'Unpaid domestic and care work (M)',
                   'Law mandates equal remuneration for females and males for work of equal value (1=yes; 0=no)': 'Mandatory equal remuneration by law',
                   'Women making their own informed decisions regarding sexual relations, contraceptive use and reproductive health care  (% of women age 15-49)': 'Freedom on sexual relations and reproductive health care',
                  'There is no legal provision that requires a married woman to obey her husband (1=yes; 0=no)': 'Requirement of obeying husband',
                   'A woman can sign a contract in the same way as a man (1=yes; 0=no)' : 'Equity in signing a contract',
                   'Women, Business and the Law: Parenthood Indicator Score (scale 1-100)' : 'WB&L: Parenthood Indicator',
                   'Share of the population with account in a financial institution (M)' : 'Financial institution account owners (M)',
                    'Share of the population with account in a financial institution (F)': 'Financial institution account owners (F)',
                   'Life expectancy at birth (M) ' : 'Life expectancy at birth (M)',
                  'Share of women inventors ' : 'Share of woman inventors'}, 
          inplace=True, errors='ignore')
    df['Gender Inequality Index (Rank)'] = df['Gender Inequality Index (Rank)'].replace("—", np.nan).replace("..", np.nan).astype(np.float64)
    df['Gender Inequality Index (Value)'] = df['Gender Inequality Index (Value)'].replace("..", np.nan).astype(np.float64)
    df['Maternal mortality ratio'] = df['Maternal mortality ratio'].replace("..", np.nan).str.replace(',','').astype(np.float64)
    df['Share of seats in parliament'] = df['Share of seats in parliament'].replace("..", np.nan).astype(np.float64)
    df['Population with at least some secondary education (F)'] = df['Population with at least some secondary education (F)'].replace("..", np.nan).astype(np.float64)
    df['Population with at least some secondary education (M)'] = df['Population with at least some secondary education (M)'].replace("..", np.nan).astype(np.float64)
    df['Labour force participation rate (F)'] = df['Labour force participation rate (F)'].replace("..", np.nan).astype(np.float64)
    df['Labour force participation rate (M)'] = df['Labour force participation rate (M)'].replace("..", np.nan).astype(np.float64)
    df['Human Development Index (F)'] = df['Human Development Index (F)'].replace("..", np.nan).astype(np.float64)
    df['Human Development Index (M)'] = df['Human Development Index (M)'].replace("..", np.nan).astype(np.float64)
    df['Expected years of schooling (F)'] = df['Expected years of schooling (F)'].replace("..", np.nan).astype(np.float64)
    df['Expected years of schooling (M)'] = df['Expected years of schooling (M)'].replace("..", np.nan).astype(np.float64)
    df['Mean years of schooling (F)'] = df['Mean years of schooling (F)'].replace("..", np.nan).astype(np.float64)
    df['Mean years of schooling (M)'] = df['Mean years of schooling (M)'].replace("..", np.nan).astype(np.float64)
    df['Estimated  gross national income per capita (F)'] = df['Estimated  gross national income per capita (F)'].replace("..", np.nan).str.replace(',','').astype(np.float64)
    df['Estimated  gross national income per capita (M)'] = df['Estimated  gross national income per capita (M)'].replace("..", np.nan).str.replace(',','').astype(np.float64)
    df["Share of woman inventors"] = df["Share of woman inventors"].astype(np.float64)
    df['Requirement of obeying husband'] = df['Requirement of obeying husband'].astype('Int64')
    df['Equity in signing a contract'] = df['Equity in signing a contract'].astype('Int64')
    df['Mandatory equal remuneration by law'] = df['Mandatory equal remuneration by law'].astype('Int64')

    return df 

def school():
    at_school = {'Country':['Spain', 'Mexico', 'USA', 'Denmark'],
        'Work full-time':[53.6, 12.9, 54.9, 71.6],
        'Work part-time':[42.0, 55.9, 40.6, 28.0],
        'Stay at home':[4.5, 31.1, 4.5, 0.4]
       }
    at_school = pd.DataFrame(at_school)
    at_school = at_school.melt(id_vars=['Country'], value_vars=['Work full-time', 'Work part-time', 'Stay at home'])
    return at_school

def not_school():
    not_at_school = {'Country':['Spain', 'Mexico', 'USA', 'Denmark'],
        'Work full-time':[13.9, 8.2, 17.3, 38.1],
        'Work part-time':[60.0, 51.8, 48.7, 56.1],
        'Stay at home':[26.2, 40.0, 33.9, 5.7]
       }
    not_at_school = pd.DataFrame(not_at_school)
    not_at_school = not_at_school.melt(id_vars=['Country'], value_vars=['Work full-time', 'Work part-time', 'Stay at home'])
    return not_at_school