import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols

# Load data from CSV file
df = pd.read_csv('AB_Testing Dataset.csv')

# Calculate the mean and standard deviation of total_visitors and total_carts
print(df[['total_visitors', 'total_carts']].describe())

# Group by location_country and calculate the mean of total_visitors and total_carts for each country
print(df.groupby('location_country')[['total_visitors', 'total_carts']].mean())

# Remove "Day " prefix from day column and convert it to integer
df['day'] = df['day'].str.replace('Day ', '').astype(int)

# Group by day and calculate the mean of total_visitors and total_carts for each day
print(df.groupby('day')[['total_visitors', 'total_carts']].mean())

# Get a list of the unique absent factors
absent_factors = df['absent_factor'].unique()

# Loop over each absent factor
for factor in absent_factors:
    # Subset the DataFrame for each absent factor
    df_factor = df[df['absent_factor'] == factor]
    
    # For each variable of interest, total_visitors and total_carts...
    for var in ['total_visitors', 'total_carts']:
        # Check if there is more than one unique value for the variable
        if df_factor[var].nunique() > 1:
            # If so, perform an ANOVA
            model = ols(f'{var} ~ C(location_country)', data=df_factor).fit()
            anova_table = sm.stats.anova_lm(model, typ=2)
            print(f'\nANOVA Results for {var} with absent factor {factor}:')
            print(anova_table)
        else:
            # If not, print a message indicating that there's not enough variation for ANOVA
            print(f'\nNot enough variation in {var} with absent factor {factor} for ANOVA.')
