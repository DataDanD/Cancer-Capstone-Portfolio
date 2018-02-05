import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import AdaBoostRegressor, GradientBoostingRegressor, RandomForestRegressor
from sklearn.linear_model import LinearRegression, LassoCV, LassoLarsCV, LassoLarsIC
from sklearn.model_selection import GridSearchCV, cross_val_score, KFold
from sklearn.preprocessing import StandardScaler, MinMaxScaler, scale, normalize
from xgboost import XGBRegressor
from catboost import CatBoostRegressor, Pool
import lightgbm as lgb
from sklearn.linear_model import LinearRegression

# read data
df = pd.read_csv('Cancer.csv')
z = df.pop('Count')
y = df.pop('Cancer Rate')
X = df

# Boosting models with MAE and RMSE
# Can make a function to score the 5 models
rf=RandomForestRegressor()
rresult=cross_val_score(rf,X,y,cv=10,scoring='neg_mean_squared_error')
rresult=float(str(round(abs(rresult.mean())**.5,2)))
rr2=abs(float(str(round(cross_val_score(rf,X,y,cv=10,scoring='neg_mean_absolute_error').mean(),2))))

ada=AdaBoostRegressor()
aresult=cross_val_score(ada,X,y,cv=10,scoring='neg_mean_squared_error')
aresult=float(str(round(abs(aresult.mean())**.5,2)))
ar2=abs(float(str(round(cross_val_score(ada,X,y,cv=10,scoring='neg_mean_absolute_error').mean(),2))))

grad=GradientBoostingRegressor()
gresult=cross_val_score(grad,X,y,cv=10,scoring='neg_mean_squared_error')
gresult=float(str(round(abs(gresult.mean())**.5,2)))
gr2=abs(float(str(round(cross_val_score(grad,X,y,cv=10,scoring='neg_mean_absolute_error').mean(),2))))

xgboost=XGBRegressor()
xresult=cross_val_score(xgboost,X,y,cv=10,scoring='neg_mean_squared_error')
xresult=float(str(round(abs(xresult.mean())**.5,2)))
xr2=abs(float(str(round(cross_val_score(xgboost,X,y,cv=10,scoring='neg_mean_absolute_error').mean(),2))))

cat=CatBoostRegressor()
cresult=cross_val_score(cat,X,y,cv=10,scoring='neg_mean_squared_error')
cresult=float(str(round(abs(cresult.mean())**.5,2)))
cr2=abs(float(str(round(cross_val_score(cat,X,y,cv=10,scoring='neg_mean_absolute_error').mean(),2))))

#feat importance graph
f,ax=plt.subplots(2,2,figsize=(17,9))

font_size = 15
plt.rcParams.update({'font.size': font_size})
plt.rcParams['xtick.labelsize'] = font_size-2
plt.rcParams['ytick.labelsize'] = font_size-2


model=RandomForestRegressor()
model.fit(X,y)
pd.Series(model.feature_importances_,X.columns).sort_values(ascending=True)[-7:].plot.barh(width=0.8,ax=ax[0,0],cmap='summer')
ax[0,0].set_title('Top 7 Feature Relevance in Random Forests',fontsize=20)
ax[0,0].text(0.6, 1.51, "RMSE {}".format(rresult),
        verticalalignment='bottom', horizontalalignment='right',
        color='lime', fontsize=20)
ax[0,0].text(0.6, 0.51, "MAE {}".format(rr2),
        verticalalignment='bottom', horizontalalignment='right',
        color='lime', fontsize=20)
# ax[0,0].yticks(fontsize=15)


model=GradientBoostingRegressor()
model.fit(X,y)
pd.Series(model.feature_importances_,X.columns).sort_values(ascending=True)[-7:].plot.barh(width=0.8,ax=ax[0,1],cmap='autumn')
ax[0,1].set_title('Top 7 Feature Relevance in Gradient Boosting',fontsize=20)
ax[0,1].text(0.175, 1.51, "RMSE {}".format(gresult),
        verticalalignment='bottom', horizontalalignment='right',
        color='crimson', fontsize=20)
ax[0,1].text(0.175, 0.51, "MAE {}".format(gr2),
        verticalalignment='bottom', horizontalalignment='right',
        color='crimson', fontsize=20)
# ax[0,1].plt.yticks(fontsize=15)


model=AdaBoostRegressor()
model.fit(X,y)
pd.Series(model.feature_importances_,X.columns).sort_values(ascending=True)[-7:].plot.barh(width=0.8,ax=ax[1,0],cmap='spring')
ax[1,0].set_title('Top 7 Feature Relevance in AdaBoost',fontsize=20)
ax[1,0].text(0.4, 1.51, "RMSE {}".format(aresult),
        verticalalignment='bottom', horizontalalignment='right',
        color='magenta', fontsize=20)
ax[1,0].text(0.4, 0.51, "MAE {}".format(ar2),
        verticalalignment='bottom', horizontalalignment='right',
        color='magenta', fontsize=20)
# ax[1,0].plt.yticks(fontsize=15)


model=CatBoostRegressor()
model.fit(X,y)
pd.Series(model.feature_importances_,X.columns).sort_values(ascending=True)[-7:].plot.barh(width=0.8,ax=ax[1,1],cmap='winter')
ax[1,1].set_title('Top 7 Feature Relevance in CatBoost',fontsize=20)
ax[1,1].text(17.5, 1.51, "RMSE {}".format(cresult),
        verticalalignment='bottom', horizontalalignment='right',
        color='teal', fontsize=20)
ax[1,1].text(17.5, 0.51, "MAE {}".format(cr2),
        verticalalignment='bottom', horizontalalignment='right',
        color='teal', fontsize=20)
# ax[1,1].plt.yticks(fontsize=15)
# # plt.yticks(fontsize=15)
plt.tight_layout()
plt.subplots_adjust(hspace=.215)
plt.savefig("test5.png", dpi = (800))
plt.show()
