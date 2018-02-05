import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from sklearn.model_selection import GridSearchCV, cross_val_score, KFold
from sklearn.preprocessing import StandardScaler, MinMaxScaler, normalize
from xgboost import XGBRegressor

df = pd.read_csv('Cancer.csv')
y = df.pop('Cancer Rate')
X = df
X_train, X_test, y_train, y_test = train_test_split(X, y)

params={
    'max_depth': [3], #[2,3,4,5,6,7,8,9]
    'subsample': [.725], #[0.4,0.5,0.6,0.7,.75,0.8,.85,0.9,1.0]
    'colsample_bytree': [.825], #[0.5,0.6,0.7,.75,0.8,.85]
    'n_estimators': [1750], #[1000,1400,1500,1600,1700,2000,3000]
    'reg_alpha': [.065] #[0.01, 0.02, 0.03, 0.04]
}
xgb = XGBRegressor()
xgbsearch = GridSearchCV(xgb, params, cv=5, scoring='neg_mean_squared_error')

model = xgbsearch.fit(X_train, y_train)
print('best params')
print(model.best_params_)
print('best score {}'.format(model.best_score_))
print('MAE {}'.format(float(str(round(mean_absolute_error(y_test, model.predict(X_test)),8)))))
print('RMSE {}'.format(float(str(round((mean_squared_error(y_test, model.predict(X_test))**.5),8)))))
