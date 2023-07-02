import streamlit as st
import pandas as pd
from io import BytesIO

st.set_page_config(page_title="orders", layout="wide")

orders = pd.read_csv("orders_selecet.csv", delimiter=",", low_memory=False)


# Fonction de filtrage
def apply_filters(data):
    filtered_data = data.copy()
    filtered_data = filtered_data[filtered_data["is_scheduled"] == is_scheduled]
    filtered_data = filtered_data[filtered_data["paymentType"] == paymentType]
    return filtered_data


st.header("Please Filter Here:")

is_scheduled = st.selectbox(
    "is_scheduled:", options=orders["is_scheduled"].unique(), index=0
)
paymentType = st.selectbox(
    "paymentType:", options=orders["paymentType"].unique(), index=0
)

filtered_orders = apply_filters(orders)


# Bouton de téléchargement Excel
def download_excel(df):
    output = BytesIO()
    excel_file = pd.ExcelWriter(output, engine="xlsxwriter")
    df.to_excel(excel_file, sheet_name="Filtered Orders", index=False)
    excel_file.save()
    output.seek(0)
    return output


excel_file = download_excel(filtered_orders)
st.download_button(
    label="Download Excel",
    data=excel_file,
    file_name="filtered_orders.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
)

st.dataframe(filtered_orders)
