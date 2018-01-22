import pandas as pd

# The merge function that will merge everything
def merge(df1,df2,group):
    df = pd.merge(df1,df2,how='left',on=group)
    return df

# Cancer has to start on the very left and then we can join every dataframe to that one with left merges. Going from 14 files to one dataframe that we can run models on
if __name__ == '__main__':
    # Read, Merge, Delete
    Cancer = pd.read_csv('/Users/d/Documents/Class/ZNA/Data/Cal/A2/Cancer.csv')
    Population = pd.read_csv('/Users/d/Documents/Class/ZNA/Data/Cal/A2/Population.csv')
    df = merge(Cancer,Population,['Year','C Fips'])
    del Cancer
    del Population
    Air = pd.read_csv('/Users/d/Documents/Class/ZNA/Data/Cal/A2/Air.csv')
    df = merge(df,Air,['Year','C Fips'])
    del Air
    TRI = pd.read_csv('/Users/d/Documents/Class/ZNA/Data/Cal/A2/TRI.csv')
    df = merge(df,TRI,['Year','C Fips'])
    del TRI
    Super = pd.read_csv('/Users/d/Documents/Class/ZNA/Data/Cal/A2/Superfund.csv')
    df = merge(df,Super,'C Fips')
    del Super
    Frack = pd.read_csv('/Users/d/Documents/Class/ZNA/Data/Cal/A2/Fracking.csv')
    df = merge(df,Frack,['C Fips'])
    del Frack
    Radon = pd.read_csv('/Users/d/Documents/Class/ZNA/Data/Cal/A2/Radon.csv')
    df = merge(df, Radon, ['C Fips'])
    del Radon
    Edu = pd.read_csv('/Users/d/Documents/Class/ZNA/Data/Cal/A2/Education.csv')
    df = merge(df, Edu, ['C Fips'])
    del Edu
    Pov = pd.read_csv('/Users/d/Documents/Class/ZNA/Data/Cal/A2/Poverty.csv')
    df = merge(df, Pov, ['C Fips'])
    del Pov
    Employed = pd.read_csv('/Users/d/Documents/Class/ZNA/Data/Cal/A2/Employment.csv')
    df = merge(df, Employed, ['C Fips'])
    del Employed
    VunPop = pd.read_csv('/Users/d/Documents/Class/ZNA/Data/Cal/A2/Vunerable.csv')
    df = merge(df, VunPop, ['C Fips'])
    del VunPop
    Health = pd.read_csv('/Users/d/Documents/Class/ZNA/Data/Cal/A2/Health.csv')
    df = merge(df, Health, ['C Fips'])
    del Health
    Insurance = pd.read_csv('/Users/d/Documents/Class/ZNA/Data/Cal/A2/Insurance.csv')
    df = merge(df, Insurance, ['C Fips'])
    del Insurance
    Infections = pd.read_csv('/Users/d/Documents/Class/ZNA/Data/Cal/A2/Infections.csv')
    df = merge(df, Infections, ['Year','C Fips'])
    del Infections

    # Engineer
    df = df[df['Year'] < 2012]
    # What should the cancer population incident rate be? Most features are out of 100. Keep it 100.
    df['Cancer Rate'] = (df['Count'] / df['Population']) * 100
    # Some NAs need filling
    df['Superfund'] = df['has_superfund'].fillna(0)
    df['Fracking'] = df['has_fracking'].fillna(0)
    # Could do one massive dump vs a few drops
    df.drop(['has_superfund','has_fracking'],1,inplace=True)
    df['Not Carcinogen'] = df['Not Carcinogen'].fillna(0)
    df['Carcinogen'] = df['Carcinogen'].fillna(0)
    # C Fips 3 did not have radon data. Not making it up
    df = df[df['C Fips'] != 3]
    # Same as cancer incident rate
    df['Uninsured'] = df['Uninsured'] / df['Population'] * 100
    df['Elderly Medicare'] = df['Elderly_Medicare'] / df['Population'] * 100
    df['Disabled Medicare'] = df['Disabled_Medicare'] / df['Population'] * 100
    df.drop(['Elderly_Medicare','Disabled_Medicare'],1,inplace=True)
    # Make better feature names
    df['Work Disabled'] = df['Sev_Work_Disabled'] / df['Population'] * 100
    df['Drug Use'] = df['Recent_Drug_Use'] / df['Population'] * 100
    df['Major Depression'] = df['Major_Depression'] / df['Population'] * 100
    df.drop(['Sev_Work_Disabled','Recent_Drug_Use','Major_Depression'],1,inplace=True)
    # Cut the % sign in this column and make it a flat like the others
    df['Median Income'] = df['Median Income'].map(lambda x: str(x)[:-1]).astype('float')

    # Save
    df.to_csv('/Users/d/Documents/Class/ZNA/df.csv',index=False)
