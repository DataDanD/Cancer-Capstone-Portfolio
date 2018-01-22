import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LassoCV, LassoLarsCV, LassoLarsIC
from statsmodels.tsa.arima_model import ARIMA, ARMAResults



def plot_ic_criterion(model, name, color):
    mi = [150]
    alpha_ = model.alpha_
    alphas_ = model.alphas_
    criterion_ = model.criterion_
    # plt.plot(-np.log10(alphas_), criterion_, '--', color=color,
    #          linewidth=3, label='%s criterion' % name)
    # plt.axvline(-np.log10(alpha_), color=color, linewidth=3,
    #             label='alpha: %s estimate' % name)
    # plt.xlabel('-log(alpha)')
    # plt.ylabel('criterion')
    print(criterion_.min())



xx = ['Elderly Medicare', 'Year', 'Uninsured', 'Median Income', 'Health_Status', 'Unemployed', 'Population', 'Fracking', 'Ozone', 'Poverty', 'Unhealthy_Days', 'HIV', 'Hep B', 'Hep C', 'Alcohal','Superfund', 'Education', 'Disabled Medicare', 'Work Disabled', 'Not Carcinogen', 'Carcinogen', 'Drug Use','Major Depression', 'PM2.5','Radon', 'C Fips', 'Count']

z = ['Elderly Medicare', 'Uninsured', 'Year', 'Fracking']
# for x1 in xx:
#     for x2 in xx:
#         if x1 != x2:
#             for x3 in xx:
#                 if x3 != x1 and x3 != x2:
#                     for x4 in xx:
#                         if x4 != x1 and x4 != x2 and x4 != x3:
#                             z = [x1, x2, x3, x4]

df = pd.read_csv('/Users/d/Documents/Class/ZNA/df.csv')
y = df.pop('Cancer Rate')
X = df
X = X[z]
X /= np.sqrt(np.sum(X ** 2, axis=0))

model_bic = LassoLarsIC(criterion='bic')
t1 = time.time()
model_bic.fit(X, y)
t_bic = time.time() - t1
alpha_bic_ = model_bic.alpha_

model_aic = LassoLarsIC(criterion='aic')
model_aic.fit(X, y)
alpha_aic_ = model_aic.alpha_

plot_ic_criterion(model_aic, 'AIC', 'b')
plot_ic_criterion(model_bic, 'BIC', 'r')
