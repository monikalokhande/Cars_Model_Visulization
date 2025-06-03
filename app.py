import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt

# Load your dataset
# Assuming you already have the dataframe `df`
# If loading from CSV: df = pd.read_csv('CARS.csv')

# Clean the MSRP column
df['MSRP'] = df['MSRP'].replace('[$,]', '', regex=True).astype('int64')

# Sidebar for brand selection
st.sidebar.title("Filter")
brand_list = df['Make'].unique()
selected_brand = st.sidebar.selectbox("Select Brand", brand_list)

# Filter data based on selection
brd = df[df['Make'] == selected_brand]

# Show the filtered DataFrame (optional)
st.subheader(f"Cars from {selected_brand}")
st.dataframe(brd)

# First Plot: Invoice by Type
st.subheader(f"Invoice by Type for {selected_brand}")
fig1, ax1 = plt.subplots(figsize=(10, 5))
sb.barplot(x='Type', y='Invoice', data=brd, palette='winter', ax=ax1)
plt.xticks(rotation=90)
st.pyplot(fig1)

# Second Plot: MSRP by Model
st.subheader(f"MSRP by Model for {selected_brand}")
fig2, ax2 = plt.subplots(figsize=(10, 5))
sb.barplot(x='Model', y='MSRP', data=brd, palette='summer', ax=ax2)
plt.xticks(rotation=90)
st.pyplot(fig2)
