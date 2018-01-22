import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from catboost import CatBoostRegressor, Pool
from sklearn.model_selection import GridSearchCV, cross_val_score, KFold
from sklearn.cross_validation import train_test_split
from sklearn.metrics import r2_score, mean_squared_error

df = pd.read_csv('/Users/d/Documents/Class/ZNA/df.csv')
y = df.pop('Cancer Rate')
X = df

X_train, X_test, y_train, y_test = train_test_split(X, y)

# parameters = {'depth':[6,9],
#      'iterations':[1000,1500],
#      'learning_rate':[.03,.3],
#      'l2_leaf_reg':[5,10],
#      'border_count':[20,40]}
# cat = CatBoostRegressor()
# cat = GridSearchCV(cat, parameters, cv=5, scoring='neg_mean_squared_error')
cat = CatBoostRegressor(depth=10,
     iterations=1500,
     learning_rate=.5,
     l2_leaf_reg=7,
     border_count=35)
cresult=cross_val_score(cat,X,y,cv=10,scoring='r2')
kfold = KFold(n_splits=10)
model = cat.fit(X_train, y_train)
print(cross_val_score(cat, X_train, y_train, cv = kfold, scoring='r2'))
print(cross_val_score(cat, X_train, y_train, cv = kfold, scoring='r2').mean())
print(model.score(X_test, y_test), 1 - (1-model.score(X_test, y_test))*(len(y_test)-1)/(len(y_test)-X_test.shape[1]-1))
print(cat.score(X_test, y_test))
print(mean_squared_error(y_test,model.predict(X_test)))
print(r2_score(y_test,model.predict(X_test)))

print(cresult)

one_hot = pd.get_dummies(X)
categorical_features_indices = np.where(one_hot.dtypes != np.float)[0]
one_hot = (one_hot - one_hot.mean()) / (one_hot.max() - one_hot.min())
categorical_features_indices = np.where(one_hot.dtypes != np.float)[0]
feature_score = pd.DataFrame(list(zip(one_hot.dtypes.index, model.get_feature_importance(Pool(one_hot, label=y, cat_features=categorical_features_indices)))),columns=['Feature','Score'])
feature_score = feature_score.sort_values(by='Score', ascending=False, inplace=False, kind='quicksort', na_position='last')[:]
plt.rcParams["figure.figsize"] = (12,7)
ax = feature_score.plot('Feature', 'Score', kind='bar', color='c')
ax.set_title("Catboost Feature Importance Ranking", fontsize = 14)
ax.set_xlabel('')
rects = ax.patches
# get feature score as labels round to 2 decimal
labels = feature_score['Score'].round(2)
for rect, label in zip(rects, labels):
   height = rect.get_height()
   ax.text(rect.get_x() + rect.get_width()/2, height + 0.35, label, ha='center', va='bottom')
plt.tight_layout()
plt.show()
