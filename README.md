# CancerCapstone

Multilevel investigation into environmental factors and cancer rates in California

Data:
1) SEER (Survailance Epidemiology and End Results program)
2) TRI (Toxic Release Inventory)
3) EPA Air Quality
4) Fracking Sites
5) SuperFund Sites
6) Radon Levels
7) Diseases
8) Census Demographic Populations

Models:
1) Linear Regression
2) Carboost Regression
3) Hierarchical Model
4) Probabilistic Model
3) LSTM

Filter all data for California
Limit years to 2001 to 2012 to avoid missing values
remove population under a certain quantity
group dataframes by year, county, age, race and sex
merge data on same list to one frame
create models
