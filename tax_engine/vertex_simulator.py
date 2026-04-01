import pandas as pd

def calculate_tax():

    data = pd.read_csv("data/middleware_output.csv")

    tax_rates = {
        "US":0.08,
        "Germany":0.19,
        "India":0.18
    }

    data["tax_rate"] = data["country"].map(tax_rates)

    data["tax_amount"] = data["amount"] * data["tax_rate"]

    data.to_csv("data/tax_engine_output.csv", index=False)

    print("Tax determination completed")