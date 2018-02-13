# Heatmaps (Plasma Soups)

![Heatmap of All Features](https://github.com/DataDanD/CancerCapstone/blob/master/Graphs/heatmap.png)

## Top left
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


## Center

Negative correlations, few positive:
Education, Median Income, Poverty, Unemployment, Uninsured, Alcohal (spelled it wrong ><), Health Status, and Unhealthy Days.

Yup, these all relate to the socioeconomic status of the population.
Range of correlation values in graph from .7 to -.3, not bad.

[SocEco](https://github.com/DataDanD/Cancer-Capstone-Portfolio/blob/master/Graphs/heat3.png)

Realizing now that heatmaps will always use the darkest possible color and lightest color in parameter when filling in graph.
The lightest color will always be used in middle diagonal, when features intersect with itself, scoring 100%
Graph will unfortunately show the most negatively correlated value as the other parameter color, in this case black, even if score is close to 0.
Wonder what would happen if minimum value is positive?

#### Positive:
Education and Income - increased education -> increased income
Poverty and Uninsured - increased poverty -> increased uninsured

#### Negative:
Education and Poverty - increased education -> less poverty
Education and Unemployment - increased education -> less unemployed
Education and Healthy Status - increased education -> lower health levels
Education and Uninsured - increased education -> less uninsured (less unemployed)
Poverty and Median Income - increased poverty -> lower incomes
Unemployment and Median Income - increased unemployment -> less income


## Bottom Right

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
