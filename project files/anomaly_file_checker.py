# anomaly_file_checker.py

"""
Anomaly Detection Module
------------------------
This module checks for abnormal spikes in KPI data using IQR method.
Displays results in tabular format with colored badges for anomalies.

Skill Tags:
- Anomaly Detection
- Outlier Detection (IQR)
- Streamlit Dashboard
"""

import pandas as pd
import streamlit as st

def load_data(uploaded_file):
    try:
        df = pd.read_csv(uploaded_file, parse_dates=['date'])
        df = df.sort_values('date')
        return df
    except Exception as e:
        st.error(f"Error loading file: {e}")
        return None

def detect_anomalies(df, column):
    """
    Detect anomalies using Interquartile Range (IQR)

    Args:
        df (pd.DataFrame): Input data
        column (str): Column to analyze (e.g., water_usage)

    Returns:
        pd.DataFrame: Data with anomaly flag
    """
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    df['anomaly'] = df[column].apply(lambda x: '🔴 Abnormal' if x < lower or x > upper else '🟢 Normal')
    return df

def style_row(row):
    color = 'red' if row['anomaly'] == '🔴 Abnormal' else 'green'
    return [f'background-color: {color}; color: white;' if col == 'anomaly' else '' for col in row.index]

def display_anomaly_checker():
    st.header("🚨 Anomaly Detection in KPI Data")
    st.write("Upload a CSV file containing KPI values to detect abnormal spikes.")
    st.markdown("**Required columns:** `date`, `water_usage`, `energy_usage`")

    uploaded_file = st.file_uploader("Upload CSV File", type=['csv'])

    if uploaded_file:
        df = load_data(uploaded_file)
        if df is not None:
            column = st.selectbox("Select KPI for Anomaly Detection", ['water_usage', 'energy_usage'])

            df_result = detect_anomalies(df, column)

            st.subheader("Detection Results")
            styled_df = df_result.style.apply(style_row, axis=1)
            st.dataframe(styled_df, use_container_width=True)

            st.info("🔴 Abnormal = Detected Outlier | 🟢 Normal = Within Safe Range")
