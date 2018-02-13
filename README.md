# Calculating Cancer Rates with Boosted Decision Trees

###### AKA, 'Boosting Cancer Rates'


## ***Content Table***

* [Motivation](#motivation)
* [Data](#data)
* [Pipeline](#pipeline)
* [EDA](#EDA)
* [Models](#models)
* [Results](#results)
* [Discussion](#discussion)
* [Conclusion](#conclusion)
* [References](#references)



## Motivation

This is a Galvanize capstone project investigating environmental factors and cancer rates in California counties from 2001 to 2012 using supervised learning techniques, specifically looking into types of gradient boosting. Boosting models are a go to base layer along with neural nets for most ensemble models in Kaggle competitions by Grand Masters. [6] This project will use different boosting models with different parameters to reduce root mean square error in test predictions. 2017 saw a new  boosting model hailing from Russian company Yandex called Catboost (Cat stands for Categorical); this model is supposed to compete well and even surpass XGBoost, the current all star.

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

Originally the cancer and population data was also grouped by County, Year, Race, Sex, and Age. This was to find out if any features affected segments of the population differently. Upon analysis, some of the cancer incident rates became extremely large. Two rows in particular had 100,000 cancer incidents per 100,000 people due to 1 person being in that row along with 1 new case of cancer for that year. Rather than setting a population cut off and removing rows under that value to reduce skewed rates, data was only grouped by year and county. This allowed us to hold on to all cancer incidents and total population for each county.

![Data Table](https://github.com/DataDanD/Cancer-Capstone-Portfolio/blob/master/Graphs/DataTable.png)


The table above contain information on all datasets in the final data frame that will be used for regression modeling. All data had to at least be grouped by county ('C') to help provide unique information in features, sadly any cool data without county level detail was deleted. Data labeled grouped by year ('Y') is only when all 10 years of correct rage were available. Some data is the average of a few years and in the above table is only considered grouped by county. Data is grouped by County Fips because, the SEER cancer data needed for project is report with county as the lowest denominator, no zip codes or town names were provided. Integers listed for columns and rows of each data source are recorded after filtering for California and for years (2001-2012) used in project. Unfortunately some of the main data used stopped in 2012, while other data is updated regularly. The number of columns the dataset provided for the final data frame is recorded in the feature column of the table.

Most data sources were thanks to government agencies and their open source files were typically located on data.gov. [1] Theses government files contain data collected from surveys, reported by companies, or are measured from an agency. A few data sources were found on [Kaggle.com](https://www.kaggle.com/) in their public dataset sharing section (as of today they have 10,833 files that can be downloaded). 

Accessing the SEER cancer data requires a [signed wavier](https://seer.cancer.gov/data/access.html), therefore I am not allowed to share the file. However, Cancer.csv is the final file and can be downloaded from the home page on this repository. It has the cancer incident vales the models are trying to predict as well as all the final features used to make these predictions. Final data frame is 627 rows with 28 columns, 27 features for the X value in scripts and the y value that is predicted is labeled 'Cancer Rate'. There are 58 counties in California and 11 years of data, there should be 638 rows, but one county was missing Radon data and was dropped from this experiment.

For more information and a link to each file used in Cancer.csv, check out [Data.md](https://github.com/DataDanD/Cancer-Capstone-Portfolio/blob/master/Data.md) on the home page.

###### **(LINK TO DISCARED DATA)**

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



## EDA

###### **(LINKED TO SINGLE FEATURE ANALYSIS)**

### Merged Data EDA 

Now we will explore all the features that have successfully passed the merge to the final dataframe.

First up is an image of a heatplot (also called "plasma soup" by an extremely select few) this will show us column relationships, in the form of correlations, in all of the data. Lighter and darker (positive and negative correlations, respectively) boxes on the graph are usually not a good thing. Exceptions currently include: diagonal in the middle where features intersect with themselves (100% correlation!) and the rows/columns with 'Count' and 'Cancer Rate'. They should honestly be removed from this graph as they are not features used in prediction. (Will fix in future, maybe; I mean it is cool to see what they relate to as well) 'Count' was used to make 'Cancer Rate' by dividing the cancer count by population in same county and year, then multiplied by 100,000.

Note: only have to look at half of plasma soup graph below to understand all the correlations. Features will intersect with all other features twice. Pick a side of light colored diagonal to avoid seeing relations twice.

![Heatmap of All Features](https://github.com/DataDanD/CancerCapstone/blob/master/Graphs/heatmap.png)


Interesting... Looks like I have more work to do. This might take awhile.

So, what correlates?

###### **(LINKED TO CORRELATION SECTION)**


#### Heatmap Analysis

Features from same source are next to each other, 
plus types (pollution, economic, infections) of data added around same time.
This creates boxed areas on the map to have larger relations.

Positive correlation area in top left and bottom right.
Middle has both types of correlations, very dark and very light boxes.
Other interesting feature relation worth exploring


###### **(LINKED TO ALL HEATMAP) (links heatmap section in above section)**

###### **(LINKED TO MULTICOLLINEARITY | FEATURE SELECTION | FEATURE ENGINEERING)**


#### Pairplot

we can look at some of these variables closer with a pairplot. 

A pairplot is similar to a heatmap, but uses scatter plots and histograms to show correlations, rather than a colored box.
In the graph below counties with cancer rate above average are colored green and below average are in blue.
We cannot use every feature in this graph as that would be hectic too much information to digest.
The features selected were of interest.

![Pair Plot](https://github.com/DataDanD/CancerCapstone/blob/master/Graphs/Updated/Pair4.png)



## Models

### Linear Regression Model

We will start with a normal linear regression gridsearched, as a baseline for the other models. The gridsearch found that setting the 3 parameters to fit_intercept=True, normalize=False, and copy_X=True will yeild the best RMSE score. Below is a histogram with cancer incident rates in the test data colored green and the model prediction for these same test values in blue.

![Lin Predicting](https://github.com/DataDanD/CancerCapstone/blob/master/Graphs/Updated/Lin.png)


(link to script)

Root Mean Squared Error means the average length the predictions are off from the real value in the test data.
With the average cancer incidents being about 540, being 60 people off isn't terrible.



### Overview of Boosted Regression Models

Not bad, but lets see how well different types of decision tree algorithms can perform with predicting these cancer rates. 

#### Model Education

###### **(LINKED TO PACKAGES FOR MODELS)**

###### **(LINKED TO FULL MODEL OVERVIEW)**

Regression models are a commonly used type of machine learning algorithms and used for predicting numerical or continuous values.


###### **(LINKED TO UNDERSTANDING SCORES)**

### Feature Importance 

Default Values


Feature importance in these tree models refers to where splits of the tree happen. Splits are decided based on how well the model can best gain information. (reduce loss function and RMSE)

The horizontal histograms below uses default parameters for each model. 
calculated feature relevance and scores for RMSE and MAE


![Boosting Models Rel](https://github.com/DataDanD/Cancer-Capstone-Portfolio/blob/master/Graphs/PosterBoosting.png)

(link to script)



### Gridsearch

(Explain)

gridsearch parameters Gradient Boosting
parameters =

     'max_depth':[3], #[2,3,4,5,6,7,8]
     
     'max_features':['auto'], #['sqrt','log2','auto']
     
     'min_samples_leaf':[4], #[1,2,3,4,5]
     
     'min_samples_split':[2], #[2,3,4,5]
     
     'n_estimators': [1600] #[600,900,1100,1200,1300,1400,1500,1600]
     

(Best GB parameters)
(link to script)




## Results

(UNDER CONSTRUCTION) 

### Final Model Selection

Gradient boosting, speed accuracy and usability. 
Catboost long to gridsearch, even in AWS (S3)
XGBoost had good results (not as friendly as GB)


### Final Model Predictions

(same graph as linear plot above)
(actual test data and model predications)

![distribution predictions (Boosting)](https://github.com/DataDanD/Cancer-Capstone-Portfolio/blob/master/Graphs/PosterPredicting.png)

(link to script)

Compare to Linear baseline



#### Feature Relevance

Recursive Feature Selection

Used to find feature importance.
(What does graph mean)
RMSE change

![Feature importance](https://github.com/DataDanD/Cancer-Capstone-Portfolio/blob/master/Graphs/PosterImportance.png)

(link to script)






## Discussion

(UNDER CONSTRUCTION) 

This project was supposed to look at specific chemicals from the Toxic Release Inventory data from the EPA and specific cancers, but the data was sparse and not all toxins released into our environment have to be reported. Adding socioeconomic data made the model more accurate and reliable. The rows with the smaller counties could have been dropped, then it would have be possible to add more features: BMI, blood pressure, smoking. Fracking wells and superfund sites information would have performed better, if the cancer data was mapped to an area smaller than the county level. There may be some data leakage with major depression, as cancer can lead to depression. CatBoost / XGBoost / LightGB could have been good alternatives to gradient boosting, but they take longer to gridsearch for optimal parameters and implement.

![Cancer and Medicare](https://github.com/DataDanD/CancerCapstone/blob/master/Graphs/Updated/CanInMedPop.png)


(talk about feature location problem)
The Fracking Wells and Superfund Sites data that researchers scrapped from the web and uploaded to Kaggle has GPS coordinates, but it is impossible to tell which SEER patients in those counties lived closer to these locations.








## Conclusion 

(UNDER CONSTRUCTION) 

Boosting works with this regression problem. The final model has variance of +/- 5 RMSE. Medicare population and county FIPS are the features that matter the most in predicting cancer incidence rates for these models. More data is needed to determine relationships between diseases and the environment. 






### Next Steps

1) Complete (EDA, Models, Results, Discussion, Conclusion)
   Table of contents
   Add scripts in pipeline?

2) Update graphs, add others (EDA)
   Clean folders

3) Add links: use links on page, add all links in paper to reference section

4) Improve EDA in pre-merged Jupyter Notebooks

5) Partial Dependency Plots to EDA section (script written) link script
   Bayesian Probabilistic Modeling with PyMC3 (link to Bayesian understanding)




## References

[1] https://www.data.gov/

[2] https://seer.cancer.gov/data/

[3] https://www.epa.gov/

[4] https://www.cancer.org/cancer/cancer-causes.html

[5] http://www.who.int/mediacentre/news/releases/2006/pr32/en/ 

[6] http://blog.kaggle.com/2017/01/23/a-kaggle-master-explains-gradient-boosting/ 

[7] https://www.nasa.gov/content/goddard/nasa-scientists-relate-urban-population-to-air-pollution/

[8] https://www.cancer.gov/about-cancer/causes-prevention/risk/age
