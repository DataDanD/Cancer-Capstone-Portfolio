# Calculating Cancer Rates with Boosted Decision Trees


## Motivation

My Galvanize capstone project is to investigate environmental factors and cancer rates in California counties from 2001 to 2012 using supervised learning techniques, specifically looking into types of gradient boosting. Boosting models are go to base layer along with neural nets for most ensemble models in Kaggle competitions by Grand Masters. [6] This project will use different boosting models with different parameters to reduce root mean square error in test predictions.
Our environment plays a very important role in our life and thus our health. According to the WHO, as much as 24% of all disease is caused by environmental exposures that could have been averted. [5] 40% of people will receive a diagnosis of cancer in their lifetime (½ of all men and ⅓ of all women). [4] Cancer rate is typically measured as incidents (new cases) per 100,000.  Yearly California counties have an average of 540 incidents per 100,000.

![Cancer Distribution Rate](https://github.com/DataDanD/CancerCapstone/blob/master/Graphs/Updated/CancerIncidents.png)


## Questions

-Can a supervised learning algorithm predict cancer rates at a county level?

-What model technique will give the lowest root mean squared error (RMSE)?

-What environmental factors will be important for predicting accuracy?

-Why do cancer rates differ widely in California countries?


![Cancer Box Plot](https://github.com/DataDanD/CancerCapstone/blob/master/Graphs/Updated/CountyCancer.png)


## Data

![Data Table](https://github.com/DataDanD/Cancer-Capstone-Portfolio/blob/master/Graphs/DataTable.png)

For more info on each datasets used, including a link to each source, please click [here](https://github.com/DataDanD/Cancer-Capstone-Portfolio/blob/master/Data.md).

Most datasets were collected from open source government data at data.gov. [1] Data is from surveys, reported by  companies, or collected from government agencies. The columns and rows in the table above are recorded after filtering for California and for years 2001-2012. Cancer data requires a signed form so I am not adding a folder for each file, but final.csv is on home page. Final date frame is 627 rows with 28 columns (y = Cancer Rate, drop Count)


## Preprocessing

1) Find useful public datasets (any format: csv, text, fwf)
2) Filter data for appropriate features
3) Group by year and county
4) Pivot columns as needed
5) Merge 14 data frames to cancer data
6) Feature engineering + more filtering
7) Sk-Learn regression models & other boosting
8) Grid search parameters for lowest RMSE on select models


## EDA 

[Air Quality](https://github.com/DataDanD/Cancer-Capstone-Portfolio/tree/master/Jupyters) / [Fracking](https://github.com/DataDanD/Cancer-Capstone-Portfolio/tree/master/Jupyters) / [Superfunds](https://github.com/DataDanD/Cancer-Capstone-Portfolio/tree/master/Jupyters) / [Radon](https://github.com/DataDanD/Cancer-Capstone-Portfolio/tree/master/Jupyters) / [TRI](https://github.com/DataDanD/Cancer-Capstone-Portfolio/tree/master/Jupyters)
[Cancer Rates and Graphs](https://github.com/DataDanD/Cancer-Capstone-Portfolio/tree/master/Jupyters)

We can see some nice correlations

![Heatmap of All Features](https://github.com/DataDanD/CancerCapstone/blob/master/Graphs/heatmap.png)

![Pair Plot](https://github.com/DataDanD/CancerCapstone/blob/master/Graphs/Updated/Pair4.png)


## Models

I will start with a normal linear regression gridsearched, as baseline.

![Boosting Models](https://github.com/DataDanD/CancerCapstone/blob/master/Graphs/Updated/Lin.png)

feature importance on boosting with default parameters

![Boosting Models](https://github.com/DataDanD/Cancer-Capstone-Portfolio/blob/master/Graphs/PosterImportance.png)


## Results

I picked gradient boosting because catboost takes way longer to gridsearch.

gridsearch parameters Gradient Boosting
parameters = {

     'max_depth':[3], #[2,3,4,5,6,7,8]
     
     'max_features':['auto'], #['sqrt','log2','auto']
     
     'min_samples_leaf':[4], #[1,2,3,4,5]
     
     'min_samples_split':[2], #[2,3,4,5]
     
     'n_estimators': [1600] #[600,900,1100,1200,1300,1400,1500,1600]
}

[distribution predictions (Boosting)](https://github.com/DataDanD/Cancer-Capstone-Portfolio/blob/master/Graphs/PosterPredicting.png)

[Feature importance](https://github.com/DataDanD/Cancer-Capstone-Portfolio/blob/master/Graphs/PosterImportance.png)


## Discussion

This project was supposed to look at specific chemicals from the Toxic Release Inventory data from the EPA and specific cancers, but the data was sparse and not all toxins released into our environment have to be reported. Adding socioeconomic data made the model more accurate and reliable. The rows with the smaller counties could have been dropped, then it would have be possible to add more features: BMI, blood pressure, smoking. Fracking wells and superfund sites information would have performed better, if the cancer data was mapped to an area smaller than the county level. There may be some data leakage with major depression, as cancer can lead to depression. CatBoost / XGBoost / LightGB could have been good alternatives to gradient boosting, but they take longer to gridsearch for optimal parameters and implement.

![Cancer and Medicare](https://github.com/DataDanD/CancerCapstone/blob/master/Graphs/Updated/CanInMedPop.png)
[Major Depression rate and Cancer Rate]


## Conclusion 

Boosting works with this regression problem. The final model has variance of +/- 5 RMSE. Medicare population and county FIPS are the features that matter the most in predicting cancer incidence rates for these models. More data is needed to determine relationships between diseases and the environment. 


### Future Steps

EDA in Jupyter Notebooks explained

Partial Dependency Plots EDA (script written)

Bayesian Probabilistic Linear Model (pymc3)

Clean graph folder


## References
[1] https://www.data.gov/

[2] https://seer.cancer.gov/data/

[3] https://www.epa.gov/

[4] https://www.cancer.org/cancer/cancer-causes.html

[5] http://www.who.int/mediacentre/news/releases/2006/pr32/en/ 

[6]http://blog.kaggle.com/2017/01/23/a-kaggle-master-explains-gradient-boosting/ 

