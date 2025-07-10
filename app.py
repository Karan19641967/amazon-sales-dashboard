# app.py
import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("amazon_sale_report.csv")

st.title("📊 Amazon Sales Dashboard")

# Sidebar Filters
selected_state = st.sidebar.selectbox("Select State", df["ship-state"].unique())
filtered_df = df[df["ship-state"] == selected_state]

# KPIs
total_sales = filtered_df["total-amount"].sum()
total_orders = filtered_df["order-id"].nunique()
st.metric("Total Sales", f"₹{total_sales:,.2f}")
st.metric("Total Orders", total_orders)

# Plotly Bar Chart
st.subheader("Sales by Category")
fig1 = px.bar(filtered_df, x="category", y="total-amount", color="category", title="Category-wise Sales")
st.plotly_chart(fig1)

# Seaborn Heatmap
st.subheader("Heatmap - Category vs Payment Type")
fig2, ax = plt.subplots()
pivot = filtered_df.pivot_table(index="category", columns="payment-type", values="total-amount", aggfunc='sum', fill_value=0)
sns.heatmap(pivot, annot=True, fmt=".0f", cmap="Blues", ax=ax)
st.pyplot(fig2)

# Matplotlib Pie Chart
st.subheader("Payment Type Distribution")
fig3, ax = plt.subplots()
filtered_df["payment-type"].value_counts().plot.pie(autopct="%1.1f%%", ax=ax)
ax.set_ylabel("")
st.pyplot(fig3)
