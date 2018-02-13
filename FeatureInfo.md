# Project Features:

## Discarded Data
(Sad section for me)

A couple times after finding relevant data, it didn't have county level information or was too sparse (missing many values) to use. Missing pieces in these tables are called null values, and too many null values makes the data sparse. It is possible to fill null values, the easiest and most well known is using mean/median values within that column. However, a few [other techniques](https://www.omicsonline.org/open-access/a-comparison-of-six-methods-for-missing-data-imputation-2155-6180-1000224.pdf) have been reported to outperform mean/median are more complicated. [reference article linked above]

This project completely avoided filling missing values by deleting data sets and dropping features that had null values. The only exception was with the radon file that had one null value and to continue to avoid guess values that one county was dropped.

- Deleted files were surveys about fitness levels, nutrition habits, and smoking rates
- Dropped feature list: Body Mass Index (BMI), fruit/veggie servings, diabetes, blood pressure, certain diseases, primary care rates, and chemical levels found in air or water.

Bigger counties usually had complete data and null values were typically in rows of the smaller counties. It would be interesting using the bigger counties and having more features for the modeling and results sections.

Pesticide data was found near the end of the project and was in a difficult format to transform. Lots of the online data that was stumbled onto was not formatted in a way that would have been easy to incorporate. SEER and census data were in fixed with files, but found early enough and were necessary; scripts (link) were created to transform into csvs. Closer to the end only csv and text files were downloaded.

A good portion of this project was spent googling and surfing for sources, as finding useful data was one of the difficulties in this project. Many files were downloaded and deleted within minutes. This section could have be longer, if all the downloaded files were logged from the start.


## Meet (some of) the Lucky Features

Links will take you to on a trip to Jupyter Notebooks where we can explore one file at a time before the merge.


### SEER: Cancer + Census

Up first and most important for this project is cancer incidents from the SEER database as well as population.
Other features can be dropped, but this is the value our models are predicting.
Both data sets downloaded from SEER website.

Cancer data had 132 columns about the cancer, but no data about the person. 
Lifestyle information would be very, very useful in finding activities that relate to cancer. 
Most of cancer data was not used and lost when grouping rows by year and county for final merge.
Originally project grouped cancer data  by county, year, age, race, and sex.
Another project could keep cancer types to see how different features relate to different cancers.

Population had many rows due to populations in initial frame already split by county, year, age, race, and sex.
Summed rows with same county and year to create file that was used in merge for modeling process.
EDA in next link has both population and cancer grouped by county, year, age, race, and sex.
If project was redone, would be cool to keep population data split by age, race, and sex 
to see how different features affect population segments differently.

Last graph is favorite - sum of different cancer types, sorted high to low in horizontal bar plot.
Graphs with time on X axis: average age, cancer incident counts, cancer rate (grouped by year, county, sex, age, race).

[Cancer + Population](https://github.com/DataDanD/Cancer-Capstone-Portfolio/blob/master/Jupyters/CanRate%20EDA.ipynb)

Feature Engineering: 
Cancer Rate (new column) = Cancer Incidents / Population * 100,000 
- after grouping by county and year, 
summing column values of incidents and population in combining rows.


### TRI (Toxic Inventory Release)

The first data source and was hoping to only link different cancers to different chemicals.
Each year was a file, step one was merging to single csv.
Multi chemical names (structure name) for each chemical, made data spare and cleaning would have taken days.

In the end rows were grouped by year, county, and column with Carcinogen or Not Carcinogen label.
Pounds of chemicals were summed in the grouping.
Maybe should have summed all chemicals by pounds and not worried about carcinogen label.

[TRI](https://github.com/DataDanD/Cancer-Capstone-Portfolio/blob/master/Jupyters/TRI%20EDA.ipynb)

Interesting to look at companies, chemicals, and counties with most pounds released.

Sad that some companies do not have to report chemicals released into our environment to the Environmental Protection Agency (EPA). 
We do not know the percentage of chemicals that are reported. 
Making the accuracy of is this data questionable.


### EPA Air Quality

Air pollution has been measured very well by our government dating back to the 1980s. 
One of the states with higher air pollution is California, 
containing some of the most polluted counties in the United States.

The data had ten measurement IDs and values for every year and county.
In EDA realized measurement IDs were looking at the same topics multiple times, 
but with different units: counts (days vs human days), percentages, and standardized/ non-standardized values.
Only two air pollution problems were being measured - Ozone and PM2.5,
arguably the two most important.

[Air Quality](https://github.com/DataDanD/Cancer-Capstone-Portfolio/blob/master/Jupyters/Air%20EDA.ipynb) 


### Radon

Radon data was scrapped on the web from Columbia University.
Years did not match full time range so an average of the listed years average county radon level was calculated to keep feature.
One county was missing radon information and that county was dropped from experiment.

[Radon Averages](https://github.com/DataDanD/Cancer-Capstone-Portfolio/blob/master/Jupyters/Rad%20EDA.ipynb)

Interesting to see the different averages, and understandable as California is a larger state.
Would have been nice to see a standard deviation of radon as well. 
Highest average was 2.5 and values over 4 pico-curies per liter are considered unhealthy.


### Fracking Wells & Superfund Sites

Both downloaded on Kaggle.com after nice people scrapped/queried, transformed, and uploaded data.
Files included GPS coordinates of the facilities, but were not usable as all other data was at county level.
Almost too much data to explore in files, one having over 500 rows with different chemical metrics.

In the end the merged file only kept count of locations in county for both files. 
This is because start years were unit listed. 
There could have been more superfund sites in past, but data not easily available.

[Fracking Wells](https://github.com/DataDanD/Cancer-Capstone-Portfolio/blob/master/Jupyters/Frack%20EDA.ipynb)

Top fracking county had over 3000 sites and second highest county had 33.
Most California counties didn't have fracking wells.
Some counties had fracking wells on uninhabited islands off their California cost.

[Superfund Sites](https://github.com/DataDanD/Cancer-Capstone-Portfolio/blob/master/Jupyters/Super%20EDA.ipynb)

15 and 13 superfund sites in a county were the highest values in this set.
Most counties having between 1 and 5 of these very polluted sites.


### More Graphs

This notebook was created after merge and contain higher quality graphs that were potential candidates for poster and GitHub.

[graphs](https://github.com/DataDanD/Cancer-Capstone-Portfolio/blob/master/Jupyters/Graphs%20EDA.ipynb)

Contains (in order):
- Histogram with KDE of Incidents in first section
- Scatter plots of features correlated to Cancer Rate
- Boxplots of Fracking, Superfund, and Cancer Incidents
- Heatmaps, one in project and smaller ones investigating values
- Probability plots of data against quantiles of normal distribution



## Heatmap Exploration

![Heatmap of All Features](https://github.com/DataDanD/CancerCapstone/blob/master/Graphs/heatmap.png)

### Top left of Heatmap
Positive correlations between:
Ozone, PM2.5, Population, and Count.

Okay, Ozone, (atmosphere region that absorbs most UV radiation) 
measured as count of days with ozone levels under national standard and 
PM2.5, (atmospheric mater with diameter greater than 2.5 micrometers) 
measured as count of days with PM2.5 levels over national standard; 
both air pollution measurements and understandably relate.

Also, cancer incidents values and population in counties should positively relate.
Meaning that bigger populations should have a larger number of cancer cases. 
'Count' really should have been dropped after using it to create incident rate, and before the merge.
Cancer count does get dropped in all modeling scripts, preventing data leakage. (discussed soon)

Even if cancer incident rates widely differ in counties, population differs more. 
Future analysis, calculate and compare standard deviations of county populations vs incidents 
to better understand the correlation between the two features. 
Incidents range from low 200 to high 900 per 100,000 people.
While, max population for counties is Log Angeles with almost 10 million
and the min population is in Alpine county with less than 2,000 people. 
larger range in population than cancer incidents.
Population is used in final model as data is easy to gather,
and doesn't cause data leakage as rates are new cases per 100,000.
Would be interesting to try modeling total cancer incidents within counties,
rather than rates,
then population would be an extremely valuable feature for predictions.

Larger urban cities are known to have worse air pollution compared to rural areas. 
More people, on average, equals more cars, jobs (pollution from: factories/plants, skyscrapers/work buildings, houses/apartments), and ultimately more waste causing unhealthy pollution measurements to increase. [7] 
We can understand why as population increases in counties, 
we should see a positive correlation and thus 
higher levels of polluted air.
If air pollution is related to cancer then it is safe to say,
'stay away from people' to reduce cancer risk. 


### Middle of Graph

Negative correlations, few positive:
Education, Median Income, Poverty, Unemployment, Uninsured, Alcohal (spelled it wrong ><), Health Status, and Unhealthy Days.

Yup, these all relate to the socioeconomic status of the population.
Range of correlation values in graph from .7 to -.3, not bad.

[SocEco](https://github.com/DataDanD/Cancer-Capstone-Portfolio/blob/master/Graphs/heat3.png)

Realizing now that heatmaps will always use the darkest possible color and lightest color in parameter when filling in graph.
The lightest color will always be used in middle diagonal, when features intersect with itself, scoring 100%
Graph will unfortunately show the most negatively correlated value as the other parameter color, in this case black, even if score is close to 0.
Wonder what would happen if minimum value is positive?

Positive:
Education and Income - increased education -> increased income
Poverty and Uninsured - increased poverty -> increased uninsured

Negative:
Education and Poverty - increased education -> less poverty
Education and Unemployment - increased education -> less unemployed
Education and Healthy Status - increased education -> lower health levels
Education and Uninsured - increased education -> less uninsured (less unemployed)
Poverty and Median Income - increased poverty -> lower incomes
Unemployment and Median Income - increased unemployment -> less income


### Bottom Right Corner

Positive correlations between: 
Elder Medicare, Disabled Medicare, Work Disabled, Drug Use, and Major Depression.

[Bottom Right](https://github.com/DataDanD/Cancer-Capstone-Portfolio/blob/master/Graphs/heat2.png)

When looking for multicollinearity there is no need to analyze target feature column.
The relations with Cancer Rate and features are useful to models in predictive analytics.

Range in graph: -.5 (Drug Use and Year) to .8 (Medicare and Depression)

What does correlation between drug use rate in counties and Medicare rate mean? Does drug use include **prescribed medications**? Will look at other features to see if it makes sense
People have access to more meds as Years increases
Should be positive, but score is -.49
Would expect to see higher collation between meds and Medicare
.37 value, that males sense
Drug use relations to Hepatitis C, Depression, and disabilities
All should be positive and they are: .22, .63, and .37, respectively
After analyzing drug use, it might possibly include medications, can’t be use unless source describes feature.

- Huh, Is drug use going down in California?
	- Drug Use (rate) and Year have slight negative correlation. 
	- As year goes up the rate of drugs used goes down.

- Work Disabled and Medicare Disabled rates correlate. What is happening to people living in these counties?

- Why are counties with higher Medicare rates also counties with more depression?
	- Could this be another machine learning problem referred to as data leakage?

Major Depression and Cancer Rate have a positive correlation.
This value might mean people with depression have an increased chance of cancer.
Is this just a county thing happening by chance? 
Wait, what comes first?
Maybe more likely to have major depression after getting diagnosed with cancer.

This might be data leakage, as counties with higher depression are caused by higher rates of cancer.
We can also see that Medicare rate relates to depression and this could be multicollinearity.
To be safe this data should not be used as knowing the rate of depression in a county will unfairly give the model better accuracy. Using this feature would be similar to using cancer count as a feature, giving the model prediction information that it is trying to guess.
[Depression and Cancer](https://github.com/DataDanD/Cancer-Capstone-Portfolio/blob/master/Graphs/CanDep.png)
