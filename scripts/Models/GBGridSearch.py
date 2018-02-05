import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import GradientBoostingRegressor, RandomForestRegressor
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Cancer.csv')
y = df.pop('Cancer Rate')
X = df
X_train, X_test, y_train, y_test = train_test_split(X, y)

parameters = {
     'max_depth':[2], #[2,3,4,5,6,7,8]
     'max_features':['auto'], #['sqrt','log2','auto']
     'min_samples_leaf':[4], #[1,2,3,4,5]
     'min_samples_split':[4], #[2,3,4,5]
     'n_estimators': [1600] #[600,900,1100,1200,1300,1400,1500,1600]
}

cat = GradientBoostingRegressor()
catsearch = GridSearchCV(cat, parameters, cv=10, scoring='neg_mean_squared_error')

model = catsearch.fit(X_train, y_train)

print('best params')
print(model.best_params_)
print('best score {}'.format(model.best_score_))
mae = float(str(round(mean_absolute_error(y_test, model.predict(X_test)),2)))
rmse = float(str(round((mean_squared_error(y_test,model.predict(X_test))**.5),2)))

f,ax=plt.subplots(1,1,figsize=(15,8))

sns.distplot(model.predict(X_test), color='blue',
    kde_kws={"color": "blue", "lw": 2})
sns.distplot(y_test, color = 'green',
    kde_kws={"color": "green", "lw": 2})
ax.set_title('Final Gradient Boosting Model Predictions',fontsize=40)
ax.text(1100, .0023, "MAE {}".format(mae),
        verticalalignment='bottom', horizontalalignment='right',
        color='blue', fontsize=30)
ax.text(1100, .0021, "RMSE {}".format(rmse),
        verticalalignment='bottom', horizontalalignment='right',
        color='blue', fontsize=30)
plt.xlabel('Cancer Incident per 100,000', fontsize=25)

# increase legend size

plt.xticks(fontsize=20)
plt.yticks(fontsize=15)
plt.tight_layout()
plt.savefig("test33.png", dpi = (800))

plt.show()
