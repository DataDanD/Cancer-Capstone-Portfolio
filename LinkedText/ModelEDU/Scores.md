# Predictive Model Scores

Scores in this section are used to compare forecasting errors of different models on the same dataset.
All model score values in project were calculated using test data.
Test data are random rows in the data frame that are withheld from the model training process.
These random rows are used after model training to score how well the model predicts unseen data.
Training the model with both test and training data will make the models scores higher on test data.
Potentially making the model overfit and thus would result in poor predictions on new data.
It is important to use test data to compare the accuracy scores of different models, 
in order to find the best algorithm for the problem.

**Regression scores**: Mean Absolute Error(MAE), R2, RMSE, or without the R in Mean Squared Error(MSE).

- **RMSE** is commonly used to score how well regression models are predicting actual values.
Works by squaring the the difference of the prediction minus actual values to make all errors positive numbers.
This formula is used so that predictions below and above actual values will not cancel each other out when summed.
It also takes the root of the error so outliers with higher values are not penalized by the squaring process.
RMSE is known as the sample standard deviation for the differences between actual values and the predicted values.
The formula used to calculate RMSE means the output value is the average of all residuals
; the average distance measured between all of the model guesses and real numbers in the test data.
It is stated to be an accuracy measurement, that contains the magnitudes of errors in prediction.

- Mean Absolute Error (**MAE**) is another data scientist recommended scoring method.
The main advantage with this score is interpretability, as MAE is easier to understand,
Compared to RMSE, the square root of the average of squared errors.
MAE calculates average absolute difference between the prediction and the actual values.
Every error in MAE is directionally proportionate to the value of error, which is not the case for RMSE.

- **R2**, called the coefficient of determination, is similar to correlation values, but its range is between 0 and 1.
This score measures the goodness-of-fit between the model and the data, 
Measures how close the data is to the fitted regression line.
R2 is defined as the percentage of the response variable variation that is explained by a linear models, equals explained variation divided by total variation. 
R2 of 0 indicates model explains none of the variability in data around the mean.
While, 1 (100%) indicates that the model explains all the variability of respond data around the mean.
Limitation of the R2 scored is that it cannot determine if the estimates are biased and does not indicate whether regression model is adequate for data.
Can have a low R-squared value for a good model, or a high R-squared value for a model that does not fit the data. 
Therefore, R2 was taken out of modeling scripts used in this project
and other regression scores that give an absolute error measure were used.

- Mean squared error (**MSE**) is similar to RMSE, but does not square root the errors. 
Therefore, this score will be influence greater by high errors values that are squared. 
MSE is a useful score for models that cannot afford to have high error values, 
a few poor outliers will strongly effect this score.

Common **classification scores**: accuracy, recall, precision, f1, and roc accuracy.
When predicting categorical data we end up with a confusion matrix that contain, true positive, true negative, false positive and false negative values. These values are then used in different formulas to calculate the the scores listed above.

Later, after finding the model with the best score we can see what features matter the most in making accurate predictions, this will calculate the feature importance in the data.
