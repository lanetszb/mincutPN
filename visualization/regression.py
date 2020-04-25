import sys
import os

current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_path, '../'))

import pandas as pd
from sklearn import linear_model

table = pd.read_csv('../out/plotting_data_for_analysis.csv')
df = pd.DataFrame(table)

df = df.sort_values(by=['k_pnm'])
df.index = df.k_pnm
df['error_rel'] = (df.k_edm - df.k_pnm) / df.k_pnm

# X = df[['radius_throat_std', 'connection_n_avg']]
X = df.drop(columns=['error_rel'])
y = df['error_rel']

regression = linear_model.LinearRegression()
regression.fit(X, y)

print('coef', regression.coef_)
print('intercept', regression.intercept_)
print('score', regression.score(X, y))
