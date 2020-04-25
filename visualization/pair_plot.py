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

regression = linear_model.LinearRegression()
y = df['error_rel']

# linea reg of radius_throat_std anf connection_n_avg to error
X = df[['radius_throat_std', 'connection_n_avg']]
regression.fit(X, y)
df['conns_radii_thr_reg_err'] = np.dot(X, regression.coef_) + regression.intercept_

# linea reg of all to error
X = df.drop(columns=['error_rel'])
regression.fit(X, y)
df['all_reg_err'] = np.dot(X, regression.coef_) + regression.intercept_

sns.set()
g = sns.pairplot(df, kind='reg', diag_kind='kde')
g = g.map_offdiag(better_regplot)
plt.savefig('../out/seaborn_pairplot.pdf', format="pdf", bbox_inches='tight')
