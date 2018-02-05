# Model
import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import GridSearchCV
from sklearn.cross_validation import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.model_selection import GridSearchCV, cross_val_score, KFold
from sklearn.linear_model import LinearRegression, LassoCV, LassoLarsCV, LassoLarsIC
from sklearn.preprocessing import StandardScaler, MinMaxScaler, scale, normalize
import seaborn as sns


# Preprocessing
# min_max=MinMaxScaler()
# scaler = StandardScaler()


# Read
df = pd.read_csv('Cancer.csv')
z = df.pop('Count')
y = df.pop('Cancer Rate')
X = df
# X = df.drop(['Count'],1)

# Transform
X_train, X_test, y_train, y_test = train_test_split(X, y)
# scaler.fit(X_train)
# X_train=scaler.transform(X_train)
# X_test=scaler.transform(X_test)
# X_train=min_max.fit_transform(X_train)
# X_test=min_max.fit_transform(X_test)
# X_train=normalize(X_train)
# X_test=normalize(X_test)

parameters = {'fit_intercept':[True,False], 'normalize':[True,False], 'copy_X':[True,False]}

lin = LinearRegression()
linsearch = GridSearchCV(lin, parameters, cv=10, scoring='neg_mean_squared_error')

model = linsearch.fit(X_train, y_train)

print('best params')
print(model.best_params_)
print('best score {}'.format(model.best_score_))
mae = float(str(round(mean_absolute_error(y_test, model.predict(X_test)),2)))
rmse = float(str(round((mean_squared_error(y_test,model.predict(X_test))**.5),2)))

f,ax=plt.subplots(1,1,figsize=(8,6))

sns.distplot(model.predict(X_test), color='blue',
    kde_kws={"color": "blue", "lw": 2, "label": "prediction"})
sns.distplot(y_test, color = 'green',
    kde_kws={"color": "green", "lw": 2, "label": "actual"})
ax.set_title('Linear Model Predictions')
ax.text(1100, .0023, "MAE {}".format(mae),
        verticalalignment='bottom', horizontalalignment='right',
        color='red', fontsize=10)
ax.text(1100, .0021, "RMSE {}".format(rmse),
        verticalalignment='bottom', horizontalalignment='right',
        color='red', fontsize=10)
# ax.text(100, .0025, "Best Parameters {}".format(model.param_grid),
#         verticalalignment='bottom', horizontalalignment='left',
#         color='red', fontsize=10)
plt.show()



# Train
# kfold = KFold(n_splits=10)
# model = clf.fit(X_train, y_train)
# print(cross_val_score(clf, X_train, y_train, cv = kfold, scoring='r2'))
# print(cross_val_score(clf, X_train, y_train, cv = kfold, scoring='r2').mean())
# rresult=cross_val_score(clf, X_train, y_train, cv = kfold, scoring='neg_mean_squared_error')
# print(model.score(X_test, y_test), 1 - (1-model.score(X_test, y_test))*(len(y_test)-1)/(len(y_test)-X_test.shape[1]-1))
# print(clf.score(X_test, y_test))
# print(mean_squared_error(y_test,model.predict(X_test)))
# print(r2_score(y_test,model.predict(X_test)))
# rresult=cross_val_score(clf, X_train, y_train, cv = kfold, scoring='neg_mean_squared_error')
# print(float(str(round(abs(rresult.mean())**.5,4))))
# return model
