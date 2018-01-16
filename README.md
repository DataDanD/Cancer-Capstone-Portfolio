# CancerCapstone

My Galvanize capstone project is to investigate environmental factors and cancer rates in California from 2000 to 2014 using a Bayesian Hierarchical Linear Regression Model.

Datasets and Source:
1) SEER (Survailance Epidemiology and End Results program)
    https://seer.cancer.gov/data/
2) TRI (Toxic Release Inventory)
    https://www.epa.gov/toxics-release-inventory-tri-program/tri-basic-data-files-calendar-years-1987-2016
3) EPA Air Quality
    https://aqs.epa.gov/aqsweb/airdata/download_files.html
4) Fracking Sites
    https://www.kaggle.com/frackinganalysis/fracking-well-chemical-disclosure-datasets
5) SuperFund Sites
    https://www.kaggle.com/srrobert50/federal-superfunds/data
6) Radon Levels
    http://www.stat.columbia.edu/~gelman/arm/examples/radon_complete/
7) Diseases
    https://data.chhs.ca.gov/dataset/infectious-disease-cases-by-county-year-and-sex
8) Census Demographic Populations
    https://seer.cancer.gov/popdata/download.html

Preprocessing:
1) Filter all data for California
2) Limit years after 2001 to avoid missing values
3) Remove populations under a certain quantity
4) Group dataframes by year, county, age, race and sex
5) Merge data on same columns that were used to group
6) Create models

Models:
1) Linear Regression
2) Hierarchical / Probabilistic Model
3) Catboost Regression
3) LSTM

