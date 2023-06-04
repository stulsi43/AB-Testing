# AB-Testing
In the model, we define the dependent variable (total_visitors or total_carts) and the independent variable (absent_factor), using C() to specify it as a categorical variable. We then perform ANOVA on these models using anova_lm(), and print the results.

Here's how it works:

The unique() function is used on the 'absent_factor' column of the dataframe: df['absent_factor'].unique(). This line of code returns an array of unique absent factors found in the dataset.
Then, a loop for factor in absent_factors: is used to iterate over these unique absent factors.
For each absent factor, the dataframe is subsetted to only include rows where 'absent_factor' equals the current factor: df[df['absent_factor'] == factor].
Then, a model is created and an ANOVA is performed on this subset of the data, separately for 'total_visitors' and 'total_carts'.
