import pandas as pd
import matplotlib.pyplot as plt
import re
import pickle,os,csv

indices = [(0,4),(4,6),(6,8),(8,11),(11,13),(13,14),(14,15),(15,16),(16,18),(18,26)]

clean_df = pd.DataFrame(columns=["Year", "State", "S Fips", "C Fips", "Registry", "Race", "Origin", "Sex", "Age", "Population"])

columns=["Year", "State", "S Fips", "C Fips", "Registry", "Race", "Origin",  "Sex", "Age", "Population"]

def pras(df):
    dct = {}
    for num in range(len(df)):
        lst = []
        x = df.iloc[num][0]
        for i in range(len(indices)):
            lst.append(x[indices[i][0]:indices[i][1]])
        dct[num] = lst
        if num%10000 ==0:
            print (num)
    return dct



if __name__=='__main__':
    textfile = '/Users/d/Documents/Class/ZNA/pop/us.1969_2016.19ages.txt'


    with open('{}.csv'.format(textfile[:-4]),'w') as csvfile:
        df = pd.read_table('/Users/d/Documents/Class/ZNA/pop/us.1969_2016.19ages.txt', header=None, index_col=None)
        dct = pras(df)
        writer = csv.writer(csvfile)
        writer.writerow(columns)
        writer.writerows(i for i in dct.values())
