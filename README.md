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

Originally the cancer and population data was also grouped by County, Year, Race, Sex, and Age. This was to find out if any features affected segments of the population differently. Upon analysis, some of the cancer incident rates became extremely large. Two rows in particular had 100,000 cancer incidents per 100,000 people due to 1 person being in that row along with 1 new case of cancer for that year. Rather than setting a population cut off and removing rows under that value to reduce skewed rates, data was only grouped by year and county. This allowed us to hold on to all cancer incidents and total population for each county.

![Data Table](https://github.com/DataDanD/Cancer-Capstone-Portfolio/blob/master/Graphs/DataTable.png)


The table above contain information on all datasets in the final data frame that will be used for regression modeling. All data had to at least be grouped by county ('C') to help provide unique information in features, sadly any cool data without county level detail was deleted. Data labeled grouped by year ('Y') is only when all 10 years of correct rage were available. Some data is the average of a few years and in the above table is only considered grouped by county. Data is grouped by County Fips because, the SEER cancer data needed for project is report with county as the lowest denominator, no zipcodes or town names were provided. Integers listed for columns and rows of each data source are recorded after filtering for California and for years (2001-2012) used in project. Unfortunately some of the main data used stopped in 2012, while other data is updated regularly. The number of columns the dataset provided for the final data frame is recorded in the feature column of the table.

Most data sources were thanks to government agencies and their open source files were typically located on data.gov. [1] Theses government files contain data collected from surveys, reported by companies, or are measured from an agency. A few data sources were found on [Kaggle.com](https://www.kaggle.com/) in their public dataset sharing section (as of today they have 10,833 files that can be downloaded). 

Accessing the SEER cancer data requires a [signed wavier](https://seer.cancer.gov/data/access.html), therefore I am not allowed to share the file. However, Cancer.csv is the final file and can be downloaded from the home page on this repository. It has the cancer incident vales the models are trying to predict as well as all the final features used to make these predictions. Final data frame is 627 rows with 28 columns, 27 features for the X value in scripts and the y value that is predicted is labeled 'Cancer Rate'. There are 58 counties in California and 11 years of data, there should be 638 rows, but one county was missing Radon data and was dropped from this experiment.

For more information and a link to each file used in Cancer.csv, check out [Data.md](https://github.com/DataDanD/Cancer-Capstone-Portfolio/blob/master/Data.md) on the home page.



### Discarded Data

(Sad section for me)

A couple times after finding relevant data, it didn't have county level information or was too sparse (missing many values) to use. Missing pieces in these tables are called null values, and too many null values makes the data sparse. It is possible to fill null values, the easiest and most well known is using mean/median values within that column. However, a few [other techniques](https://www.omicsonline.org/open-access/a-comparison-of-six-methods-for-missing-data-imputation-2155-6180-1000224.pdf) have been reported to outperform mean/median are more complicated. [reference article linked above]

This project completely avoided filling missing values by deleting data sets and dropping features that had null values. The only exception was with the radon file that had one null value and to continue to avoid guess values that one county was dropped.

- Deleted files were surveys about fitness levels, nutrition habits, and smoking rates
- Dropped feature list: Body Mass Index (BMI), fruit/veggie servings, diabetes, blood pressure, certain diseases, primary care rates, and chemical levels found in air or water.

Bigger counties usually had complete data and null values were typically in rows of the smaller counties. It would be interesting using the bigger counties and having more features for the modeling and results sections.

Pesticide data was found near the end of the project and was in a difficult format to transform. Lots of the online data that was stumbled onto was not formatted in a way that would have been easy to incorporate. SEER and census data were in fixed with files, but found early enough and were necessary; scripts (link) were created to transform into csvs. Closer to the end only csv and text files were downloaded.

A good portion of this project was spent googling and surfing for sources, as finding useful data was one of the difficulties in this project. Many files were downloaded and deleted within minutes. This section could have be longer, if all the downloaded files were logged from the start.



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

### Meet (some of) the Lucky Features

Links will take you to on a trip to Jupyter Notebooks where we can explore the pre-merged files.


#### SEER: Cancer + Census

Up first and most important for this project is cancer incidents from the SEER database as well as population.
Other features can be dropped, but this is the value our models are predicting.
Both data sets downloaded from SEER website.

Cancer data had 132 columns about the cancer, but no data about the person. 
Lifestyle information would be very, very useful in finding activites that relate to cancer. 
Most of cancer data was not used and lost when grouping rows by year and county for final merge.
Origanally project grouped cancer data  by county, year, age, race, and sex.
Another project could keep cancer types to see how different features relate to different cancers.

Population had many rows due to populations in inital frame already split by county, year, age, race, and sex.
Summed rows with same county and year to create file that was used in merge for modeling process.
EDA in next link has both population and cancer grouped by county, year, age, race, and sex.
If project was redone, would be cool to keep population data split by age, race, and sex 
to see how different features affect population segments differently.

Last graph is favorite - sum of different cancer types, sorted high to low in horizontal bar plot.
Graphs with time on X axis: average age, cancer incident counts, cancer rate (grouped by year, county, sex, age, race).

[Cancer + Population](https://github.com/DataDanD/Cancer-Capstone-Portfolio/blob/master/Jupyters/CanRate%20EDA.ipynb)

Feature Engineering: 
Cancer Rate (new column) = Cancer Incidents / Population * 100,000 
- after groupping by county and year, 
summing column values of incidents and population in combining rows.


#### TRI (Toxic Inventory Release)

The first data source and was hoping to only link different cancers to different chemicals.
Each year was a file, step one was merging to single csv.
Multi chemical names (structure name) for each chemical, made data spare and cleaning would have taken days.

In the end rows were grouped by year, county, and column with Carcinogen or Not Carcinogen label.
Pounds of chemicals were summed in the groupping.
Maybe should have summed all chemicals by pounds and not worried about carcinogen label.

[TRI](https://github.com/DataDanD/Cancer-Capstone-Portfolio/blob/master/Jupyters/TRI%20EDA.ipynb)

Interesting to look at companies, chemicals, and counties with most pounds released.

Sad that some compannies do not have to report chemicals released into our environment to the Enviromental Protection Agency (EPA). 
We do not know the percentage of chemicals that are reported. 
Making the accuracy of is this data questionable.


#### EPA Air Quality

Air pollution has been measured very well by our government dating back to the 1980s. 
One of the states with higher air pollution is California, 
containing some of the most polluted counties in the United States.

The data had ten measurment IDs and values for every year and county.
In EDA realized measurment IDs were looking at the same topics multiple times, 
but with different units: counts (days vs human days), percentages, and standardized/ non-standardized values.
Only two air pollution problems were being measured - Ozone and PM2.5,
argualby the two most important.

[Air Quality](https://github.com/DataDanD/Cancer-Capstone-Portfolio/blob/master/Jupyters/Air%20EDA.ipynb) 


#### Radon

Radon data was scrapped on the web from Columbia University.
Years did not match full time range so an average of the listed years average county radon level was calculated to keep feature.
One county was missing radon information and that county was dropped from expirement.

[Radon Averages](https://github.com/DataDanD/Cancer-Capstone-Portfolio/blob/master/Jupyters/Rad%20EDA.ipynb)

Interesting to see the different averages, and understandable as California is a larger state.
Would have been nice to see a standard deveation of radon as well. 
Highest average was 2.5 and values over 4 picocuries per litre are considered unhealthy.


#### Fracking Wells & Supefund Sites

Both downloaded on Kaggle.com after nice people scrapped/queried, transformed, and uploaded data.
Files included GPS coordinates of the facilities, but were not usable as all other data was at county level.
Almost too much data to explore in files, one having over 500 rows with different chemical metrics.

In the end the merged file only kept count of locations in county for both files. 
This is because start years were unot listed. 
There could have been more superfund sites in past, but data not easily avalible.

[Fracking Wells](https://github.com/DataDanD/Cancer-Capstone-Portfolio/blob/master/Jupyters/Frack%20EDA.ipynb)

Top fracking county had over 3000 sites and second highest county had 33.
Most California counties didn't have fracking wells.
Some counties had fracking wells on uninhabited islands off their California cost.

[Superfund Sites](https://github.com/DataDanD/Cancer-Capstone-Portfolio/blob/master/Jupyters/Super%20EDA.ipynb)

15 and 13 superfund sites in a county were the highest values in this set.
Most counties having between 1 and 5 of these very polluted sites.


#### More graphs

This notebook was created after merge and contain higher qualiy graphs that were potential candidates for poster and GitHub.

[graphs](https://github.com/DataDanD/Cancer-Capstone-Portfolio/blob/master/Jupyters/Graphs%20EDA.ipynb)

Contains (in order):
- Histogram with KDE of Incidents in first section
- Scatter plots of features correlated to Cancer Rate
- Boxplots of Fracking, Superfund, and Cancer Incidents
- Heatmaps, one in project and smaller ones investigating values
- Probability plots of data against quantiles of normal distribution


### Merged Data EDA 

Now we will explore all the features that have successfully passed the merge to the final dataframe.

First up is an image of a heatplot (also called "plasma soup" by an extremely select few) this will show us column relationships, in the form of correlations, in all of the data. Lighter and darker (positive and negative correlations, respectively) boxes on the graph are usually not a good thing. Exceptions currently include: diagonal in the middle where features intersect with themselves (100% correlation!) and the rows/columns with 'Count' and 'Cancer Rate'. They should honestly be removed from this graph as they are not features used in prediction. (Will fix in future, maybe; I mean it is cool to see what they relate to as well) 'Count' was used to make 'Cancer Rate' by dividing the cancer count by population in same county and year, then multiplied by 100,000.

Note: only have to look at half of plasma soup graph below to understand all the correlations. Features will intersect with all other features twice. Pick a side of light colored diagonal to aviod seeing relations twice.

![Heatmap of All Features](https://github.com/DataDanD/CancerCapstone/blob/master/Graphs/heatmap.png)


Interesting... Looks like I have more work to do. This might take awhile.


#### Correlation Overview

Correlation happens when a variable can be very accuratly predictied 
by useing other data feature or features
in a basic mutiple linear regression model.
Basicly defined as a mutual dependence,or association 
between two of more things 
in a predictable statistical manner.
This linear relationship might be causal, but does not have to be to form a correlation.
Scale of data is not considered when determining correlations.
The three types of correlations are positive, negative, or no correlation.
Correltations are measured with a correlation coeffcient 
that varies between -1 (a strong negative relations) and +1 (a stong positive correlation). 
The relationship gets weaker as the value goes towards 0.

Unfortunitly we have lots of correlating features in heatmap above
and this section is the longest.
A data scientist should believe that
Garbage data into the model equals garbage predictions out.

This "garbage" data is why analyzing data has one of the largest proportions of total time 
in typical machine learning projects.
Cleaning and possibly modeling
data are the other processes that should take a long time for good results.
Finding government data took a long time as well in this atypical machine learning adventure. 
Going to assuming companies already have databases with information 
available for modeling activites.




##### Positve Correlation 

Represented as light color in graph above.

A county with high value in feature_1, likly has high value in feature_2, or low and low values, when feature_1 and feature_2 have a positive correlation. When fearues increase or decrease together, in same direction.

If all values for the two features are graphed on a scatter plot and a line is drawn though points, it would start in lower left corner and reach to upper right.


###### Positve Example 

Elderly Medicare & Cancer Rate features have a positive correlation.

This makes sense, as humans age we have a higher chance of getting cancer.
Advancing age is the most important cancer risk factor states the National Cancer Institue. [8]

Older populations (higher Medicare rate) are more prone to cancer
and having an older population within a county will have more cancer indcidents.

Less young people get cancer with the average age of a cancer diagnosis is over 60; 
seen in the graph below, created with the California cancer data.

[cancer age](https://github.com/DataDanD/Cancer-Capstone-Portfolio/blob/master/Graphs/SexCanAge.png)

Accroding to the data from this project, men have a higher average age for getting cancer; 
this was suprising as females are known to live a few years longer and than men. 
Maybe this is due to breast cancer vs prostate cancer or men not going to the doctor as often?

This correlation should help with model predictions later on.
The project started without socioeconomic data and wasn't preforming very well.


##### Negative Correlation 

Represented as darker colors on the heatmap.

Featue values go in opposite directions of eachother if they have a negative correlation. Therefore, when feature_1 increases then feature_2 decreases, or as feature_1 is considered to have a lower value then feature_2 should have a higher value compared to county averages.

If graphed the same way as in positive correlation section, regression line would start in top left and go to bottom right.


###### Negative Example

In the heatmap Median Income & Disabled Medicare have a negative correlation. 
As median income goes up disabled medicare rates go down. 

This could suggest:
1) Age?
Counties with a younger population could have higher median incomes and lower disabled Medicare. 
- Higher income: higher working rate as young people need to build up currency for life expenses.
- Less disabled Medicare: younger people are supposed to be healthier and would qualify for Medicaid, not Medicare. Medicare is for citizens over 65 years of age, some few rare age exceptions.

Counties with older populations have lower median incomes and higher disabled Medicare rates.
- Lower Income: more retired people not working, relying on saved funds.
- Higher disabled Medicare: As people age the change of injury, infection and other disabeling conditions become more likely.

2) Cost?
People with disabled Medicare might unfortunitly not be able to afford to live in counties with higher incomes. 
Rates of disabled medicare are in counties of lower income.

3) Work Ethic? 
(Based on trips to Arkansas)
Counties with people making less might have a higher rate to abuse the system. 

The negative relation here can mean many things and we can only guess or hypotheis the reasons. 
We cannot say for fact what factors are causeing these features to relatie without a research expirement.
Proper references articles citing research on these relations would also work.

Some relations in this projects heatmap might be abnormal.
Only seen in California or 
based on the select data used.
That is another thing to keep in mind. 


###### Correlation Test (on Graphs From Lucky Feature Section)

Which graph shows a positive and which shows a negative correlation to year?

Cancer Incidents per Year
[Cancer Incidents](https://github.com/DataDanD/Cancer-Capstone-Portfolio/blob/master/Graphs/SexCanCountsYr.png)

2nd graph in [SEER EDA](https://github.com/DataDanD/Cancer-Capstone-Portfolio/blob/master/Jupyters/CanRate%20EDA.ipynb) notebook

Chemicals Released per Year
[Chemicals](https://github.com/DataDanD/Cancer-Capstone-Portfolio/blob/master/Graphs/ChemByYr.png)

fourth graph in [TRI](https://github.com/DataDanD/Cancer-Capstone-Portfolio/blob/master/Jupyters/TRI%20EDA.ipynb) notebook

Answers:

Cancer Incidents: 
Positive correlation to time - 
increasing number of cancer cases as year increases. 
Positive note: population is also increasing in the state of California and cancer incidents is dropping 
[SEER EDA](https://github.com/DataDanD/Cancer-Capstone-Portfolio/blob/master/Jupyters/CanRate%20EDA.ipynb) third graph is cancer rates when grouped by county, year, age, race, and sex.

Chemicals Released: 
Negative correlation to time - 
less chemicals being released as year increses. 
Negative note: possibility that less companies are reporting releases of chemicals 


#### Heatmap Analysis

So, what correlates?


##### Top left of Hatmap
Positive correlations between:
Ozone, 
PM2.5, 
Population, and
Count.

Okay, Ozone, (atmosphere region that absorbs most UV radiation) 
measured as count of days with ozone levels under national standard and 
PM2.5, (atmospheric mater with diameter greater than 2.5 micrometers) 
measured as count of days with PM2.5 levels over national standard; 
both air pollution measurements and understandably relate.

Also, cancer incidents vlues and population in counties should positvily relate.
Meaning that bigger populations should have a larger number of cancer cases. 
'Count' really should have been droped after using it to create incident rate, and before the merge.
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
More pople, on average, equals more cars, jobs (pollution from: factories/plants, skyscapers/work buildings, houses/apartments), and utimatly more waste causing unhealthy pollution measuremes to increase. [7] 
We can understand why as population increases in counties, 
we should see a positive correlation and thus 
higher levels of polluted air.
If air pollution is related to cancer then it is safe to say,
'stay away from people' to reduce cancer risk. 



###### Multicolinearity (fix)

In statistics, multicollinearity is when features in data used for regression models, correlate.
Having already exploted correlations in too much detail we should understand what a regression models is used for.
Regression models are a commonly used type of machine learning algorithm used for predicting numerical targets.
Having correlatd features, makes the effects of features
on the target variable hard to distinhuish from each other.

Making model train longer.


###### Feature Selection (complete)

One method of losing correlated features is to simply drop one of the features.

Example with air pollution:

Feature 1 - Ozone, larger correlation to value being predicted (Cancer Rate), 
and research has related lower ozone values to higher skin cancer rates.

Feature 2 - PM2.5, larger correlation with some featues like (Population), 
and research has linked higher PM2.5 values to increased rigk of lung cancer.

Would keep Ozone as it relates more to incident and less to other features in data being modeled, 
if only selecting one.
Could try modeling methoods with both features seperatly to analyze results; 
more code, maybe better result, and more analysis potention.
Also, merging both columns into a single value, might yeild interesting results.
Combining columns together is called feature engineering and is discussed in next section .


##### Middle of Graph
Negative correlations, few positive:
Education, 
Median Income, 
Poverty, 
Unemployment, 
Uninsured, 
Alcohal (spelled wrong), 
Health Status, 
Unhealthy Days.

Yup, these all relate to the socioeconimic status of the popultion.

Quick here to cover most of the feature relations.

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


###### Feture Engineering

Feture engineering keeps corrilated features by creating a new column that 
somehow combines values of different columns
These definetly related social determinent columns would be appropriate to combine together.
Especially if the columns are measured with similar unites.
Using feature selection to drop some correlated features would be a quicker process, in reducing multicolinearity.

Most of these correlation were found after poster and modeling was completed, unfortunitly engineering wont happen unless I redo parts of this project in the future.

Feture Engineering Example: 
Socioeconomic Status (new column) = (Normalize all columns) Povery + Education + Unemployed + Uninsured / 4

Normalize all features so they weigh similar amounts (porpotions) before summing together. 
Adding a feature with higher values to columns with lower values will make the column with high values more important, 
skewing the new column potentially make lower valued features irrelavent. 
Normalizing will also importantly keep deviations of the features being added together.
However, these features already use the same unit of rates in population and wont need normalizing.
Divide by 4 (not nessacary for modeling) in above equation to make new unit rate similar to other feature. 
If feature is used to create new column in formula it will have to be dropped and can't be analysed later in project.
Therefore, combine as few featues as possible when reducing corrilations keeping more uniqe data and features 
for better modeling more features to analyze in result section.
If engineered features correlate they will need to be combined or dropped and process repeated,
untill no multicolinearity exists between features used for the machine learning models.

(resource link)


##### Bottom Right Corner

Positive correlations between: 
Elder Medicare, 
Disabled Medicare, 
Work Disabled, 
Drug Use, 
Major Depression.

Questions about relations:
- Why are counties with higher Medicare rates also counties with more depression?
- What does drug use even mean if counties with more medicare are counties with highre drug use?
- Work Disabled and Medicare Disabled rates correlate. What is going on in these counties?



##### Other Interesting Relations

Is drug use going down in California?
Drug Use (rate) and Year have a negative correlation. 
As year goes up the rate of drugs used goes down.


Major Depression and Cancer Rate have a positive correlation. What?
Could this mean that people with depression have an increased chance of cancer.
Is this just a county thing happening by chance? 
Wait, what comes first?
Maybe more likely to have major depression after getting diagnosed with cancer.

This might be data leakage, as counties with higher depression are caused by higher rates of cancer.
We can also see that Medicare rate relates to depression and this could be multicolinearity.
To be safe this data should not be used as knowing the rate of depression in a county will unfairly give the model better accuracy. Using this feature would be similar to using cancer count as a feature, giving the model prediction information that it is trying to guess.
[Depression and Cancer](https://github.com/DataDanD/Cancer-Capstone-Portfolio/blob/master/Graphs/CanDep.png)



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

#### Regression Model Packages 

Next, up 
[random forest](http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html), 
[gradient boosting](http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html), 
[ada(adaptive)boost](http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostRegressor.html#sklearn.ensemble.AdaBoostRegressor), 
and [cat(categorical)boost](https://tech.yandex.com/catboost/)
with default parameters. 
Links above are to exact models used, first three from python machine learning package SK-Learn. 
Catboost is an algorithm released by Russian company Yandex which is trying to break into the world AI scene and downloaded from web. 
If you are interested in learning about a new state of the art model, read about CatBoost!

After deciding on best model, of the four mentioned in section, for this problem, 
we can compare to another web downloaded model [XG(Extreme Gradient)Boost](https://github.com/dmlc/xgboost).
XGBoost is the current go to and considered king of the boosting algorithm family by data scientist.

[XGBoost article](https://machinelearningmastery.com/develop-first-xgboost-model-python-scikit-learn/)


##### Model Education (complete)

Regression models are a commonly used type of machine learning algorithms and used for predicting numerical or continuous values.
The other popular supervised learning technique is called classification and this class of algorithms is used to predict the observations into differnt classes, as the name suggest. 
Only use classification models when predicting categorical variables. 
However, we are predicting rates, a numerical/continuous variable and 
therefore will use regression models to make these guesses of cancer incidents.
Most statistical algorithms can be used for both regression and classification problems. 
Classification trees are used for splitting data into groups, 
while regression trees are used in cases of predicting numerical variables. 
Both of these tree models are also called dicision trees.
The main differences between these two tree types
is when to use each, but also how they calculate formation of branches.
Basically, tree model will try all available features, along with all available data, 
to calculate the feature to split the data on that will yeild the best results.
[Tree splits](http://www.simafore.com/blog/bid/62482/2-main-differences-between-classification-and-regression-trees), explained in more detail.

The problem with a single dicision tree is that it will keep splitting 
until all the training data is correct, this causes overfitting and
poor performance on test data.
Using algorithms that contain multiple low correlating stumps is can lead to powerful model, 
especailly when the stumps are created in sequeltial order, learning for mistakes in training data.

Decision trees are important for both Random forest and boosting models.
How dicision trees decide on feature to split on

Radom forst has a buch of dicision tree with randomly selected featres to split on, 
and randomly slected data to train each unique tree. 
All of the trees in the forest are used in the prediction process.
Taking the mode of all tree predictions for a classification model or 
the mean value from all the tree predictions in a regresion model.

Random forest differs 

Boosting

http://dataaspirant.com/2017/05/22/random-forest-algorithm-machine-learing/
http://blog.kaggle.com/2017/01/23/a-kaggle-master-explains-gradient-boosting/



[class vs regress](http://www.simafore.com/blog/bid/62482/2-main-differences-between-classification-and-regression-trees)

###### Model Scores

Scores in this section are used to compare forcasting errors of different models on the same dataset.
All model scores found in project were calculated using test data.
Test data are random rows in the data frame that are withheld from the model training process.
These random rows are used after model training to score how well the model predicts unseen data.
Training the model with both test and training data will make the models scores higher on test data.
Potentially making the model overfit and thus would result in poor predictions on new data.
It is important to use test data to compare the accuaracy scores of differnt models, 
in order to find the best algorithm for the problem.

Scores for regression models are: Mean Absolute Error(MAE), R2, RMSE, or without the R in Mean Squared Error(MSE).

- RMSE is commonly used to score how well regression models are predicting actual values.
Works by squaring the the difference of the prediction minus actual values to make all errors positive numbers.
This formula is used so that predictions below and above actual values will not cancel each other out when summed.
It also takes the root of the error so outliers with higher values are not penalized by the suarring process.
RMSE is known as the sample standard diciation for the diffenences between actual values and the predicted values.
The formula used to calculate RMSE means the output value is the average of all residuals
; the average distance measured between all of the model guesses and real numbers in the test data.
It is stated to be an accuracy measurement, that contains the magnitudes of errors in prediction.

- Mean Absolute Error (MAE) is another data scientist recommended scoring methood.
The main advantage with this score is interpretability, as MAE is easier to understand,
Compared to RMSE, the square root of the average of squared errors.
MAE calculates average absolute difference between the prediction and the actual values.
Every error in MAE is directionaly porportionate to the value of error, which is not the case for RMSE.

- R2, called the coefficient of determination, is similar to correlation values, but its range is between 0 and 1.
This score measures the goodness-of-fit between the model and the data, 
Measures how close the data is to the fitted regression line.
R2 is defined as the percentage of the response variable variation that is explained by a linear moded, equals explained variation divided by total variation. 
R2 of 0 indicates model explains none of the variability in data around the mean.
While, 1 (100%) indicates that the model explains all the variability of respone data around the mean.
Limitation of the R2 scored is that it cannont determine if the estimates are biased and does not indicate wheather regreesion model is adequate for data.
Can have a low R-squared value for a good model, or a high R-squared value for a model that does not fit the data. 
Therefore, R2 was taken out of modeling scripts used in this project
and other regression scores that give an absolut error measure were used.

- Mean squared error (MSE) is similar to RMSE, but does not sqaure root the errors. 
Therefore, this score will be influence greater by high errors values that are squared. 
MSE is a useful score for models that cannot afford to have high error values, 
a few poor outliers will strongly effect this score.

Scores for classification incluse: accuracy, recall, precision, f1, and roc accuracy.
When predicting categorical data we end up with a confusion matrix that contain, true positive, true negative, false positive and false negative values. These values are then used in different formulas to calculate the the scores listed above.

Later, after finding the model with the best score we can see what features matter the most in making accurate predictions, this will calculate the feature importance in the data.

### (UNDER CONSTRUCTION) Feature Importance and Default Scores

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
   Add scripts in pipeline

2) Update graphs, add others (EDA)
   Clean folders

3) Add links (Use refference links on page)(add all links in paper to refferences)

4) Improve EDA in permerged Jupyter Notebooks

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
