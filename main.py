import streamlit as st
import yfinance as yf 

# Fucking arround with streamlit
import pandas as pd 
import numpy as np

ticker = "AAPL"

st.write(f"""
# Simple stock price app

Ticker symbol of the stock to be displayed in the graph: {ticker}        
         """)


data = yf.Ticker(ticker)

data_df = data.history(period='1d', start='2010-5-31', end='2022-9-30')
st.write(f"""# Closing price""")
st.line_chart(data_df.Close)
st.write(f"""# Volume""")
st.line_chart(data_df.Volume)