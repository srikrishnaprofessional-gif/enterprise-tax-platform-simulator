import streamlit as st
import pandas as pd
import numpy as np
from faker import Faker

fake = Faker()

# -----------------------------------
# PAGE CONFIGURATION
# -----------------------------------

st.set_page_config(
    page_title="Enterprise Tax Platform Simulator",
    page_icon="📊",
    layout="wide"
)

# -----------------------------------
# HEADER
# -----------------------------------

st.markdown(
"""
<h1 style='text-align:center;color:#4ade80;'>
Enterprise Tax Platform Simulator
</h1>
<p style='text-align:center;font-size:18px;'>
ERP → Middleware → Vertex Tax Engine → Tax Data Hub
</p>
""",
unsafe_allow_html=True
)

# -----------------------------------
# SIDEBAR CONTROL PANEL
# -----------------------------------

st.sidebar.title("Simulation Control Panel")

num_transactions = st.sidebar.slider(
    "ERP Transaction Volume",
    100,
    5000,
    500
)

st.sidebar.info(
"Adjust parameters to simulate enterprise workloads."
)

# -----------------------------------
# ERP TRANSACTION GENERATOR
# -----------------------------------

def generate_transactions(n):

    products = ["Vehicle","Parts","Services"]
    countries = ["US","Germany","India"]

    data = []

    for i in range(n):

        amount = np.random.randint(5000,50000)

        data.append({
            "transaction_id": i,
            "product": np.random.choice(products),
            "country": np.random.choice(countries),
            "amount": amount,
            "customer": fake.company()
        })

    return pd.DataFrame(data)


transactions = generate_transactions(num_transactions)

# -----------------------------------
# MIDDLEWARE PIPELINE (INFORMATICA)
# -----------------------------------

middleware_data = transactions.copy()

middleware_data["pipeline_status"] = "Processed"

# -----------------------------------
# TAX ENGINE (VERTEX SIMULATION)
# -----------------------------------

tax_rates = {
    "US":0.08,
    "Germany":0.19,
    "India":0.18
}

middleware_data["tax_rate"] = middleware_data["country"].map(tax_rates)

middleware_data["tax_amount"] = middleware_data["amount"] * middleware_data["tax_rate"]

# -----------------------------------
# KPI METRICS
# -----------------------------------

total_transactions = len(transactions)
total_revenue = transactions["amount"].sum()
total_tax = middleware_data["tax_amount"].sum()

col1, col2, col3 = st.columns(3)

col1.metric("Transactions", total_transactions)
col2.metric("Revenue", f"${total_revenue:,.0f}")
col3.metric("Total Tax", f"${total_tax:,.0f}")

# -----------------------------------
# SYSTEM MONITORING
# -----------------------------------

systems = pd.DataFrame({

    "System":[
        "ERP",
        "Middleware",
        "Vertex Engine",
        "Tax Data Hub"
    ],

    "Status":[
        "Healthy",
        "Healthy",
        np.random.choice(["Healthy","Failure"]),
        "Healthy"
    ]
})

systems["Status"] = systems["Status"].apply(
    lambda x: "🟢 Healthy" if x=="Healthy" else "🔴 Failure"
)

# -----------------------------------
# TABS
# -----------------------------------

tab1, tab2, tab3, tab4, tab5 = st.tabs([
"ERP Transactions",
"Middleware",
"Tax Engine",
"Reporting",
"AI Copilot"
])

# -----------------------------------
# ERP TAB
# -----------------------------------

with tab1:

    st.subheader("ERP Transaction System")

    st.dataframe(transactions)

    st.subheader("Revenue Distribution")

    st.bar_chart(transactions["amount"])

# -----------------------------------
# MIDDLEWARE TAB
# -----------------------------------

with tab2:

    st.subheader("Middleware Processing (Informatica Simulation)")

    st.write("Transactions processed through ETL pipeline")

    st.dataframe(middleware_data.head())

# -----------------------------------
# TAX ENGINE TAB
# -----------------------------------

with tab3:

    st.subheader("Vertex Tax Determination")

    st.dataframe(middleware_data)

# -----------------------------------
# REPORTING TAB
# -----------------------------------

with tab4:

    st.subheader("Tax Data Hub Reporting")

    report = middleware_data.groupby("country")["tax_amount"].sum()

    st.bar_chart(report)

    st.subheader("System Health Monitoring")

    st.dataframe(systems)

# -----------------------------------
# AI COPILOT TAB
# -----------------------------------

def ask_ai(q):

    q = q.lower()

    if "vertex" in q:
        return "Vertex is a tax determination engine used to calculate indirect taxes during transactions."

    if "middleware" in q:
        return "Middleware like Informatica moves data between ERP systems and tax engines."

    if "tax reporting" in q:
        return "Tax reporting aggregates tax data and generates regulatory compliance reports."

    if "incident" in q:
        return "Integration incidents occur when data pipelines fail between ERP, middleware, and tax engines."

    return "Ask about enterprise tax systems such as Vertex, middleware, or tax reporting."


with tab5:

    st.subheader("AI Tax Systems Copilot")

    question = st.text_input("Ask about enterprise tax systems")

    if question:

        response = ask_ai(question)

        st.success(response)

# -----------------------------------
# DATA DOWNLOAD
# -----------------------------------

st.header("Download Simulation Data")

csv = middleware_data.to_csv(index=False)

st.download_button(
    label="⬇ Download Transaction Dataset",
    data=csv,
    file_name="tax_transactions.csv",
    mime="text/csv"
)