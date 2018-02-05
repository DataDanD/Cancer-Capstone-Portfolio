import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.model_selection import GridSearchCV, cross_val_score, KFold
from sklearn.preprocessing import StandardScaler, MinMaxScaler, normalize
from xgboost import XGBRegressor, plot_tree
from sklearn.feature_selection import RFE
from matplotlib.pylab import rcParams


df = pd.read_csv('Cancer.csv')
y = df.pop('Cancer Rate')
X = df
X_train, X_test, y_train, y_test = train_test_split(X, y)

xgb = XGBRegressor(
    max_depth = 3,
    subsample = 0.8,
    colsample_bytree = .85,
    n_estimators = 1600,
    reg_alpha = .03)

model = xgb.fit(X_train, y_train)

print('R2 {}'.format(float(str(round(r2_score(y_test, model.predict(X_test)),8)))))
print('RMSE {}'.format(float(str(round(mean_squared_error(y_test, model.predict(X_test)),8)))))

plot_tree(model, num_trees=2)

# plot_tree(model, num_trees=4)
# plot_tree(model, num_trees=0, rankdir='LR')

# Graphing the test train accuracy
# import matplotlib.pyplot as plt
# # compute test set deviance
# test_score = np.zeros((params['n_estimators'],), dtype=np.float64)
# for i, y_pred in enumerate(model.staged_decision_function(x_test)):
#     test_score[i] = model.loss_(y_test, y_pred)
# plt.figure(figsize=(12, 6))
# plt.subplot(1, 1, 1)
# plt.title('Deviance')
# plt.plot(np.arange(params['n_estimators']) + 1, model.train_score_, 'b-',
#                 label='Training Set Deviance')
# plt.plot(np.arange(params['n_estimators']) + 1, test_score, 'r-',
#                 label='Test Set Deviance')
# plt.legend(loc='upper right')
# plt.xlabel('Boosting Iterations')
# plt.ylabel('Deviance')

## Feature Importance in Final Model
feature_importance = model.feature_importances_
# make importances relative to max importance
feature_importance = 100.0 * (feature_importance / feature_importance.max())
sorted_idx = np.argsort(feature_importance)
pos = np.arange(sorted_idx.shape[0]) + .5
plt.figure(figsize=(12, 6))
plt.subplot(1, 1, 1)
plt.barh(pos, feature_importance[sorted_idx], align='center')
plt.yticks(pos, X.columns[sorted_idx])
plt.xlabel('Relative Importance')
plt.title('Variable Importance')
plt.show()
xgb.plot_importance(final_gb)
