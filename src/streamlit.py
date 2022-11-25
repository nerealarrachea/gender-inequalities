import streamlit as st
import streamlit.components.v1 as components
from datetime import date
import pandas as pd
import pickle
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline

st.set_page_config(
     page_title="Salary prediction",
     page_icon="🚀",
     layout="wide",
)
