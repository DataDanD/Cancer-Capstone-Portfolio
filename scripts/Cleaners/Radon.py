import pandas as pd

def load():
    df1 = pd.read_csv('http://www.stat.columbia.edu/~gelman/arm/examples/radon_complete/srrs1.dat')
    df2 = pd.read_csv('http://www.stat.columbia.edu/~gelman/arm/examples/radon_complete/srrs2.dat')
    df3 = pd.read_csv('http://www.stat.columbia.edu/~gelman/arm/examples/radon_complete/srrs3.dat')
    df4 =  pd.read_csv('http://www.stat.columbia.edu/~gelman/arm/examples/radon_complete/srrs4.dat')
    df5 = pd.read_csv('http://www.stat.columbia.edu/~gelman/arm/examples/radon_complete/srrs5.dat')
    df = pd.concat([df1, df2, df3, df4, df5])
    df.columns = df.columns.map(str.strip)
    return df

if __name__ == '__main__':
    df = load()
    df.to_csv('Data/Cleaner/Radon.csv', index=False)
