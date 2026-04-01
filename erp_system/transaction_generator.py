import pandas as pd
import random

products = ["Vehicle","Parts","Services"]
countries = ["US","Germany","India"]

data = []

for i in range(500):

    amount = random.randint(5000,50000)

    data.append({
        "transaction_id": i,
        "product": random.choice(products),
        "country": random.choice(countries),
        "amount": amount
    })

df = pd.DataFrame(data)

df.to_csv("data/erp_transactions.csv", index=False)

print("ERP transactions generated")