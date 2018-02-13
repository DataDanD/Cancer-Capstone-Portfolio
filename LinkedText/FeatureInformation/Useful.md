# Lucky Features in Jupyter Explorations

Links in section will take you on trip to a Jupyter Notebook 
where we will explore one (one has two) file(s) at a time before the merge.

## SEER (Surveillance Epidemiology and End Results):
### Overview
Up first and most importantly for this project is cancer incidents (cases) 
as well as population from the SEER database.
Other features can be dropped, but this is the value our models are predicting.
Both data sets downloaded from SEER website.

#### Cancer File
Cancer data had 132 columns about the cancer, but no data about the person. 
Lifestyle information would be very, very useful in finding activities that relate to cancer. 
Most of cancer data was not used and lost when grouping rows by year and county for final merge.
Originally project grouped cancer data  by county, year, age, race, and sex.
Another project could keep cancer types to see how different features relate to different cancers.

#### Population Data
Population had many rows due to populations in initial frame already split by county, year, age, race, and sex.
Summed rows with same county and year to create file that was used in merge for modeling process.
EDA in next link has both population and cancer grouped by county, year, age, race, and sex.
If project was redone, would be cool to keep population data split by age, race, and sex 
to see how different features affect population segments differently.

### Creating Target Variable
Feature Engineering: 
###### **(LINK)**
Cancer Rate (new column) = Cancer Incidents / Population * 100,000 
- after grouping by county and year, 
summing column values of incidents and population in combining rows.

### Exploration
Last graph is favorite - sum of different cancer types, sorted high to low in horizontal bar plot.
Graphs with time on X axis: average age, cancer incident counts, cancer rate (grouped by year, county, sex, age, race).

[Cancer + Population](https://github.com/DataDanD/Cancer-Capstone-Portfolio/blob/master/Jupyters/CanRate%20EDA.ipynb)


## Toxic Inventory Release (TRI)
### Overview
The first data source and was hoping to only link different cancers to different chemicals.
Each year was a file, step one was merging to single csv.
Multi chemical names (structure name) for each chemical, made data spare and cleaning would have taken days.

### Processing
In the end rows were grouped by year, county, and column with Carcinogen or Not Carcinogen label.
Pounds of chemicals were summed in the grouping.
Maybe should have summed all chemicals by pounds and not worried about carcinogen label.

### Exploration
Interesting to look at companies, chemicals, and counties with most pounds released.

[TRI](https://github.com/DataDanD/Cancer-Capstone-Portfolio/blob/master/Jupyters/TRI%20EDA.ipynb)

### Discussion
Sad that some companies do not have to report chemicals released into our environment to the Environmental Protection Agency (EPA). 
We do not know the percentage of chemicals that are reported. 
Making the accuracy of is this data questionable.


## EPA Air Quality
### Overview
Air pollution has been measured very well by our government dating back to the 1980s. 
One of the states with higher air pollution is California, 
containing some of the most polluted counties in the United States.

### Processing
The data had ten measurement IDs and values for every year and county.
In EDA realized measurement IDs were looking at the same topics multiple times, 
but with different units: counts (days vs human days), percentages, and standardized/ non-standardized values.
Only two air pollution problems were being measured - Ozone and PM2.5,
arguably the two most important.

### Exploration
[Air Quality](https://github.com/DataDanD/Cancer-Capstone-Portfolio/blob/master/Jupyters/Air%20EDA.ipynb) 


## Radon
### Overview
Radon data was scrapped on the web from Columbia University.
Years did not match full time range so an average of the listed years average county radon level was calculated to keep feature.
One county was missing radon information and that county was dropped from experiment.

### Exploration
Interesting to see the different averages, and understandable as California is a larger state.

[Radon Averages](https://github.com/DataDanD/Cancer-Capstone-Portfolio/blob/master/Jupyters/Rad%20EDA.ipynb)

### Discussion
Would have been nice to see a standard deviation of radon as well. 
Highest average was 2.5 and values over 4 pico-curies per liter are considered unhealthy.


## Fracking Wells & Superfund Sites
### Overview
Both downloaded on Kaggle.com after nice people scrapped/queried, transformed, and uploaded data.
Files included GPS coordinates of the facilities, but were not usable as all other data was at county level.
Almost too much data to explore in files, one having over 500 rows with different chemical metrics.

### Processing
In the end the merged file only kept count of locations in county for both files. 
This is because start years were not listed. 
There could have been more superfund sites in past, but data not easily available.

### Exploration
#### Frack
Top fracking county had over 3000 sites and second highest county had 33.
Most California counties didn't have fracking wells.
Some counties had fracking wells on uninhabited islands off their California cost.

[Fracking Wells](https://github.com/DataDanD/Cancer-Capstone-Portfolio/blob/master/Jupyters/Frack%20EDA.ipynb)

#### Super
15 and 13 superfund sites in a county were the highest values in this set.
Most counties having between 1 and 5 of these very polluted sites.

[Superfund Sites](https://github.com/DataDanD/Cancer-Capstone-Portfolio/blob/master/Jupyters/Super%20EDA.ipynb)


## Merged Notebook
### Overview
This notebook was created after merge and contain higher quality graphs that were potential candidates for poster and GitHub.

### Exploration
Contains (in order):
- Histogram with KDE of Incidents in first section
- Scatter plots of features correlated to Cancer Rate
- Boxplots of Fracking, Superfund, and Cancer Incidents
- Heatmaps, one in project and smaller ones investigating values
- Probability plots of data against quantiles of normal distribution

[graphs](https://github.com/DataDanD/Cancer-Capstone-Portfolio/blob/master/Jupyters/Graphs%20EDA.ipynb)


