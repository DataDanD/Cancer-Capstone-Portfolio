# Boosting Cancer Rates

## Motivation

My Galvanize capstone project is to investigate environmental factors and cancer rates in California counties from 2000 to 2014 using supervised learning techniques. Boosting techniques are popular in the data science community and are commonly used as a base model in most ensamble models that win Kaggle compititions. This project will use different boosting models with different parameters to reduce root mean square error in test predictions. 


### Preprocessing: (CleanGroup.py + Merge.py)
1) Filter Government data for California
2) Limit years after 2001 to avoid missing values
3) Remove populations under a certain quantity
4) Group dataframes by year and county (age, race and sex made data sparse)


### EDA (Jupyter Notebooks)
Why do different counties have higher cancer rates?

![Cancer Distribution Rate](https://github.com/DataDanD/CancerCapstone/blob/master/Graphs/Updated/CancerIncidents.png)


Some Counties have higher rates of cancer then others

![Cancer Box Plot](https://github.com/DataDanD/CancerCapstone/blob/master/Graphs/Updated/CountyCancer.png)


HeatMaps!

![Heatmap of All Features](https://github.com/DataDanD/CancerCapstone/blob/master/Graphs/heatmap.png)


Some Correlations dug into

![Pair Plot](https://github.com/DataDanD/CancerCapstone/blob/master/Graphs/Updated/Pair4.png)


As we can see in these graphs there are some correlations between some of the features and cancer rate

Cancer Rate and Medicare Rates Correlation

![Cancer and Medicare](https://github.com/DataDanD/CancerCapstone/blob/master/Graphs/Updated/CanInMedPop.png)



### Models (add scripts used here)

Gridsearched linear Model

![Boosting Models](https://github.com/DataDanD/CancerCapstone/blob/master/Graphs/Updated/Lin.png)

feature importance on default parameters

![Boosting Models](https://github.com/DataDanD/CancerCapstone/blob/master/Graphs/Updated/Boostrel4.png)


gridsearch parameters Gradient Boosting
parameters = {

     'max_depth':[3], #[2,3,4,5,6,7,8]
     
     'max_features':['auto'], #['sqrt','log2','auto']
     
     'min_samples_leaf':[4], #[1,2,3,4,5]
     
     'min_samples_split':[2], #[2,3,4,5]
     
     'n_estimators': [1600] #[600,900,1100,1200,1300,1400,1500,1600]
}


![Fin Models](https://github.com/DataDanD/CancerCapstone/blob/master/Graphs/Updated/Predict.png)





Recursive Feature Elimination (feature importance (Worked well for gradient boosting))

[(1, 'Carcinogen'), (1, 'Disabled Medicare'), (1, 'Drug Use'), (1, 'HIV'), (1, 'Hep B'), (1, 'Hep C'), (1, 'Major Depression'), (1, 'Medicare Population'), (1, 'Ozone'), (1, 'PM2.5'), (1, 'Population'), (1, 'Uninsured'), (1, 'Work Disabled'), (2, 'Not Carcinogen'), (3, 'Year'), (4, 'C Fips'), (5, 'Radon'), (6, 'Unemployed'), (7, 'Education'), (8, 'Health Status'), (9, 'Alcohol'), (10, 'Median Income'), (11, 'Unhealthy Days'), (12, 'Poverty'), (13, 'Fracking'), (14, 'Superfund')]
