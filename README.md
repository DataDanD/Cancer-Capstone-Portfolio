# Boosting Cancer Rates

## Motivation

My Galvanize capstone project is to investigate environmental factors and cancer rates in California counties from 2000 to 2014 using supervised learning techniques.

### Preprocessing: (CleanGroup.py + Merge.py)
1) Filter Government data for California
2) Limit years after 2001 to avoid missing values
3) Remove populations under a certain quantity
4) Group dataframes by year and county (age, race and sex made data sparse)


### EDA (Jupyter Notebooks)
Why do different counties have higher cancer rates?

![Cancer Distribution Rate](https://github.com/DataDanD/CancerCapstone/blob/master/Graphs/CanDis.png)


Tableau Graph of cancer rates by county

![Cancer by County](https://github.com/DataDanD/CancerCapstone/blob/master/Graphs/cancerCA.png)


Some Counties have higher rates of cancer then others

![Cancer Box Plot](https://github.com/DataDanD/CancerCapstone/blob/master/Graphs/CanCounty.png)
![Cancer CA](https://github.com/DataDanD/CancerCapstone/blob/master/Graphs/CanCoun2.png)


Do Fracking Wells correlate to Cancer rates?

![Fracking in CA](https://github.com/DataDanD/CancerCapstone/blob/master/Graphs/FrackEDA2.png)
![Fracking and Cancer](https://github.com/DataDanD/CancerCapstone/blob/master/Graphs/Frack.png)


Do Superfund Sites correlate to Cancer rates?

![SuperfundSites in CA](https://github.com/DataDanD/CancerCapstone/blob/master/Graphs/SuperfundEDA.png)
![SuperfundSites and Cancer](https://github.com/DataDanD/CancerCapstone/blob/master/Graphs/Super.png)


HeatMaps!

![Heatmap of All Features](https://github.com/DataDanD/CancerCapstone/blob/master/Graphs/heatmap.png)
![Heatmap2](https://github.com/DataDanD/CancerCapstone/blob/master/Graphs/heat2.png)
![Heatmap2](https://github.com/DataDanD/CancerCapstone/blob/master/Graphs/heat3.png)


Some Correlations dug into
![Pair Plot](https://github.com/DataDanD/CancerCapstone/blob/master/Graphs/pair.png)

As we can see in these graphs there are some correlations between some of the features and cancer rate


Cancer Rate and Medicare Rates Correlation

![Cancer and Medicare](https://github.com/DataDanD/CancerCapstone/blob/master/Graphs/CanMed.png)



### Models (add scripts used here)

Add linear Model here



feature importance on default parameters

![Boosting Models](https://github.com/DataDanD/CancerCapstone/blob/master/Graphs/RelevanceBoost.png)


Add best model scores here? gridsearch parameters Catboost?

MAE 

RMSE 



Recursive Feature Elimination (feature importance (Worked well for gradient boosting))

[(1, 'Alcohol'), (1, 'C Fips'), (1, 'Disabled Medicare'), (1, 'Drug Use'), (1, 'HIV'), (1, 'Hep B'), (1, 'Hep C'), (1, 'Major Depression'), (1, 'Medicare Population'), (1, 'PM2.5'), (1, 'Population'), (1, 'Uninsured'), (1, 'Year'), (2, 'Ozone'), (3, 'Work Disabled'), (4, 'Median Income'), (5, 'Health Status'), (6, 'Not Carcinogen'), (7, 'Education'), (8, 'Radon'), (9, 'Fracking'), (10, 'Carcinogen'), (11, 'Unemployed'), (12, 'Superfund'), (13, 'Unhealthy Days'), (14, 'Poverty')]




![Medicare Map](https://github.com/DataDanD/CancerCapstone/blob/master/Graphs/medicareCA.png)

![Cancer by County](https://github.com/DataDanD/CancerCapstone/blob/master/Graphs/cancerCA.png)




