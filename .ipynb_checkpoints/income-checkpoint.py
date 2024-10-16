import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statistics as stats

# Step 1: Create an ndarray that represents company income for 10 months
income = np.array([10000, 12000, 15000, 18000, 20000, 22000, 25000, 27000, 30000, 32000])  # Income for Jan to Oct

# Step 2: Multiply these incomes by 0.7 to get income without tax
income_without_tax = income * 0.7

# Step 3: Create another data collection that represents company expenses for the same 10 months
expenses = np.array([8000, 9000, 11000, 13000, 14000, 16000, 17000, 19000, 21000, 23000])  # Expenses for Jan to Oct

# Step 4: Create a DataFrame based on income_without_tax and expenses
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct']
data = {
    'Month': months,
    'Income_without_tax': income_without_tax,
    'Expenses': expenses
}
df = pd.DataFrame(data)

# Step 5: Output the DataFrame on the screen
print("Full DataFrame:")
print(df)

# Step 6: Output the data related to the 1st quarter only (Jan, Feb, Mar)
first_quarter_df = df[df['Month'].isin(['Jan', 'Feb', 'Mar'])]
print("nData for the 1st Quarter (Jan, Feb, Mar):")
print(first_quarter_df)

# Calculate savings for each month
savings = income_without_tax - expenses
df['Savings'] = savings

# Filter out negative savings for the pie chart
positive_savings = df[df['Savings'] >= 0]

# Plot: Income by Month
plt.figure(figsize=(10, 5))
plt.plot(df['Month'], df['Income_without_tax'], marker='o', color='blue', label='Income without Tax')
plt.title('Income by Month')
plt.xlabel('Month')
plt.ylabel('Income without Tax')
plt.xticks(rotation=45)
plt.legend()
plt.grid()
plt.show()

# Column Chart: Savings for Each Month
plt.figure(figsize=(10, 5))
plt.bar(df['Month'], df['Savings'], color='green')
plt.title('Savings for Each Month')
plt.xlabel('Month')
plt.ylabel('Savings')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()

# Pie Chart: Part of Each Month Saving in Total Saving of This Year (only positive savings)
if not positive_savings.empty:
    total_positive_savings = positive_savings['Savings'].sum()
    plt.figure(figsize=(8, 8))
    colors = plt.cm.Paired(np.arange(len(positive_savings)))  # Generate colors from colormap
    plt.pie(positive_savings['Savings'], labels=positive_savings['Month'], colors=colors, autopct='%1.1f%%')
    plt.title('Savings Distribution by Month (Positive Values Only)')
    plt.show()
else:
    print("No positive savings to display in the pie chart.")

# Calculate average income for each quarter
quarter1_income = income_without_tax[0:3].mean()  # Jan, Feb, Mar
quarter2_income = income_without_tax[3:6].mean()  # Apr, May, Jun
quarter3_income = income_without_tax[6:9].mean()  # Jul, Aug, Sep
quarter4_income = income_without_tax[9:].mean()    # Oct

print(f"Average Income for Quarter 1: {quarter1_income}")
print(f"Average Income for Quarter 2: {quarter2_income}")
print(f"Average Income for Quarter 3: {quarter3_income}")
print(f"Average Income for Quarter 4: {quarter4_income}")