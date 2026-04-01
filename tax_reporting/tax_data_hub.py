import pandas as pd

def generate_reports():

    data = pd.read_csv("data/tax_engine_output.csv")

    summary = data.groupby("country")["tax_amount"].sum()

    summary.to_csv("data/tax_summary_report.csv")

    print("Tax reporting generated")