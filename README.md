# DSA210-PROJECT
Project Proposal:
The motivation for this project is to apply data science methods to a real-world problem in planetary defense. Near-Earth Objects (NEOs) can pose a potential collision threat, and this project aims to build a model to identify them.

Goal: To build a machine learning model that can accurately predict whether an asteroid is "Potentially Hazardous" (a PHA) based on its available orbital and physical data.

Research Question: What are the most significant features (minimum orbit intersection distance, eccentricity, diameter) that determine if an asteroid is classified as hazardous?

The Data to be Used:
The project will use a single, publicly available dataset: the Asteroid Dataset available on Kaggle.

This dataset is a single, compiled CSV file sourced from the NASA JPL Small-Body Database (SBDB). It contains orbital parameters (like eccentricity, semi-major axis, minimum orbit intersection distance) and physical parameters (like diameter and albedo) for thousands of asteroids.

Plans on How to Collect It:
The data collection process is straightforward:

Navigate to the Kaggle dataset page for the Asteroid Dataset.

Download the asteroid_dataset.csv file directly.


Phase 2: Analysis Report


1. Data Collection and Cleaning

The data was successfully collected from the NASA JPL Asteroid Dataset (via Kaggle).
* Loading: The dataset was loaded into a Pandas DataFrame.
* Cleaning:
    * Rows with missing diameter were dropped to ensure accurate physical characterization.
    * The target variable PHA was mapped to binary values.
    * Final Dataset Size: 136,209 asteroids were used for the analysis.

2. Exploratory Data Analysis (EDA)

I conducted an exploratory analysis to understand the distribution of key orbital features and their relationship with the hazardous classification.
Univariate Analysis:
* Diameter: The distribution of asteroid diameters is highly right-skewed. Most asteroids are small, while a few are very large (Visualized in diameter_distribution.png).
Bivariate Analysis:
* Correlation Matrix: I generated a correlation heatmap (correlation_matrix.png).
    * Observation: MOID shows a negative correlation with the PHA label, suggesting that as the intersection distance decreases, the likelihood of being hazardous increases.
* Scatter Plots: We plotted moid_ld vs. diameter (moid_vs_diameter.png).
    * Pattern: Hazardous asteroids (PHA=1) clearly cluster in the region where moid_ld is low and diameter is sufficient to cause damage.

3. Hypothesis Testing

I formally tested the relationship between Earth intersection distance and hazardous classification.
* Null Hypothesis (H_0): There is no difference in the mean Minimum Orbit Intersection Distance (moid_ld) between Hazardous Asteroids (PHA) and Non-Hazardous Asteroids.
* Alternative Hypothesis (H_1): Hazardous Asteroids have a significantly smaller mean moid_ld than Non-Hazardous Asteroids.
* Test Used: Independent Two-Sample T-Test (assuming unequal variances).
Results:
* Mean MOID (Hazardous): 8.8419
* Mean MOID (Non-Hazardous): 555.0089
* T-statistic: -837.33
* P-value: < 0.001 (Calculated as approx. 0.0)
Conclusion:
Since the p-value is less than the significance level (alpha = 0.05), we reject the null hypothesis. There is statistically significant evidence that PHAs have a much smaller minimum orbit intersection distance than non-PHAs.

