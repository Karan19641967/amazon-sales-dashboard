import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
@st.cache
def load_data():
    data = pd.read_csv('amazon_sale_report.csv')
    return data

# Main function to run the app
def main():
    st.title("Amazon Sales Report Dashboard")

    # Load data
    data = load_data()

    # Display the data
    st.subheader("Data Overview")
    st.write(data.head())

    # Sales by Status
    st.subheader("Sales by Status")
    sales_status = data.groupby('Status')['Amount'].sum().reset_index()
    fig1 = px.bar(sales_status, x='Status', y='Amount', title='Total Sales by Status')
    st.plotly_chart(fig1)

    # Sales by Fulfilment
    st.subheader("Sales by Fulfilment")
    sales_fulfilment = data.groupby('Fulfilment')['Amount'].sum().reset_index()
    fig2 = px.pie(sales_fulfilment, names='Fulfilment', values='Amount', title='Sales Distribution by Fulfilment')
    st.plotly_chart(fig2)

    # Seaborn heatmap for Quantity by Category and Size
    st.subheader("Quantity Heatmap by Category and Size")
    heatmap_data = data.pivot_table(values='Qty', index='Category', columns='Size', aggfunc='sum', fill_value=0)
    plt.figure(figsize=(10, 6))
    sns.heatmap(heatmap_data, annot=True, fmt='g', cmap='viridis')
    st.pyplot(plt)

    # Matplotlib line chart for Amount over Order ID
    st.subheader("Sales Amount Over Order ID")
    plt.figure(figsize=(10, 6))
    plt.plot(data['Order ID'], data['Amount'], marker='o')
    plt.title('Sales Amount Over Order ID')
    plt.xlabel('Order ID')
    plt.ylabel('Amount')
    plt.xticks(rotation=45)
    st.pyplot(plt)

if __name__ == "__main__":
    main()
