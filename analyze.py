import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("expenses.csv")

print("First few rows:")
print(df.head())

print("\nTotal spent:", df["amount"].sum())

print("\nSpending by category:")
category_totals = df.groupby("category")["amount"].sum()
print(category_totals)

category_totals.plot(kind="bar", title="Spending by Category")
plt.ylabel("Amount")
plt.tight_layout()
plt.savefig("spending_chart.png")
plt.show()
df["date"] = pd.to_datetime(df["date"])
daily_totals = df.groupby("date")["amount"].sum()

plt.figure()
daily_totals.plot(kind="line", marker="o", title="Spending Over Time")
plt.ylabel("Amount")
plt.xlabel("Date")
plt.tight_layout()
plt.savefig("spending_over_time.png")
plt.show()