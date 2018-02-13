# Discarded Data
(Sad section for me)

## County
## ID Problems
A couple times after finding relevant data, it didn't have county level information or was too sparse (missing many values) to use. Missing pieces in these tables are called null values, and too many null values makes the data sparse. It is possible to fill null values, the easiest and most well known is using mean/median values within that column. However, a few [other techniques](https://www.omicsonline.org/open-access/a-comparison-of-six-methods-for-missing-data-imputation-2155-6180-1000224.pdf) have been reported to outperform mean/median are more complicated. [reference article linked above]

## Spares Data
Bigger counties usually had complete data and null values were typically in rows of the smaller counties. It would be interesting using the bigger counties and having more features for the modeling and results sections.

## Null Values
This project completely avoided filling missing values by deleting data sets and dropping features that had null values. The only exception was with the radon file that had one null value and to continue to avoid guess values that one county was dropped.

- Deleted files were surveys about fitness levels, nutrition habits, and smoking rates
- Dropped feature list: Body Mass Index (BMI), fruit/veggie servings, diabetes, blood pressure, certain diseases, primary care rates, and chemical levels found in air or water.

## Other Fails
Pesticide data was found near the end of the project and was in a difficult format to transform. Lots of the online data that was stumbled onto was not formatted in a way that would have been easy to incorporate. SEER and census data were in fixed with files, but found early enough and were necessary; scripts (link) were created to transform into csvs. Closer to the end only csv and text files were downloaded.

## Discussion
