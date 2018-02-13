# Feature Engineering
## Overview
Feature engineering will keep the correlated features for the modeling process, 
by creating a new column that somehow manages to combine the values within the different columns.
The correlated socioeconomic features would be appropriate to tie together.
Engineering for the new value would be easy as they are
all measured with percent of population.
It is convenient to merge columns that share the same unite measurement.

### Could use Selection
Using feature selection by deleting columns that
have strong correlation values might be a quicker process, 
in reducing multicollinearity.

## Example: 
Socioeconomic Status (new column) = (Normalize all columns) Poverty + Education + Unemployed + Uninsured / 4

### Method
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

## Discusion
Most of these correlation were found after poster and modeling was completed, unfortunately engineering wont happen unless I redo parts of this project in the future.


#### (resource link)

