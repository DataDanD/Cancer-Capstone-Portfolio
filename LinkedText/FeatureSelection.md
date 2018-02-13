# Feature Selection

An easy method for reducing multicollinearity is to only keep features that do not correlated by simply dropping columns. 
When two features relate delete the column: with a higher correlation value to a different feature, or with lower value to target variable.
A more timely method that will find the better feature when facing the feature selection dilemma is to run model multiple times switching correlated features.
The feature used in the model with highest score should then be kept.
Actually, when many variables relate in a problem this might not be simple. 

## Example with air pollution:

#### Ozone 
Larger correlation to value being predicted (Cancer Rate), 
and research has related lower ozone values to higher skin cancer rates.

#### PM2.5
Larger correlation with some features like (Population), 
and research has linked higher PM2.5 values to increased risk of lung cancer.

### Deciding
Would keep Ozone as it relates more to incident and less to other features in data being modeled, 
if only selecting one.

#### Techniques
Could try modeling methods with both features separately to analyze results; 
more code, maybe better result, and more analysis potential.
Also, merging both columns into a single value, might yield interesting results.
Combining columns together is called feature engineering and is discussed in next section.

