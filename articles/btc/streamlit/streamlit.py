import streamlit as st
from streamlit_echarts import st_echarts
import pandas as pd

# Load your data into a pandas DataFrame.
# Replace 'your_data.csv' with the path to your actual data file.
# Ensure your data file has 'date', 'active_addresses', and 'funded_addresses' columns.
data = pd.read_csv('btc.csv')

# Create the ECharts line chart options dictionary.
options = {
    "title": {
        "text": 'Bitcoin daily active addresses grew 2% QoQ',
        "subtext": 'Daily active addresses and funded addresses',
        "left": 'center'
    },
    "tooltip": {
        "trigger": 'axis'
    },
    "legend": {
        "data": ['Active Addresses', 'Funded Addresses'],
        "top": 'bottom'
    },
    "grid": {
        "left": '3%',
        "right": '4%',
        "bottom": '3%',
        "containLabel": True
    },
    "toolbox": {
        "feature": {
            "saveAsImage": {}
        }
    },
    "xAxis": {
        "type": 'category',
        "boundaryGap": False,
        "data": data['date'].tolist()  # Assumes a 'date' column in your data.
    },
    "yAxis": [
        {
            "type": 'value',
            "name": 'Daily Active Addresses (millions)',
            "position": 'left'
        },
        {
            "type": 'value',
            "name": 'Funded Addresses (millions)',
            "position": 'right'
        }
    ],
    "series": [
        {
            "name": 'Active Addresses',
            "type": 'line',
            "data": data['active_addresses'].tolist()  # Assumes an 'active_addresses' column in your data.
        },
        {
            "name": 'Funded Addresses',
            "type": 'line',
            "yAxisIndex": 1,
            "data": data['funded_addresses'].tolist()  # Assumes a 'funded_addresses' column in your data.
        }
    ]
}

# Use streamlit_echarts to render the chart in Streamlit.
st_echarts(options=options, height="500px")
