# Statistical Methods in Machine Learning

Concepts in this file were taking up too much space in README file.
All sections have a link to them in projects home page.

## Correlation Overview

![Heatmap of All Features](https://github.com/DataDanD/CancerCapstone/blob/master/Graphs/heatmap.png)

Correlation happens when a variable can be very accurately predicted 
by using other data feature or features
in a basic multiple linear regression model.
Basically defined as a mutual dependence, or association 
between two of more things 
in a predictable statistical manner.
This linear relationship might be causal, but does not have to be to form a correlation.
Scale of data is not considered when determining correlations.
The three types of correlations are positive, negative, or no correlation.
Correlations are measured with a correlation coefficient 
that varies between -1 (a strong negative relations) and +1 (a strong positive correlation). 
The relationship gets weaker as the value goes towards 0.

Unfortunately we have lots of correlating features in heatmap above
and this section is the longest.
A data scientist should believe that
Garbage data into the model equals garbage predictions out.

This "garbage" data is why analyzing data has one of the largest proportions of total time 
in typical machine learning projects.
Cleaning and possibly modeling
data are the other processes that should take a long time for good results.
Finding government data took a long time as well in this atypical machine learning adventure. 
Going to assuming companies already have databases with information 
available for modeling activities.


### Positive Correlation 

Represented as light color in graph above.

A county with high value in feature_1, likely has high value in feature_2, or low and low values, when feature_1 and feature_2 have a positive correlation. When features increase or decrease together, in same direction.

If all values for the two features are graphed on a scatter plot and a line is drawn though points, it would start in lower left corner and reach to upper right.

#### Positive Example 

Elderly Medicare & Cancer Rate features have a positive correlation.

This makes sense, as humans age we have a higher chance of getting cancer.
Advancing age is the most important cancer risk factor states the National Cancer Institute. [8]
Older populations (higher Medicare rate) are more prone to cancer
and having an older population within a county will have more cancer incidents.
Less young people get cancer with the average age of a cancer diagnosis is over 60; 
seen in the graph below, created with the California cancer data.

[cancer age](https://github.com/DataDanD/Cancer-Capstone-Portfolio/blob/master/Graphs/SexCanAge.png)

According to the data from this project, men have a higher average age for getting cancer; 
this was surprising as females are known to live a few years longer and than men. 
Maybe this is due to breast cancer vs prostate cancer or men not going to the doctor as often?

This correlation should help with model predictions later on.
The project started without socioeconomic data and wasn't preforming very well.


### Negative Correlation 

Represented as darker colors on the heatmap.

Feature values go in opposite directions of each other if they have a negative correlation. Therefore, when feature_1 increases then feature_2 decreases, or as feature_1 is considered to have a lower value then feature_2 should have a higher value compared to county averages.

If graphed the same way as in positive correlation section, regression line would start in top left and go to bottom right.

#### Negative Example

In the heatmap Median Income & Disabled Medicare have a negative correlation. 
As median income goes up disabled medicare rates go down. 

This could suggest:
1) Age?
Counties with a younger population could have higher median incomes and lower disabled Medicare. 
- Higher income: higher working rate as young people need to build up currency for life expenses.
- Less disabled Medicare: younger people are supposed to be healthier and would qualify for Medicaid, not Medicare. Medicare is for citizens over 65 years of age, some few rare age exceptions.
Counties with older populations have lower median incomes and higher disabled Medicare rates.
- Lower Income: more retired people not working, relying on saved funds.
- Higher disabled Medicare: As people age the change of injury, infection and other disabling conditions become more likely.

2) Cost?
People with disabled Medicare might unfortunately not be able to afford to live in counties with higher incomes. 
Rates of disabled medicare are in counties of lower income.

3) Work Ethic? 
(Based on trips to Arkansas)
Counties with people making less might have a higher rate to abuse the system. 

The negative relation here can mean many things and we can only guess or hypothesis the reasons. 
We cannot say for fact what factors are causing these features to relate without a research experiment.
Proper references articles citing research on these relations would also work.

Some relations in this projects heatmap might be abnormal.
Only seen in California or 
based on the select data used.
That is another thing to keep in mind. 


### Correlation Test (Graph from Early EDA)

Which graph shows a positive and which shows a negative correlation to year?

#### Cancer Incidents per Year
[Cancer Incidents](https://github.com/DataDanD/Cancer-Capstone-Portfolio/blob/master/Graphs/SexCanCountsYr.png)

Second graph in [SEER EDA](https://github.com/DataDanD/Cancer-Capstone-Portfolio/blob/master/Jupyters/CanRate%20EDA.ipynb) notebook

#### Chemicals Released per Year
[Chemicals](https://github.com/DataDanD/Cancer-Capstone-Portfolio/blob/master/Graphs/ChemByYr.png)

fourth graph in [TRI](https://github.com/DataDanD/Cancer-Capstone-Portfolio/blob/master/Jupyters/TRI%20EDA.ipynb) notebook

#### Answers:

##### Cancer Incidents: 
Positive correlation to time - 
increasing number of cancer cases as year increases. 
Positive note: population is also increasing in the state of California and cancer incidents is dropping 
[SEER EDA](https://github.com/DataDanD/Cancer-Capstone-Portfolio/blob/master/Jupyters/CanRate%20EDA.ipynb) third graph is cancer rates when grouped by county, year, age, race, and sex.

##### Chemicals Released: 
Negative correlation to time - 
less chemicals being released as year increases. 
Negative note: possibility that less companies are reporting releases of chemicals 


## Multicollinearity (fix)


In statistics, multicollinearity is when features in data used for regression models have strong correlation values. 
Having already explored correlations in probably too much detail we should understand what a regression models is used for
Then get into this relationship problem happening between correlated features.
Regression models are a commonly used type of machine learning algorithm used for predicting numerical targets.

Having correlated features, makes the effects of features
on the target variable hard to distinguish from each other.
Making model train longer.


## Feature Selection (complete)

An easy method for reducing multicollinearity is to only keep features that do not correlated by simply dropping columns. 
When two features relate delete the column: with a higher correlation value to a different feature, or with lower value to target variable.
A more timely method that will find the better feature when facing the feature selection dilemma is to run model multiple times switching correlated features.
The feature used in the model with highest score should then be kept.
Actually, when many variables relate in a problem this might not be simple. 

### Example with air pollution:

Feature 1 - Ozone, larger correlation to value being predicted (Cancer Rate), 
and research has related lower ozone values to higher skin cancer rates.

Feature 2 - PM2.5, larger correlation with some features like (Population), 
and research has linked higher PM2.5 values to increased risk of lung cancer.

Would keep Ozone as it relates more to incident and less to other features in data being modeled, 
if only selecting one.
Could try modeling methods with both features separately to analyze results; 
more code, maybe better result, and more analysis potential.
Also, merging both columns into a single value, might yield interesting results.
Combining columns together is called feature engineering and is discussed in next section.



###### Feature Engineering

Feature engineering keeps correlated features by creating a new column that 
somehow combines values of different columns
These definitely related social determinant columns would be appropriate to combine together.
Especially if the columns are measured with similar unites.
Using feature selection to drop some correlated features would be a quicker process, in reducing multicollinearity.

Most of these correlation were found after poster and modeling was completed, unfortunately engineering wont happen unless I redo parts of this project in the future.

Feature Engineering Example: 
Socioeconomic Status (new column) = (Normalize all columns) Poverty + Education + Unemployed + Uninsured / 4

Normalize all features so they weigh similar amounts (portions) before summing together. 
Adding a feature with higher values to columns with lower values will make the column with high values more important, 
skewing the new column potentially make lower valued features irrelevant. 
Normalizing will also importantly keep deviations of the features being added together.
However, these features already use the same unit of rates in population and wont need normalizing.
Divide by 4 (not necessary for modeling) in above equation to make new unit rate similar to other feature. 
If feature is used to create new column in formula it will have to be dropped and can't be analyzed later in project.
Therefore, combine as few features as possible when reducing correlations keeping more unique data and features 
for better modeling more features to analyze in result section.
If engineered features correlate they will need to be combined or dropped and process repeated,
until no multicollinearity exists between features used for the machine learning models.

(resource link)



