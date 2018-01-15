# Model
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from catboost import CatBoostRegressor, Pool
from sklearn.cross_validation import train_test_split
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.model_selection import GridSearchCV, cross_val_score, KFold
from sklearn.linear_model import LinearRegression


def mod(df):
    y = df.pop('Rate')
    X = df
    # X = df.drop(['Count'],1)
    X_train, X_test, y_train, y_test = train_test_split(X, y)
    kfold = KFold(n_splits=10)
    # parameters = {'depth':[6,9],  #                 9
    #       'iterations':[1000,1500],  #           1100-1125
    #       'learning_rate':[.03,.3],  #      .031-.0325
    #       'l2_leaf_reg':[5,10],  #         2.25-2.35
    #       'border_count':[20,40]}
    # cat = CatBoostRegressor()
    # clf = GridSearchCV(cat, parameters, cv=2, scoring='neg_mean_squared_error')
    clf = CatBoostRegressor(depth=10,
          iterations=2000,
          learning_rate=.5,
          l2_leaf_reg=7,
          border_count=35)
    # clf = LinearRegression(normalize=True)
    model = clf.fit(X_train, y_train)
    print(cross_val_score(clf, X_train, y_train, cv = kfold, scoring='r2'))
    # print(cross_val_score(clf, X_train, y_train, cv = kfold, scoring='r2').mean())
    # print(clf.score(X_test, y_test))
    # print(mean_squared_error(y_test,model.predict(X_test)))
    # print(r2_score(y_test,model.predict(X_test)))

    # one_hot = pd.get_dummies(X)
    # categorical_features_indices = np.where(one_hot.dtypes != np.float)[0]
    # one_hot = (one_hot - one_hot.mean()) / (one_hot.max() - one_hot.min())
    # categorical_features_indices = np.where(one_hot.dtypes != np.float)[0]
    # feature_score = pd.DataFrame(list(zip(one_hot.dtypes.index, model.get_feature_importance(Pool(one_hot, label=y, cat_features=categorical_features_indices)))),columns=['Feature','Score'])
    # feature_score = feature_score.sort_values(by='Score', ascending=False, inplace=False, kind='quicksort', na_position='last')[:15]
    # plt.rcParams["figure.figsize"] = (12,7)
    # ax = feature_score.plot('Feature', 'Score', kind='bar', color='c')
    # ax.set_title("Catboost Feature Importance Ranking", fontsize = 14)
    # ax.set_xlabel('')
    # rects = ax.patches
    # # get feature score as labels round to 2 decimal
    # labels = feature_score['Score'].round(2)
    # for rect, label in zip(rects, labels):
    #     height = rect.get_height()
    #     ax.text(rect.get_x() + rect.get_width()/2, height + 0.35, label, ha='center', va='bottom')
    # plt.tight_layout()
    # plt.show()
    return model


if __name__ == '__main__':
    model = mod(pd.read_csv('/Users/d/Documents/Class/ZNA/Data/Cleaner/MVP/RadSupFraAirCan.csv'))
