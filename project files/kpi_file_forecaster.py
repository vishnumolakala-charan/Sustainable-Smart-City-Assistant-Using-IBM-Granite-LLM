# kpi_file_forecaster.py

"""
KPI Forecasting Module
----------------------
This module allows forecasting of water or energy usage using Linear Regression.
It's designed for integration with the Streamlit dashboard in the Sustainable Smart City Assistant project.

Skill Tags:
- Linear Regression
- Time-Series Forecasting
- Streamlit Visualization
"""

import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from datetime import timedelta

def load_data(uploaded_file):
    try:
        df = pd.read_csv(uploaded_file, parse_dates=['date'])
        df = df.sort_values('date')
        return df
    except Exception as e:
        st.error(f"Error loading file: {e}")
        return None

def forecast_kpi(df, target_column, days_ahead=7):
    """
    Forecast KPI using Linear Regression

    Args:
        df (pd.DataFrame): DataFrame with 'date' and target_column
        target_column (str): Name of KPI column to predict
        days_ahead (int): Days to forecast

    Returns:
        pd.DataFrame: Future dates and predicted values
    """
    df = df[['date', target_column]].dropna()
    df['days_since_start'] = (df['date'] - df['date'].min()).dt.days

    # Prepare training data
    X = df[['days_since_start']]
    y = df[target_column]

    model = LinearRegression()
    model.fit(X, y)

    # Forecast future dates
    last_day = df['days_since_start'].max()
    future_days = np.arange(last_day + 1, last_day + 1 + days_ahead).reshape(-1, 1)
    predictions = model.predict(future_days)

    future_dates = [df['date'].max() + timedelta(days=i) for i in range(1, days_ahead + 1)]
    forecast_df = pd.DataFrame({
        'date': future_dates,
        f'predicted_{target_column}': predictions
    })

    return forecast_df

def plot_forecast(df, forecast_df, target_column):
    plt.figure(figsize=(10, 5))
    plt.plot(df['date'], df[target_column], label='Actual', marker='o')
    plt.plot(forecast_df['date'], forecast_df[f'predicted_{target_column}'], label='Forecast', marker='x', linestyle='--')
    plt.xlabel('Date')
    plt.ylabel(target_column.capitalize())
    plt.title(f'{target_column.capitalize()} Forecast')
    plt.legend()
    st.pyplot(plt)

def display_forecasting_ui():
    st.header("📈 KPI Forecasting")
    st.write("Upload a CSV file with historical data to forecast Water or Energy usage.")
    st.markdown("**Required columns:** `date`, `water_usage`, `energy_usage`")

    uploaded_file = st.file_uploader("Upload CSV File", type=['csv'])

    if uploaded_file:
        df = load_data(uploaded_file)
        if df is not None:
            kpi_option = st.selectbox("Select KPI to Forecast", ['water_usage', 'energy_usage'])
            forecast_days = st.slider("Days to Forecast", min_value=1, max_value=30, value=7)

            forecast_df = forecast_kpi(df, kpi_option, forecast_days)

            st.subheader("Forecasted Data")
            st.dataframe(forecast_df)

            plot_forecast(df, forecast_df, kpi_option)
