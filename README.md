# Calculating Cancer Rates with Boosted Decision Trees

###### AKA, 'Boosting Cancer Rates' (teachers didn't approve)


## Motivation

My Galvanize capstone project is to investigate environmental factors and cancer rates in California counties from 2001 to 2012 using supervised learning techniques, specifically looking into types of gradient boosting. Boosting models are a go to base layer along with neural nets for most ensemble models in Kaggle competitions by Grand Masters. [6] This project will use different boosting models with different parameters to reduce root mean square error in test predictions. 2017 saw a new  boosting model hailing from Russian company Yandex called Catboost (Cat stands for Categorical); this model is supposed to compete well and even surpass XGBoost, the current all star.

Our environment plays a very important role in our life and thus our health. According to the WHO, as much as 24% of all disease is caused by environmental exposures that could have been averted. [5] New research keeps getting published about cancer and environmental pollution and some of this data is now being collected by government departments, especially in California. The Surveillance, Epidemiology, and End Results program (SEER) has about 10 million cases of cancer in their database ranging over 11 states, some starting in the 1970s. The last California counties to join this program (mandated by the state) happened in 2001 and since that year they have logged 2.5 million cancer incidents. This might seem like a lot for a state close to 40 million people, but the American Cancer Society states that 40% of American people will receive a diagnosis of cancer in their lifetime (½ of all men and ⅓ of all women). [4] Cancer rate is typically measured as incidents (new cases) per 100,000 and so will this project. This measure should not be confused with prevalence, total current cases. 

The first goal was to find the average yearly California incident rate per county. The histogram below is a plot of the different incidents and the average is 542 cases per 100,000, ranging from 200 to 1,000.

![Cancer Distribution Rate](https://github.com/DataDanD/CancerCapstone/blob/master/Graphs/Updated/CancerIncidents.png)



## Questions

- Can a supervised learning algorithm predict cancer rates at a county level?

- What model technique will give the lowest root mean squared error (RMSE)?

- What environmental factors will be important for prediction accuracy?

- Why do cancer rates differ in California counties? 

This following is a box plot demonstrating the variety of county cancer incidents within California.

![Cancer Box Plot](https://github.com/DataDanD/CancerCapstone/blob/master/Graphs/Updated/CountyCancer.png)


County Fips code is used in this project to keep county names simple. FIPS (Federal Information Processing Standard) Code is used by the government and is 5 digits when you concatenate the 2 digit code for the state ID and 3 digit code for the county. This numbering systems helps identify counties with the same name that are in different states by using a unique ID system. The term County Fips (and in some files C Fips) will be used in this project, as we are only looking at one state and the California code of 06 was delete from all data for the merging process. Link to [California Fips dictionary](https://www.weather.gov/hnx/cafips), if interested in certain location.



## Data

![Data Table](https://github.com/DataDanD/Cancer-Capstone-Portfolio/blob/master/Graphs/DataTable.png)

The table above contain information on all datasets in the final data frame that will be used for regression modeling. All data was at least grouped by county to help provide unique information in features, sadly any cool data without county level detail was deleted. Data labeled grouped by year is when when all 10 years in correct rage were available. Some data is the average of a few years and in the table is only considered grouped by county. Data is grouped by County Fips because, the SEER cancer data is report with the county level as the lowest denominator. Integers listed for columns and rows of each data source are recorded after filtering for California and for years (2001-2012) used in project. Unfortunately some of the main data used stopped in 2012, while other data is updated regularly. The number of columns the dataset provided for the final data frame is recorded in the feature column of the table.

Most data sources were thanks to government agencies and their open source files were typically located on data.gov. [1] Theses government files contain data collected from surveys, reported by companies, or are measured from an agency. A few data sources were found on [Kaggle.com](https://www.kaggle.com/) in their public dataset sharing section (as of today they have 10,833 files that can be downloaded). 

Accessing the SEER cancer data requires a [signed wavier](https://seer.cancer.gov/data/access.html), therefore I am not allowed to share the file. However, Cancer.csv is the final file and can be downloaded from the home page on this repository. It has the cancer incident vales the models are trying to predict as well as all the final features used to make these predictions. Final data frame is 627 rows with 28 columns, 27 features for the X value in scripts and the y value that is predicted is labeled 'Cancer Rate'. There are 58 counties in California and 11 years of data, there should be 638 rows, but one county was missing Radon data and was dropped from this experiment.

For more information and a link to each file used in Cancer.csv, check out [Data.md](https://github.com/DataDanD/Cancer-Capstone-Portfolio/blob/master/Data.md) on the home page.


### Discared Data Section

(In progress)







## Pipeline

### Preprocessing 

1) Find useful environmental and socioeconomic public datasets, in any format
2) Turn all downloaded files into data frames with Pandas, an awesome Python package
3) Exploratory Data Analysis (EDA) to see if file has usable features to use in modeling
4) Remove any inappropriate states and/or years, but keep all columns for now
5) Save info as CSV file for a checkpoint incase of future problems or to reference
6) Decide on appropriate columns for modeling process, drop features that will not be used 
7) Group data by county and by year when possible to get rows ready for merge
8) Group spare features with count or sum when to many exist (group chems by carcinogen, sum pounds)
9) Pivot columns that have multiple features into separate columns, drop new features that are not needed)
10) Match County Fips, delete 6000 to lose state ID from ints or change strings to match Fips file and merge #
11) Merge final (14) data frames to SEER data to create Cancer.csv (merge to the left each time of C Fips)
12) Feature engineering and more filtering to prevent multicollinearity and data leakage for good modeling

### Modeling

1) Get base measure with a grid searched (3 boolean parameters) linear regression model 
2) Look into performance of Sk-Learn regression models & boosting packages (XGBoost, CatBoost, LightGBM)
3) Study different models to see how they using the data to make cancer incident predictions
4) Grid search on models with low RMSE to find best parameters and finally the best model 
5) Get feature importance with recursive feature selection to see what data is most useful



## EDA (Exploitory Data Analysis)

### (UNDER CONSTRUCTION) Meet Some of the Lucky Features

These next links will take you to on a trip to Jupyter Notebooks where we can explore files before the merge.

(Links have eda and basic graphs, adding description for each kernel later)

#### TRI

[Toxic Inventory Release (TRI)](https://github.com/DataDanD/Cancer-Capstone-Portfolio/tree/master/Jupyters)

#### EPA Air Quality

[Air Quality](https://github.com/DataDanD/Cancer-Capstone-Portfolio/tree/master/Jupyters) 

#### Radon

[Radon Averages](https://github.com/DataDanD/Cancer-Capstone-Portfolio/tree/master/Jupyters)

#### Fracking Wells

[Fracking Wells](https://github.com/DataDanD/Cancer-Capstone-Portfolio/tree/master/Jupyters)

#### Supefund Sites

[Superfund Sites](https://github.com/DataDanD/Cancer-Capstone-Portfolio/tree/master/Jupyters)

#### SEER Cancer & Census

[SEER + Census](https://github.com/DataDanD/Cancer-Capstone-Portfolio/tree/master/Jupyters)








### (UNDER CONSTRUCTION) EDA in Final project 

Now we will explore all the features that have successfully passed the merge to the final dataframe.

First up is an image of a heatplot (also called "plasma soup" by an extremely select few) this will show us column relationships, in the form of correlations, in all of the data. Lighter and darker (positive and negative correlations, respectively) boxes on the graph are usually not a good thing. Exceptions currently include: diagonal in the middle where features intersect with themselves (100% correlation!) and the rows/columns with 'Count' and 'Cancer Rate'. They should honestly be removed from this graph as they are not features used in prediction. (Will fix in future, maybe; I mean it is cool to see what they relate to as well) 'Count' was used to make 'Cancer Rate' by dividing the cancer count by population in same county and year, then multiplied by 100,000.

We only have to look at half of the plasma soup graph to understand all the correlations, as features will intersect with all other features twice. Pick one side of the diagonal to aviod looking at the same thing twice.

![Heatmap of All Features](https://github.com/DataDanD/CancerCapstone/blob/master/Graphs/heatmap.png)

Interesting... Looks like I have more work to do. This might take awhile.

What correlates?



#### (UNDER CONSTRUCTION)

Positve: 
A county with high value in feature_1 likly has high value in feature_2, or low and low values, when feature_1 and feature_2 have positive correlation. This is represented as light color in graph above.

Negative: 
Reverse of positive,
as feature_1 increases, feature_2 decreases, when negative correltation exist between the two features.
(lower and higher, higher and lower)



Top left - positive correlation box:

Ozone, 
PM2.5, 
Population, and
Count

Okay, Ozone and PM2.5 is obvious as well as incident count and population.

Makes some sense that places that have more people have worse air pollution

Stay away from people

Ozone, more correlation to cancer rate

PM2.5, more correlation with count and pop




Middle of graph - lots of positive and negative relations:

Education,
Median Income,
Poverty,
Unemployment,
Uninsured,
Alcohal (spelled wrong),
Health Status,
Unhealthy Days

Yup, these all measure socioeconimic status of the popultion 

Education and Income: Positive

Education, Poverty, Unemploted: Negative

Keep?
Drop?



Bottom Right - positive correlations: 

Elder Medicare, 
Disabled Medicare, 
Work Disabled, 
Drug Use, 
Major Depression

What drugs are the elders on?

Work or Medicare disabled?




Other:

Median Income & Disabled Medicare:
Negative,
High income less disabled

Drug Use and Year??:
Negative,
Year goes up use goes down.
Is drug use going down in California?

Major Depression and Cancer Rate -  Huh? 
Positive,
What comes first?




The features that correlate to other features is call multicolinearity 

not a good thing for machine learning algorithms. 

Why are correlated features bad? 

Explain why multicolinearity or link to?

What should we do to correlated features?





However, on a good note, we can see some correlations between cancer incidents and features in the heatmap

Good: Cancer Rate and Medicare (/Uninsured)
Positive
Makes sense
Older population more cancer
Not many young people get cancer compared to our elders





we can look at some of these variables closer with a pairplot. 

(Pair plot explaination)
(high and low rates)
(Why these variables)


![Pair Plot](https://github.com/DataDanD/CancerCapstone/blob/master/Graphs/Updated/Pair4.png)



(Major depression and cancer incidents)
(Explain Data Leakage)





## (UNDER CONSTRUCTION) Models

We will start with a normal linear regression gridsearched, as a baseline for the other models. The gridsearch found that setting the 3 parameters to fit_intercept=True, normalize=False, and copy_X=True will yeild the best RMSE score. Below is a histogram with cancer incident rates in the test data colored green and the model prediction for these same test values in blue.

![Lin Predicting](https://github.com/DataDanD/CancerCapstone/blob/master/Graphs/Updated/Lin.png)

#### (UNDER CONSTRUCTION)

(talk about scripts for each model)

(Graph is from Lin.py script)

(Explain RMSE and MAE in the graph)

Not bad, but lets see how well boosting can perform with predicting these cancer rates. 
Next, up Random forest, gradient boosting, addaboost, and catboost with default parameters. 
Then we can compare the best model to XGBoost the current king of the boosting algorithms.



### Overview of Models

(In progress)


### (UNDER CONSTRUCTION) Feature Importance and Default Scores

Feature importance in these tree models refers to where splits of the tree happen. Splits are decided based on how well the model can best gain information. (reduce loss function and RMSE)

The horizontal histograms below uses default parameters for each model. 
calculated feature relevance and scores for RMSE and MAE


![Boosting Models Rel](https://github.com/DataDanD/Cancer-Capstone-Portfolio/blob/master/Graphs/PosterBoosting.png)







## (UNDER CONSTRUCTION) Results


(XGB vs GB vs Cat?)

(Gridsearch explaination)

(AWS Cat)(EC2(S3)


gridsearch parameters Gradient Boosting
parameters =

     'max_depth':[3], #[2,3,4,5,6,7,8]
     
     'max_features':['auto'], #['sqrt','log2','auto']
     
     'min_samples_leaf':[4], #[1,2,3,4,5]
     
     'min_samples_split':[2], #[2,3,4,5]
     
     'n_estimators': [1600] #[600,900,1100,1200,1300,1400,1500,1600]
     

(Best GB parameters)

(same as lin plot above)
(actual test data and model predications)




![distribution predictions (Boosting)](https://github.com/DataDanD/Cancer-Capstone-Portfolio/blob/master/Graphs/PosterPredicting.png)




(recursive feature selection)
(What does graph mean)
RMSE change

![Feature importance](https://github.com/DataDanD/Cancer-Capstone-Portfolio/blob/master/Graphs/PosterImportance.png)







## Discussion

(Add to section)

This project was supposed to look at specific chemicals from the Toxic Release Inventory data from the EPA and specific cancers, but the data was sparse and not all toxins released into our environment have to be reported. Adding socioeconomic data made the model more accurate and reliable. The rows with the smaller counties could have been dropped, then it would have be possible to add more features: BMI, blood pressure, smoking. Fracking wells and superfund sites information would have performed better, if the cancer data was mapped to an area smaller than the county level. There may be some data leakage with major depression, as cancer can lead to depression. CatBoost / XGBoost / LightGB could have been good alternatives to gradient boosting, but they take longer to gridsearch for optimal parameters and implement.

![Cancer and Medicare](https://github.com/DataDanD/CancerCapstone/blob/master/Graphs/Updated/CanInMedPop.png)


(talk about feature location problem)
The Fracking Wells and Superfund Sites data that researchers scrapped from the web and uploaded to Kaggle has GPS coordinates, but it is impossible to tell which SEER patients in those counties lived closer to these locations.








## Conclusion 

(Add to section)

Boosting works with this regression problem. The final model has variance of +/- 5 RMSE. Medicare population and county FIPS are the features that matter the most in predicting cancer incidence rates for these models. More data is needed to determine relationships between diseases and the environment. 





### Future Steps

1) Complete (EDA, Models, Results, Discussion, Conclusion)

2) Update graphs, add others (EDA)

3) Clean all folders

4) Add prequel and turn up fun

4) Add links (Use refference links on page)

5) EDA in Jupyter Notebooks explained

6) Partial Dependency Plots to EDA section (script written) link script

7) Bayesian Probabilistic Modeling with PyMC3 (link to Bayesian understanding)







## References

[1] https://www.data.gov/

[2] https://seer.cancer.gov/data/

[3] https://www.epa.gov/

[4] https://www.cancer.org/cancer/cancer-causes.html

[5] http://www.who.int/mediacentre/news/releases/2006/pr32/en/ 

[6] http://blog.kaggle.com/2017/01/23/a-kaggle-master-explains-gradient-boosting/ 
