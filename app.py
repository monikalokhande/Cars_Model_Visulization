import streamlit as st
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

st.title("Car Dataset Visualization")

# Upload CSV file
uploaded_file = st.file_uploader("Upload your car dataset CSV", type=["csv"])

if uploaded_file is not None:
    # Load the dataset
    df = pd.read_csv(uploaded_file)

    # Preprocess MSRP column if it exists
    if 'MSRP' in df.columns:
        df['MSRP'] = df['MSRP'].replace('[$,]', '', regex=True).astype('int64')

    # Sidebar brand selector
    brand_list = df['Make'].unique()
    selected_brand = st.sidebar.selectbox("Select Brand", brand_list)

    # Filter by selected brand
    brd = df[df['Make'] == selected_brand]

    # Show the filtered data
    st.subheader(f"Cars from {selected_brand}")
    st.dataframe(brd)

    # Invoice by Type
    st.subheader("Invoice by Type")
    fig1, ax1 = plt.subplots(figsize=(10, 5))
    sb.barplot(x='Type', y='Invoice', data=brd, palette='winter', ax=ax1)
    plt.xticks(rotation=90)
    st.pyplot(fig1)

    # MSRP by Model
    st.subheader("MSRP by Model")
    fig2, ax2 = plt.subplots(figsize=(12, 6))
    sb.barplot(x='Model', y='MSRP', data=brd, palette='summer', ax=ax2)
    plt.xticks(rotation=90)
    st.pyplot(fig2)

else:
    st.info("Please upload a CSV file to begin.")
