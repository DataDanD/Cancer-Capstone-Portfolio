import pandas as pd
import numpy as np

def SEER(df):
    df = df[df['Year'] > 2000]
    # df.loc[ df['Age at diagnosis'] <= 30, 'Age at diagnosis'] = 0
    # df.loc[(df['Age at diagnosis'] > 30) & (df['Age at diagnosis'] <= 60), 'Age at diagnosis'] = 1
    # df.loc[ df['Age at diagnosis'] > 60, 'Age at diagnosis'] = 2
    # group1=['Year of diagnosis', 'State-county recode', 'Sex',
    # 'Age at diagnosis', 'Race recode (White, Black, Other)']
    group2=['Year of diagnosis', 'State-county recode']
    df['Count'] = 0
    df = df.groupby(by=group1)['Count'].count()
    df = pd.DataFrame(new).reset_index()
    df['C Fips'] = (df['C Fips']-6000)
    df.columns = ['C Fips', 'Year', 'Count']
    # df.columns = ['Sex', 'Age', 'C Fips', 'Race', 'Year', 'Count']
    return df

def POP(df):
    # df.loc[ dff['Age'] <= 6, 'Age'] = 0
    # df.loc[(dff['Age'] > 6) & (df['Age'] <= 12), 'Age'] = 1
    # df.loc[ dff['Age'] > 12, 'Age'] = 2
    # dff = df.groupby(['Year','C Fips','Race','Sex','Age'])['Population'].sum()
    dff = df.groupby(['Year','C Fips'])['Population'].sum()
    dff = pd.DataFrame(dff).reset_index()
    return dff

def Air(df):
    df = df[df['Year'] > 2000]
    dff['CountyFips'] = dff['CountyFips']-6000
    dff = dff.drop('Unnamed: 0',1)
    x = ['MeasureId', 'MeasureType', 'CountyFips',
         'ReportYear', 'Unit', 'UnitName', 'Value']
    newdf = dff[x]
    Air = pd.pivot_table(newdf,index=['CountyFips','ReportYear'],columns='MeasureId',values ='Value').reset_index()
    Air.columns = ['C Fips', 'Year', 292, 293, 294, 295, 296]
    # Use 292 294 as the Air Quality measures
    return Air

def TRI(df):
    # filter out grams from unit measure
    xx = ['YEAR','COUNTY','CHEMICAL','ON-SITE_RELEASE_TOTAL']
    TT = df[xx]
    dff = TT.groupby(['YEAR','COUNTY','CHEMICAL'])['ON-SITE_RELEASE_TOTAL'].sum()
    T = pd.pivot_table(df,index=['COUNTY','YEAR'],columns='CHEMICAL',values ='ON-SITE_RELEASE_TOTAL').reset_index()
    return T

def Frack(df):
    df['has_fracking'] = 0
    df = df['CountyName', 'has_fracking']
    df = df.groupby(['CountyName'])['has_fracking'].count().reset_index()
    f.columns = ['Name', 'has_fracking']
    df = df.merge(Fips,on='Name')
    df = df.drop(['Name'],1)
    return df

def Super(df):
    df['Name'] = df['County_name'].map(lambda x: str(x)[:-7])
    df = df.merge(Fips,on='Name')
    df = df.drop(['Name','County_name','Unnamed: 0'],1)
    return df

def Radon(df):
    df = df[df['state'] == 'CA']
    df = df.drop(['idnum', 'state', 'state2', 'stfips', 'zip', 'region', 'typebldg', 'floor', 'room', 'basement', 'windoor', 'rep', 'stratum', 'wave', 'starttm', 'stoptm', 'startdt', 'stopdt', 'dupflag', 'zipflag', 'county'], 1)
    df = df.groupby('cntyfips')['activity'].mean().reset_index()
    df.columns = ['C Fips', 'Radon']
    return df

def Disease(df):
    return df

def Infect(df):
    return df



if __name__ == '__main__':
    #Load Data
    Fips = pd.read_csv('Data/Cleaner/FIPS.csv')
    Cancer = SEER(pd.read_csv('Data/Cleaner/Cancer.csv'))
    Population = POP(pd.read_csv('Data/Cleaner/PopPop.csv'))
    Air = Air(pd.read_csv('Data/Cleaner/Air.csv'))
    TRI = TRI(pd.read_csv('Data/Cleaner/TRI.csv'))
    Frack = Frack(pd.read_csv('Data/Cleaner/Frackit.csv'))
    Super = Super(pd.read_csv('Data/Cleaner/SuperSites.csv'))
    Chronic = Disease(pd.read_csv('Data/Cleaner/Chronic.csv'))
    Infect = Infect(pd.read_csv('Data/Cleaner/Infect.csv'))
    Radon = Radon(pd.read_csv('Data/Cleaner/Radon.csv'))

    #Joins
    ndf = pd.merge(Cancer, Population, how='left', on=['Year','C Fips','Race','Sex','Age'])
    ndf['Rate'] = ndf['Count'] / ndf['Population']
    ndf = pd.merge(Air, ndf, how='left', on=['Year','C Fips'])
    ndf = pd.merge(TRI, ndf, how='left', on=['Year',''])
    ndf = ndf.merge(Super,how='left', on='C Fips')
    ndf['has_superfund'] = ndf['has_superfund'].fillna(0)
    ndf = ndf.merge(Super,how='left', on='C Fips')
    ndf['has_fracking'] = ndf['has_superfund'].fillna(0)
    ndf = nfd.merge(Radon,how='left', on='C Fips')
    ndf = ndf[ndf['C Fips'] != 3]
