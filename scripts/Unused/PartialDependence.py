from sklearn.ensemble.partial_dependence import plot_partial_dependence
import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.model_selection import GridSearchCV, cross_val_score, KFold
from sklearn.preprocessing import StandardScaler, MinMaxScaler, normalize
from xgboost import XGBRegressor
from sklearn.feature_selection import RFE
from sklearn.ensemble import GradientBoostingRegressor, RandomForestRegressor


df = pd.read_csv('Cancer.csv')
y = df.pop('Cancer Rate')
X = df
X_train, X_test, y_train, y_test = train_test_split(X, y)



model = GradientBoostingRegressor(
                        max_depth=2,
                        max_features='auto',
                        min_samples_leaf=3,
                        min_samples_split=2,
                        n_estimators=1600)


clf = model.fit(X_train, y_train)
#20,21,22   ,12, 17,18,19
fig, axs = plot_partial_dependence(clf, X_train,
                                   features=[20,21,22],
                                   # features=[17,18,19],
                                   feature_names=X_train.columns,
                                   n_cols=2)
fig.tight_layout()
fig.show()
