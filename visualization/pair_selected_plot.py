import sys
import os

current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_path, '../'))

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from sklearn import linear_model
import itertools


def better_regplot(x, y, **kwargs):
    ax = sns.regplot(x, y, **kwargs)
    margin = (max(y) - min(y)) * 0.1
    plt.ylim(min(y) - margin, max(y) + margin)
    R2 = round(stats.pearsonr(x, y)[0] ** 2, 3)
    plt.text(0.4, 0.9, '$R^2$ = ' + str(R2), ha='center',
             va='center', transform=ax.transAxes)


df = pd.read_csv('../out/plotting_data_for_analysis.csv')

df = df.sort_values(by=['k_pnm'])
df.index = df.k_pnm
df['error_rel'] = (df.k_edm - df.k_pnm) / df.k_pnm

data = pd.DataFrame(df[['k_pnm', 'porosity', 'radius_pore_avg', 'radius_throat_avg',
                        'length_throat_avg', 'connection_n_avg', 'error_rel']])
correlation_param = 'err'
params = ['k', 'p', 'r_p', 'r_th', 'l_th', 'c_n']
columns = params.copy()
columns.append(correlation_param)
data.columns = columns

complex_params = []
for param in params:
    complex_params.append([param])

for L in range(1, 3):
    for subset in itertools.combinations(params, L):
        complex_params.append(list(subset))

print('complex_params', complex_params)

score_threshold = 0.54
print('score_threshold', score_threshold)

reg = linear_model.LinearRegression()
y = data[correlation_param]
complex_params_n = len(complex_params)
count = 0
count_selected = 0
data_selected = pd.DataFrame(data[correlation_param])
for complex_param in complex_params:
    X = data[complex_param]
    reg.fit(X, y)
    complex_param_name = complex_param[0]
    for param in complex_param[1:]:
        complex_param_name += '__' + param
    score = reg.score(X, y)
    if score > score_threshold:
        data_selected[complex_param_name] = np.dot(X, reg.coef_) + reg.intercept_
        count_selected += 1
    count += 1
    print('complex_param: ', count, 'from ', complex_params_n, 'score', round(score, 3))
print('regression analysis finished')
print('count_selected', count_selected)

sns.set()
g = sns.pairplot(data_selected, kind='reg', diag_kind='kde')
g = g.map_offdiag(better_regplot)
plt.savefig('../out/pair_selected_1_2_plot.pdf', format="pdf",
            bbox_inches='tight')
