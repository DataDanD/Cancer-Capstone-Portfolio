
# Model Types in Machine Learning

Regression models are a commonly used type of machine learning algorithms and used for predicting numerical or continuous values.
The other popular supervised learning technique is called classification and this class of algorithms is used to predict the observations into different classes, as the name suggest. 
Only use classification models when predicting categorical variables. 
However, we are predicting rates, a numerical/continuous variable and 
therefore will use regression models to make these guesses of cancer incidents.
Most statistical algorithms can be used for both regression and classification problems. 
Classification trees are used for splitting data into groups, 
while regression trees are used in cases of predicting numerical variables. 
Both of these tree models are also called decision trees.
The main differences between these two tree types
is when to use each, but also how they calculate formation of branches.
Basically, tree model will try all available features, along with all available data, 
to calculate the feature to split the data on that will yield the best results.
[Tree splits](http://www.simafore.com/blog/bid/62482/2-main-differences-between-classification-and-regression-trees), explained in more detail.

The problem with a single decision tree is that it will keep splitting 
until all the training data is correct, this causes overfitting and
poor performance on test data.
Using algorithms that contain multiple low correlating stumps is can lead to powerful model, 
especially when the stumps are created in sequential order, learning for mistakes in training data.

Decision trees are important for both Random forest and boosting models.
How decision trees decide on feature to split on
