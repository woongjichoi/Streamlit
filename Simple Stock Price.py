# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 13:37:18 2022

@author: choiw
"""

import yfinance as yf # can access to yahoo finance 
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price App 

Shown are the stock **closing price** and ***volume*** of Google!

""")

tickerSymbol = "GOOGL"
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')

st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)
st.write("""
## Volume Price
""")
st.line_chart(tickerDf.Volume)