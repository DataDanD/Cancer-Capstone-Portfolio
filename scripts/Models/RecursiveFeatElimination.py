import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import GridSearchCV, cross_val_score
from sklearn.ensemble import GradientBoostingRegressor
import matplotlib.pyplot as plt

def RFE(df,current,X_train, X_test, y_train, y_test):
    diff = []
    scored = []
    cols = list(df.columns)
    for x in cols:
        z = df.pop(x)
        model.fit(X_train,y_train)
        rmse = float(str(round((mean_squared_error(y_test,model.predict(X_test))**.5),2)))
        new = rmse - current
        diff.append(new)
        scored.append(rmse)
        print(x)
        print(new)
    RMSE_list = pd.DataFrame(
    {'Feature': cols,
     'RMSE': scored,
     'diff': diff
    })
    graph = pd.DataFrame(
    {'Feature': cols,
     'diff': diff
    })
    return RMSE_list, graph, diff, cols

if __name__ == '__main__':
    df = pd.read_csv('Cancer.csv')
    z = df.pop('Count')
    y = df.pop('Cancer Rate')
    X = df
    X_train, X_test, y_train, y_test = train_test_split(X, y)

    model = GradientBoostingRegressor(
         max_depth = 3,
         max_features = 'auto',
         min_samples_leaf = 4,
         min_samples_split = 2,
         n_estimators = 1600)
    model.fit(X_train,y_train)
    current = float(str(round((mean_squared_error(y_test,model.predict(X_test))**.5),2)))
    print(current)
    fin, graph, diff, cols = RFE(df,current,X_train, X_test, y_train, y_test)
    print(fin)
    print(current)

    f,ax=plt.subplots(1,1,figsize=(15,12))
    pd.Series(diff,cols).sort_values(ascending=True)[15:].plot.barh(width=0.8,ax=ax,cmap='autumn')
    ax.set_title('Top 15 Feature importance in Final Model',fontsize=40)
    plt.show()

 
# f,ax=plt.subplots(1,1,figsize=(15,12))
# pd.Series(x,y).sort_values(ascending=True).plot.barh(width=0.
# 8,ax=ax,color='purple')
# ax.set_title('Top 15 Feature importance in Final Model')
# plt.show()


# [(1, 'Carcinogen'), (1, 'Disabled Medicare'), (1, 'Drug Use'), (1, 'HIV'), (1, 'Hep B'), (1, 'Hep C'), (1, 'Major Depression'), (1, 'Medicare Population'), (1, 'Ozone'), (1, 'PM2.5'), (1, 'Population'), (1, 'Uninsured'), (1, 'Work Disabled'), (2, 'Not Carcinogen'), (3, 'Year'), (4, 'C Fips'), (5, 'Radon'), (6, 'Unemployed'), (7, 'Education'), (8, 'Health Status'), (9, 'Alcohol'), (10, 'Median Income'), (11, 'Unhealthy Days'), (12, 'Poverty'), (13, 'Fracking'), (14, 'Superfund')]
