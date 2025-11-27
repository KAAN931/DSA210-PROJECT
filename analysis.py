import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import numpy as np

# --- 1. Load Data ---
print("Loading data...")
df = pd.read_csv('dataset.csv', low_memory=False)

# --- 2. Data Cleaning ---
print("Cleaning data...")
df = df.dropna(subset=['diameter'])

# Convert 'diameter' to numeric
df['diameter'] = pd.to_numeric(df['diameter'], errors='coerce')

# Map PHA (Potentially Hazardous Asteroid) to binary: Y=1, N=0
df['PHA_binary'] = df['pha'].map({'Y': 1, 'N': 0})

# Drop any rows that became NaN after conversion
df = df.dropna(subset=['diameter', 'PHA_binary', 'moid_ld'])

print(f"Data cleaned. Remaining rows: {len(df)}")

# --- 3. Exploratory Data Analysis (EDA) ---

# A. Histogram of Diameter
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='diameter', bins=50, log_scale=True)
plt.title('Distribution of Asteroid Diameters (Log Scale)')
plt.xlabel('Diameter (km)')
plt.savefig('diameter_distribution.png')
print("Saved: diameter_distribution.png")

# B. Scatter Plot: MOID vs Diameter (Colored by PHA)
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='moid_ld', y='diameter', hue='pha', alpha=0.6)
plt.yscale('log') # Log scale for diameter makes it easier to see
plt.title('MOID vs Diameter (Colored by Hazard Status)')
plt.xlabel('Earth Minimum Orbit Intersection Distance (MOID)')
plt.ylabel('Diameter (km) - Log Scale')
plt.savefig('moid_vs_diameter.png')
print("Saved: moid_vs_diameter.png")

# C. Correlation Matrix
# Select only numeric columns relevant to orbit/physics
numeric_cols = ['diameter', 'e', 'a', 'q', 'i', 'moid_ld', 'PHA_binary']
corr_matrix = df[numeric_cols].corr()

plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix of Orbital Features')
plt.savefig('correlation_matrix.png')
print("Saved: correlation_matrix.png")

# --- 4. Hypothesis Testing (The T-Test) ---
print("\n--- Running T-Test ---")

# Split the data into two groups
pha_group = df[df['pha'] == 'Y']['moid_ld']
non_pha_group = df[df['pha'] == 'N']['moid_ld']

# Perform Independent T-Test
# equal_var=False because variances are likely different (Welch's t-test)
t_stat, p_val = stats.ttest_ind(pha_group, non_pha_group, equal_var=False)

print(f"Mean MOID (Hazardous): {pha_group.mean():.4f}")
print(f"Mean MOID (Non-Hazardous): {non_pha_group.mean():.4f}")
print(f"T-statistic: {t_stat:.4f}")
print(f"P-value: {p_val}")

if p_val < 0.05:
    print("Result: Significant difference found (Reject Null Hypothesis)")
else:
    print("Result: No significant difference (Fail to reject H0)")
