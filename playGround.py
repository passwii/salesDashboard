import streamlit as st
import pandas as pd

filePath = 'amazonOrderData/order.csv'
df = pd.read_csv(filePath)
keywords = df.columns.tolist()

selectCols = st.multiselect('Select Columns', keywords)
priceRange = st.slider('Price Range', float(df['item-price'].min()), float(df['item-price'].max()),
                       (float(df['item-price'].min()), float(df['item-price'].max())))

filteredData = df[selectCols][(df['item-price'] >= priceRange[0]) & (df['item-price'] <= priceRange[1])]
st.dataframe(filteredData)
