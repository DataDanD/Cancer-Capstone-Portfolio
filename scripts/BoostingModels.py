#boosting model
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

# read data
df = pd.read_csv('df.csv')
z = df.pop('Count')
y = df.pop('Cancer Rate')
X = df

def rmse(predictions, targets):
    return np.sqrt(((predictions - targets) ** 2).mean())

# Boosting models with R2 and RMSE
# Can make a function to score the 5 models
rf=RandomForestRegressor()
rresult=cross_val_score(rf,X,y,cv=10,scoring='neg_mean_squared_error')
rresult=float(str(round(abs(rresult.mean())**.5,4)))
rr2=float(str(round(cross_val_score(rf,X,y,cv=10,scoring='r2').mean(),4)))

ada=AdaBoostRegressor()
aresult=cross_val_score(ada,X,y,cv=10,scoring='neg_mean_squared_error')
aresult=float(str(round(abs(aresult.mean())**.5,4)))
ar2=float(str(round(cross_val_score(ada,X,y,cv=10,scoring='r2').mean(),4)))

grad=GradientBoostingRegressor()
gresult=cross_val_score(grad,X,y,cv=10,scoring='neg_mean_squared_error')
gresult=float(str(round(abs(gresult.mean())**.5,4)))
gr2=float(str(round(cross_val_score(grad,X,y,cv=10,scoring='r2').mean(),4)))

xgboost=XGBRegressor()
xresult=cross_val_score(xgboost,X,y,cv=10,scoring='neg_mean_squared_error')
xresult=float(str(round(abs(xresult.mean())**.5,4)))
xr2=float(str(round(cross_val_score(xgboost,X,y,cv=10,scoring='r2').mean(),4)))

cat=CatBoostRegressor()
cresult=cross_val_score(cat,X,y,cv=10,scoring='neg_mean_squared_error')
cresult=float(str(round(abs(cresult.mean())**.5,4)))
cr2=float(str(round(cross_val_score(cat,X,y,cv=10,scoring='r2').mean(),4)))

#feat importance graph
f,ax=plt.subplots(2,2,figsize=(15,12))

model=RandomForestRegressor()
model.fit(X,y)
pd.Series(model.feature_importances_,X.columns).sort_values(ascending=True).plot.barh(width=0.8,ax=ax[0,0],cmap='summer')
ax[0,0].set_title('Feature Importance in Random Forests')
ax[0,0].text(0.6, 5.01, "RMSE {}".format(rresult),
        verticalalignment='bottom', horizontalalignment='right',
        color='lime', fontsize=20)
ax[0,0].text(0.6, 2.51, "R2 {}".format(rr2),
        verticalalignment='bottom', horizontalalignment='right',
        color='lime', fontsize=20)

model=GradientBoostingRegressor()
model.fit(X,y)
pd.Series(model.feature_importances_,X.columns).sort_values(ascending=True).plot.barh(width=0.8,ax=ax[0,1],cmap='autumn')
ax[0,1].set_title('Feature Importance in Gradient Boosting')
ax[0,1].text(0.15, 5.01, "RMSE {}".format(gresult),
        verticalalignment='bottom', horizontalalignment='right',
        color='crimson', fontsize=20)
ax[0,1].text(0.15, 2.51, "R2 {}".format(gr2),
        verticalalignment='bottom', horizontalalignment='right',
        color='crimson', fontsize=20)

model=AdaBoostRegressor()
model.fit(X,y)
pd.Series(model.feature_importances_,X.columns).sort_values(ascending=True).plot.barh(width=0.8,ax=ax[1,0],cmap='spring')
ax[1,0].set_title('Feature Importance in AdaBoost')
ax[1,0].text(0.4, 5.01, "RMSE {}".format(aresult),
        verticalalignment='bottom', horizontalalignment='right',
        color='magenta', fontsize=20)
ax[1,0].text(0.4, 2.51, "R2 {}".format(ar2),
        verticalalignment='bottom', horizontalalignment='right',
        color='magenta', fontsize=20)

model=CatBoostRegressor()
model.fit(X,y)
pd.Series(model.feature_importances_,X.columns).sort_values(ascending=True).plot.barh(width=0.8,ax=ax[1,1],cmap='winter')
ax[1,1].set_title('Feature Importance in CatBoost')
ax[1,1].text(15, 5.01, "RMSE {}".format(cresult),
        verticalalignment='bottom', horizontalalignment='right',
        color='teal', fontsize=20)
ax[1,1].text(15, 2.51, "R2 {}".format(cr2),
        verticalalignment='bottom', horizontalalignment='right',
        color='teal', fontsize=20)

plt.tight_layout()
plt.show()

print('The RMSE cross validated score for AdaBoost is:',aresult)
print('The RMSE cross validated score for Random Forest is:',rresult)
print('The RMSE cross validated score for Gradient Boosting is:',gresult)
print('The RMSE cross validated score for XGBoost is:',xresult)
print('The RMSE cross validated score for Cat is:',cresult)
print()
print('The R2 cross validated score for AdaBoost is:',ar2)
print('The R2 cross validated score for Random Forest is:',rr2)
print('The R2 cross validated score for Gradient Boosting is:',gr2)
print('The R2 cross validated score for XGBoost is:',xr2)
print('The R2 cross validated score for Cat is:',cr2)


# Colormap
# Accent, Accent_r, Blues, Blues_r, BrBG, BrBG_r, BuGn, BuGn_r, BuPu, BuPu_r, CMRmap, CMRmap_r, Dark2, Dark2_r, GnBu, GnBu_r, Greens, Greens_r, Greys, Greys_r, OrRd, OrRd_r, Oranges, Oranges_r, PRGn, PRGn_r, Paired, Paired_r, Pastel1, Pastel1_r, Pastel2, Pastel2_r, PiYG, PiYG_r, PuBu, PuBuGn, PuBuGn_r, PuBu_r, PuOr, PuOr_r, PuRd, PuRd_r, Purples, Purples_r, RdBu, RdBu_r, RdGy, RdGy_r, RdPu, RdPu_r, RdYlBu, RdYlBu_r, RdYlGn, RdYlGn_r, Reds, Reds_r, Set1, Set1_r, Set2, Set2_r, Set3, Set3_r, Spectral, Spectral_r, Vega10, Vega10_r, Vega20, Vega20_r, Vega20b, Vega20b_r, Vega20c, Vega20c_r, Wistia, Wistia_r, YlGn, YlGnBu, YlGnBu_r, YlGn_r, YlOrBr, YlOrBr_r, YlOrRd, YlOrRd_r, afmhot, afmhot_r, autumn, autumn_r, binary, binary_r, bone, bone_r, brg, brg_r, bwr, bwr_r, cool, cool_r, coolwarm, coolwarm_r, copper, copper_r, cubehelix, cubehelix_r, flag, flag_r, gist_earth, gist_earth_r, gist_gray, gist_gray_r, gist_heat, gist_heat_r, gist_ncar, gist_ncar_r, gist_rainbow, gist_rainbow_r, gist_stern, gist_stern_r, gist_yarg, gist_yarg_r, gnuplot, gnuplot2, gnuplot2_r, gnuplot_r, gray, gray_r, hot, hot_r, hsv, hsv_r, inferno, inferno_r, jet, jet_r, magma, magma_r, nipy_spectral, nipy_spectral_r, ocean, ocean_r, pink, pink_r, plasma, plasma_r, prism, prism_r, rainbow, rainbow_r, seismic, seismic_r, spectral, spectral_r, spring, spring_r, summer, summer_r, tab10, tab10_r, tab20, tab20_r, tab20b, tab20b_r, tab20c, tab20c_r, terrain, terrain_r, viridis, viridis_r, winter, winter_r
