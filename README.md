# Boosting Cancer Rates

My Galvanize capstone project is to investigate environmental factors and cancer rates in California counties from 2000 to 2014 using supervised learning techniques.

Datasets and Source:
1) SEER (Survailance Epidemiology and End Results program)
    - https://seer.cancer.gov/data/
2) TRI (Toxic Release Inventory)
    - https://www.epa.gov/toxics-release-inventory-tri-program/tri-basic-data-files-calendar-years-1987-2016
3) EPA Air Quality
    - https://aqs.epa.gov/aqsweb/airdata/download_files.html
4) Fracking Sites
    - https://www.kaggle.com/frackinganalysis/fracking-well-chemical-disclosure-datasets
5) SuperFund Sites
    - https://www.kaggle.com/srrobert50/federal-superfunds/data
6) Radon Levels
    - http://www.stat.columbia.edu/~gelman/arm/examples/radon_complete/
7) Diseases
    - https://data.chhs.ca.gov/dataset/infectious-disease-cases-by-county-year-and-sex
8) Census Demographic Populations
    - https://seer.cancer.gov/popdata/download.html
9) Education Levels
    - https://catalog.data.gov/dataset/county-level-data-sets
10) Poverty Levels
    - https://catalog.data.gov/dataset/county-level-data-sets
11) Employment Levels
    - https://catalog.data.gov/dataset/county-level-data-sets
12) California Infections
    - https://data.chhs.ca.gov/dataset/infectious-disease-cases-by-county-year-and-sex
13) Community Health Status Indicators - Vunerable Populations
    - https://catalog.data.gov/dataset/community-health-status-indicators-chsi-to-combat-obesity-heart-disease-and-cancer
14) Community Health Status Indicators - Health Status
    - https://catalog.data.gov/dataset/community-health-status-indicators-chsi-to-combat-obesity-heart-disease-and-cancer
15) Community Health Status Indicators - Insurance information
    - https://catalog.data.gov/dataset/community-health-status-indicators-chsi-to-combat-obesity-heart-disease-and-cancer
16) State County FIPS Codes
    - https://catalog.data.gov/dataset/fips-county-code-look-up-tool

## Preprocessing: (CleanGroup.py + Merge.py)
1) Filter Government data for California
2) Limit years after 2001 to avoid missing values
3) Remove populations under a certain quantity
4) Group dataframes by year and county (age, race and sex made data sparse)
5) Merge data on same columns that were used to group

## EDA (Jupyter Notebooks)
Why do different counties have higher cancer rates

![Cancer Distribution Rate](https://github.com/DataDanD/CancerCapstone/blob/master/Graphs/CanDis.png)
![Cancer by County](https://github.com/DataDanD/CancerCapstone/blob/master/Graphs/cancerCA.png)
![Cancer Box Plot](https://github.com/DataDanD/CancerCapstone/blob/master/Graphs/CanCounty.png)
![Cancer CA](https://github.com/DataDanD/CancerCapstone/blob/master/Graphs/CanCoun2.png)
![Fracking in CA](https://github.com/DataDanD/CancerCapstone/blob/master/Graphs/FrackEDA2.png)
![Fracking and Cancer](https://github.com/DataDanD/CancerCapstone/blob/master/Graphs/Frack.png)
![SuperfundSites in CA](https://github.com/DataDanD/CancerCapstone/blob/master/Graphs/SuperfundEDA.png)
![SuperfundSites and Cancer](https://github.com/DataDanD/CancerCapstone/blob/master/Graphs/Super.png)
![Heatmap of All Features](https://github.com/DataDanD/CancerCapstone/blob/master/Graphs/heatmap.png)
![Heatmap2](https://github.com/DataDanD/CancerCapstone/blob/master/Graphs/heat2.png)
![Heatmap2](https://github.com/DataDanD/CancerCapstone/blob/master/Graphs/heat3.png)

![Heatmap2](https://github.com/DataDanD/CancerCapstone/blob/master/Graphs/pair.png)
As we can see in these graphs there are some correlations between some of the features and cancer rate

Cancer Rate and Medicare Rate
![Cancer and Medicare](https://github.com/DataDanD/CancerCapstone/blob/master/Graphs/CanMed.png)
Cancer Rate and Major Depression
![Cancer and Medicare](https://github.com/DataDanD/CancerCapstone/blob/master/Graphs/CanDep.png)

## Models 
feature importance on default parameters
![Boosting Models](https://github.com/DataDanD/CancerCapstone/blob/master/Graphs/BoostingImportance.png)
XGBoost feature importance
A decision tree
learning rate
risiduals



