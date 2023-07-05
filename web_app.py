import streamlit as st
import pandas as pd
import plotly.express as px
import plost

st.set_page_config(page_title="Sales Dashboard", page_icon=":bar_chart:", layout="wide", initial_sidebar_state='expanded')

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


st.sidebar.success("Sellers statistics")

df = pd.read_excel("sellers_informations.xlsx", engine="openpyxl", index_col=0)



# -----SIDEBAR
st.sidebar.header("Filter sellers: ")

sellers = st.sidebar.multiselect(
    "Select the Seller:",
    options=df["title"].unique(),
    default=df["title"][1]  
)

# ---- MAINPAGE ----
st.title(":bar_chart: Sales Dashboard")
st.markdown("##")

df_selection = df.query(
    "title == @sellers"
)

# TOP KPI's
total_sold_products = int(df_selection['total_sold_products'])
count_categories = int(df_selection['selling_categories'])
average_price = int(df_selection['average_price'])
total_sales = int(df_selection["total_revenue"].sum())
average_rating = round(df_selection["rating"].mean(), 1)
star_rating = ":star:" * int(round(average_rating, 0))
st.markdown('### Sellers')
col1, col2, col3, col4, col5 = st.columns(5)

col1.metric("Total Sold Products", f"{total_sold_products:}")
col2.metric("Total Sales", f"UZS {total_sales:,}", "-8%")
col3.metric("Count of Selling Categories", count_categories)
col4.metric("Average Product Price", f"{average_price: ,}")
col4.metric("Average Rating", f"{average_rating}")


st.markdown("""---""")

st.dataframe(df)
