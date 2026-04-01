import pandas as pd

def run_pipeline():

    transactions = pd.read_csv("data/erp_transactions.csv")

    transactions["status"] = "processed"

    transactions.to_csv("data/middleware_output.csv", index=False)

    print("Middleware ETL completed")