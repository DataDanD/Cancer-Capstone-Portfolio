# Correlations

## Overview
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

### Figure 1. Heatmap
Unfortunately this heatmap including all features has a lot of correlating values.

![Heatmap of All Features](https://github.com/DataDanD/CancerCapstone/blob/master/Graphs/heatmap.png)

### Clean Up 
A data scientist should believe that
Garbage data into the model equals garbage predictions out.
This "garbage" data is why analyzing data has one of the largest proportions of total time 
in typical machine learning projects.
Cleaning and possibly modeling
data are the other processes that should take a long time for good results.
Finding government data took a long time as well in this atypical machine learning adventure. 
Going to assuming companies already have databases with information 
available for modeling activities.


## Positive Correlation 
Represented as light color in graph above.

A county with high value in feature_1, likely has high value in feature_2, or low and low values, when feature_1 and feature_2 have a positive correlation. When features increase or decrease together, in same direction.

If all values for the two features are graphed on a scatter plot and a line is drawn though points, it would start in lower left corner and reach to upper right.

### Positive Example 
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


## Negative Correlation 
Represented as darker colors on the heatmap.

Feature values go in opposite directions of each other if they have a negative correlation. Therefore, when feature_1 increases then feature_2 decreases, or as feature_1 is considered to have a lower value then feature_2 should have a higher value compared to county averages.

If graphed the same way as in positive correlation section, regression line would start in top left and go to bottom right.

### Negative Example
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


## Correlation Test (Graph from Early EDA)

Which graph shows a positive and which shows a negative correlation to year?

#### Cancer Incidents per Year
![Cancer Incidents](https://github.com/DataDanD/Cancer-Capstone-Portfolio/blob/master/Graphs/SexCanCountsYr.png)

Second graph in [SEER EDA](https://github.com/DataDanD/Cancer-Capstone-Portfolio/blob/master/Jupyters/CanRate%20EDA.ipynb) notebook

#### Chemicals Released per Year
![Chemicals](https://github.com/DataDanD/Cancer-Capstone-Portfolio/blob/master/Graphs/ChemByYr.png)

fourth graph in [TRI](https://github.com/DataDanD/Cancer-Capstone-Portfolio/blob/master/Jupyters/TRI%20EDA.ipynb) notebook

### Answers:

##### Cancer Incidents: 
Positive correlation to time - 
increasing number of cancer cases as year increases. 
Positive note: population is also increasing in the state of California and cancer incidents is dropping 
[SEER EDA](https://github.com/DataDanD/Cancer-Capstone-Portfolio/blob/master/Jupyters/CanRate%20EDA.ipynb) third graph is cancer rates when grouped by county, year, age, race, and sex.

##### Chemicals Released: 
Negative correlation to time - 
less chemicals being released as year increases. 
Negative note: possibility that less companies are reporting releases of chemicals 
