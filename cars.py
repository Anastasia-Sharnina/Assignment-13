import seaborn as sns
import matplotlib.pyplot as plt

# Load the car crashes dataset
car_crashes = sns.load_dataset("car_crashes")

# Set the style for the plots
sns.set(style="whitegrid")

# 1. Histogram of Total Accidents
plt.figure(figsize=(10, 6))
sns.histplot(car_crashes['total'], bins=30, kde=True)
plt.title('Distribution of Total Accidents')
plt.xlabel('Total Accidents (per billion miles)')
plt.ylabel('Frequency')
plt.show()

# 2. Pair Plot
sns.pairplot(car_crashes, vars=['total', 'speeding', 'alcohol', 'ins_losses'], hue='abbrev')
plt.suptitle('Pair Plot of Key Variables by State Abbreviation', y=1.02)
plt.show()

#Bar Plot of Average Speeding by State Abbreviation
plt.figure(figsize=(14, 6))
average_speeding = car_crashes.groupby('abbrev')['speeding'].mean().sort_values(ascending=False)
sns.barplot(x=average_speeding.index, y=average_speeding.values)
plt.title('Average Speeding Percentage by State Abbreviation')
plt.xlabel('State Abbreviation')
plt.ylabel('Average Speeding Percentage')
plt.xticks(rotation=90)
plt.show()