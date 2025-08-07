import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

# Load and preprocess data
df = pd.read_csv("Nifty_Stocks.csv")
df['Date'] = pd.to_datetime(df['Date'])

# App title
st.title("Nifty Stocks Explorer")

# Show available categories
categories = df['Category'].unique()
selected_category = st.selectbox("Select Nifty Category:", categories)

# Filter by selected category
cat_df = df[df['Category'] == selected_category]

# Show available company symbols in selected category
symbols = cat_df['Symbol'].unique()
selected_symbol = st.selectbox("Select Nifty Company Symbol:", symbols)

# Filter by selected symbol
sym_df = cat_df[cat_df['Symbol'] == selected_symbol]

# Plot closing price
st.subheader(f"Closing Price Trend for {selected_symbol}")
fig, ax = plt.subplots(figsize=(15, 8))
sb.lineplot(x='Date', y='Close', data=sym_df, ax=ax)
plt.xticks(rotation=45)
st.pyplot(fig)
