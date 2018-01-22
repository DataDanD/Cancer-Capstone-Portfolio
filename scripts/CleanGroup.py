import pandas as pd
import numpy as np

# Functions that will clean all of the dataframes used in this project
def SEER(df):
    '''
    INPUT: Pandas dataframe collected from https://seer.cancer.gov/data/ (CDC).
           run SEER.py to turn text into csv before this script
    OUTPUT: Pandas dataframe of cancer grouped by county & year in California
    '''
    # California is 06 and the last 3 digits are for counties
    df =df[df'State-county recode'] > 5000]
    df =df[df'State-county recode'] < 7000]
    # Limit the years to avoid a sparse dataframe
    df = df[df['Year of diagnosis'] > 1999]
    df = df[df['Year of diagnosis'] < 2011]
    group=['Year of diagnosis', 'State-county recode']
    df['Count'] = 0
    df = df.groupby(by=group)['Count'].count().reset_index()
    df.columns = ['Year', 'C Fips', 'Count']
    # Don't need state fips code anymore, just need county for the merge
    df['C Fips'] = (df['C Fips']-6000)
    return df


def POP(df):
    '''
    INPUT: Pandas dataframe from https://seer.cancer.gov/popdata/download.html.
           run Pop.py to turn text into csv before this script
    OUTPUT: Pandas dataframe of Population grouped by county & year.
            Originally grouped by sex, race, and age bins, as well.
            We will do a left join so no need to filter state
    '''
    df = df.groupby(['Year','C Fips'])['Population'].sum().reset_index()
    # Don't have to limit year, but it will run faster / save space
    df = df[df['Year'] > 1999]
    return df


def Air(df):
    '''
    INPUT: Pandas dataframe with Air quality from the EPA
           https://aqs.epa.gov/aqsweb/airdata/download_files.html
    OUTPUT: Pandas dataframe with appropriate measures for CA
    '''
    # Don't have to limit year, but it will run faster / save space
    df = df[df['ReportYear'] > 2000]
    # Don't need state fips code anymore
    df['CountyFips'] = (df['CountyFips']-6000)
    x = ['MeasureId', 'MeasureType', 'CountyFips',
         'ReportYear', 'Unit', 'UnitName', 'Value']
    newdf = df[x]
    # Pivot measure ID to have unique columns for each measure
    Air =  pd.pivot_table(newdf,index=['CountyFips','ReportYear'], \
           columns='MeasureId',values ='Value').reset_index()
    # 293 = ozone count in person days, 295 = PM2.5 in person years
    # The 8 other questions were the same just measured differently
    x = ['CountyFips', 'ReportYear', 293, 295]
    Air = Air[x]
    Air.columns = ['C Fips', 'Year', 'Ozone', 'PM2.5']
    return Air


def Frack(df):
    '''
    INPUT: Pandas dataframe from kaggle. Could use chemicals in wells
           https://www.kaggle.com/frackinganalysis/fracking-well-chemical-disclosure-datasets Scraped from  https://frackingdata.org/
    OUTPUT: Pandas dataframe using count of wells by county in CA
    '''
    # Counties are not named uniformly, not changing offshore names
    df.loc[df['CountyName'] == 'Kern - 30', 'CountyName'] = 'Kern'
    df.loc[df['CountyName'] == 'Kern County', 'CountyName'] = 'Kern'
    df.loc[df['CountyName'] == 'Los Angeles Offshore', 'CountyName'] = 'Los Angeles'
    df.loc[df['CountyName'] == 'LA SALLE', 'CountyName'] = 'La Salle'
    # Create column to place sum of fracking wells in counties
    df['has_fracking'] = 0
    df = df[['CountyName', 'has_fracking']]
    df = df.groupby(['CountyName'])['has_fracking'].count().reset_index()
    df.columns = ['Name', 'has_fracking']
    # All data is being merged on FIPS code note name of county
    # This is becuase counties can have different naming conventions
    df = df.merge(Fips,on='Name')
    df = df.drop(['Name'],1)
    return df


def Super(df):
    '''
    INPUT: Pandas Dataframe with list of Superfund sites scraped from
           https://www.census.gov/research/data/planning_database/2015/ from Kaggle https://www.kaggle.com/srrobert50/federal-superfunds/data
    OUTPUT: Pandas dataframe of CA Superfund Sited grouped by county
    '''
    https://www.kaggle.com/srrobert50/federal-superfunds/data
    # Remove the word county from each county name and merge with FIPS
    df['Name'] = df['County_name'].map(lambda x: str(x)[:-7])
    df = df.merge(Fips,on='Name')
    df = df.drop(['Name','County_name','Unnamed: 0'],1)
    return df

def Radon(df):
    '''
    INPUT: Pandas dataframe with 5 years of radon levels in the US
           http://www.stat.columbia.edu/~gelman/arm/examples/radon_complete
    OUTPUT: Pandas dataframe with mean radon per CA county
    '''
    # Limit dataframe to needed metrics
    df = df[df['state'] == 'CA']
    df = df.drop(['idnum', 'state', 'state2', 'stfips', 'zip', 'region', 'typebldg', 'floor', 'room', 'basement', 'windoor', 'rep', 'stratum', 'wave', 'starttm', 'stoptm', 'startdt', 'stopdt', 'dupflag', 'zipflag', 'county'], 1)
    # Group by Fips and get one mean radon score for each county
    df = df.groupby('cntyfips')['activity'].mean().reset_index()
    df.columns = ['C Fips', 'Radon']
    return df

def TRI(df):
    '''
    INPUT: Pandas dataframe with toxic release inventory for US
           http://www.stat.columbia.edu/~gelman/arm/examples/radon_complete
    OUTPUT: Pandas dataframe with Carcinogenic and non-Carcinogeni chemicals
            summed by counties and year in Ca
    '''
    # One chemical in grams is dioxins and wont add much to our weight total
    df = df[df['UNIT_OF_MEASURE'] != 'Grams']
    # Dropping lots of cool data that would make the dataframe too sparse
    group = ['YEAR','COUNTY','CARCINOGEN','ON-SITE_RELEASE_TOTAL']
    df = df[group]
    # Sum up ON-SITE_RELEASE_TOTAL for county, year, and Carcinogen
    # OFF-SITE_RELEASE_TOTAL was too small to use
    df = df.groupby(['YEAR','COUNTY','CARCINOGEN'])['ON-SITE_RELEASE_TOTAL'].sum().reset_index()
    # Turn Carcinogen and non-Carcinogen into their own columns
    df = pd.pivot_table(df,index=['COUNTY','YEAR'],columns='CARCINOGEN',values ='ON-SITE_RELEASE_TOTAL').reset_index()
    # Rename columsn for easier merge
    df.columns = ['Name','Year','Not Carcinogen', 'Carcinogen']
    # County names were in caps, need them standard to get FIPS
    df['Name'] = df['Name'].str.title()
    df = df.merge(Fips,on='Name')
    df.drop('Name',1,inplace=True)
    return df

def EDU(df):
    '''
    INPUT: Pandas dataframe with education levels in Ca by county
           https://catalog.data.gov/dataset/county-level-data-sets
    OUTPUT: Pandas dataframe with mean education level ready to merge
    '''
    df['C Fips'] = df['fips'] - 6000
    # Drop the % sign to make column a float
    df['Education'] = df['rate_2000'].map(lambda x: str(x)[:-1])
    df['Education'].astype('float')
    group = ['Education','C Fips']
    df = df[group]
    return df

def Poverty(df):
    '''
    INPUT: Pandas dataframe with Poverty levels in Ca by county
           https://catalog.data.gov/dataset/county-level-data-sets
    OUTPUT: Pandas dataframe with mean Poverty level ready to merge
    '''
    df['C Fips'] = df['fips2'] - 6000
    group = ['total_est_pct3','C Fips']
    df = df[group]
    # Change needed column to something more understandable
    df['Poverty'] = df['total_est_pct3']
    df.drop('total_est_pct3',1,inplace=True)
    return df

def Employed(df):
    '''
    INPUT: Pandas dataframe with 5 years Employment levels in Ca by county
           https://catalog.data.gov/dataset/county-level-data-sets
    OUTPUT: Pandas dataframe with mean Employment level ready to merge
    '''
     x = ['fips1', 'ID2008',  'ID2009', 'ID2010', 'ID2011', 'ID20121', 'Textbox11']
     df['C Fips'] = df['fips1'] - 6000
     # Average the 5 year of Unemployment
     df['Unemployed'] = (df['ID2008'] + df['ID2009'] + df['ID2010'] + df['ID2011'] + df['ID20121']) / 5
     # Grab Median Income as well and make it more readable
     df['Median Income'] = df['Textbox11']
     group = ['C Fips','Unemployed','Median Income']
     df = df[group]
     return df

def VunPop(df):
    '''
    INPUT: Pandas dataframe with Vunerable Population information for US
           https://catalog.data.gov/dataset/community-health-status-indicators-chsi-to-combat-obesity-heart-disease-and-cancer
    OUTPUT: Pandas dataframe with Work Disabled Major Depression and Recent Drug Use for CA counties
    '''
    df = df[df['State_FIPS_Code'] == 6]
    df['C Fips'] = df['County_FIPS_Code']
    # Could use No_HS_Diploma and Unemployed, but have that from other reports
    # x = ['C Fips','No_HS_Diploma','Unemployed',
    # 'Sev_Work_Disabled','Major_Depression','Recent_Drug_Use']
    x = ['C Fips','Sev_Work_Disabled','Major_Depression','Recent_Drug_Use']
    df = df[x]
    return df

def HealthStat(df):
    '''
    INPUT: Pandas dataframe with US Health information for the US
           https://catalog.data.gov/dataset/community-health-status-indicators-chsi-to-combat-obesity-heart-disease-and-cancer
    OUTPUT: Pandas dataframe with Alcohol, Health Status, and Unhealthy Days for CA counties
    '''
    df = df[df['State_FIPS_Code'] == 6]
    x = ['County_FIPS_Code', 'Max_ALE', 'Max_Health_Status', 'Max_Unhealthy_Days']
    df = df[x]
    # Changing names of columns to make more sense
    df.columns = ['C Fips', 'Alcohol', 'Health_Status', 'Unhealthy_Days']
    return df

def Insurance(df):
    '''
    INPUT: Pandas dataframe with US Insurance information https://www.data.gov/
    OUTPUT: Pandas dataframe with Uninsued and Medicare rates for CA counties
    '''
    df = df[df['State_FIPS_Code'] == 6]
    x = ['County_FIPS_Code', 'Uninsured', 'Elderly_Medicare', 'Disabled_Medicare']
    df = df[x]
    # Elderly Medicare is very predictive of cancer rates
    df.columns = ['C Fips', 'Uninsured', 'Elderly_Medicare', 'Disabled_Medicare']
    return df

def Infections(df):
    '''
    INPUT: Pandas dataframe with US Infection by county for many years
           https://data.chhs.ca.gov/dataset/infectious-disease-cases-by-county-year-and-sex
    OUTPUT: Pandas dataframe rates of infections that might be correlated to
            cancer within CA counties
    '''
    # Drop the rows with CA - representing all counties
    df = df[df['County'] != 'California']
    # Drop rows with male and female seperated data
    df = df[df['Sex'] == 'Total']
    column = ['Disease', 'County', 'Year', 'Rate']
    df = df[column]
    # Take only rows with HIV, Hep B, and Hep C
    df = df[(df['Disease'] == 'HIV') | (df['Disease'] == 'Hepatitis B, Chronic') | (df['Disease'] == 'Hepatitis C, Chronic')]
    # Make a column for each of the unique infections
    df = pd.pivot_table(df,index=['County','Year'],columns='Disease',values ='Rate').reset_index()
    df.columns = ['Name', 'Year', 'HIV', 'Hep B', 'Hep C']
    df = df.merge(Fips,on='Name')
    df.drop('Name',1,inplace = True)
    return df

def tocsv(df,name):
    df.to_csv('/Users/d/Documents/Class/ZNA/Data/Cal/A2/{}.csv'.format(name), index=False)


if __name__ == '__main__':
    # Import one dataframe at a time, run it through its unique Functions
    # Save it as a csv in the location of the tocsv function
    # Then delete the dataframe to save pc memory
    Can = SEER(pd.read_csv('/Users/d/Documents/Class/ZNA/Data/Cal/CalCan.csv'))
    tocsv(Can,'Cancer')
    del Can
    Pop = POP(pd.read_csv('/Users/d/Documents/Class/ZNA/Data/Cal/CalPop.csv'))
    tocsv(Pop,'Population')
    del Pop
    Air = Air(pd.read_csv('/Users/d/Documents/Class/ZNA/Data/Cal/CalAir.csv'))
    tocsv(Air,'Air')
    del Air
    Fips = pd.read_csv('/Users/d/Documents/Class/ZNA/Data/Cal/FIPS.csv')
    tocsv(Fips,'Fips')
    Super = Super(pd.read_csv('/Users/d/Documents/Class/ZNA/Data/Cal/SuperSites.csv'))
    tocsv(Super,'Superfund')
    del Super
    Frack = Frack(pd.read_csv('/Users/d/Documents/Class/ZNA/Data/Cal/FrackCA.csv'))
    tocsv(Frack,'Fracking')
    del Frack
    Rad = Radon(pd.read_csv('/Users/d/Documents/Class/ZNA/Data/Cal/Radon.csv'))
    tocsv(Rad,'Radon')
    del Rad
    TRI = TRI(pd.read_csv('/Users/d/Documents/Class/ZNA/Data/Cal/CalTRI.csv'))
    tocsv(TRI,'TRI')
    del TRI
    Edu = EDU(pd.read_csv('/Users/d/Documents/Class/ZNA/Data/Cal/EducationReport.csv'))
    tocsv(Edu,'Education')
    del Edu
    Pov = Poverty(pd.read_csv('/Users/d/Documents/Class/ZNA/Data/Cal/PovertyReport.csv'))
    tocsv(Pov,'Poverty')
    del Pov
    Employed = Employed(pd.read_csv('/Users/d/Documents/Class/ZNA/Data/Cal/UnemploymentReport.csv'))
    tocsv(Employed,'Employment')
    del Employed
    VunPop = VunPop(pd.read_csv('/Users/d/Documents/Class/ZNA/Data/Cal/VUNERABLEPOPSANDENVHEALTH.csv'))
    tocsv(VunPop,'Vunerable')
    del VunPop
    Health = HealthStat(pd.read_csv('/Users/d/Documents/Class/ZNA/Data/Cal/SUMMARYMEASURESOFHEALTH.csv'))
    tocsv(Health,'Health')
    del Health
    Insurance = Insurance(pd.read_csv('/Users/d/Documents/Class/ZNA/Data/Cal/RISKFACTORSANDACCESSTOCARE.csv'))
    tocsv(Insurance,'Insurance')
    del Insurance
    Infect = Infections(pd.read_csv('/Users/d/Documents/Class/ZNA/Data/Cal/infectiousCa.csv'))
    tocsv(Infect,'Infections')
    del Infect
    del Fips
