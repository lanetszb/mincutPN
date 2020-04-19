import sys
import os

current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_path, '../'))

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def better_regplot(x, y, **kwargs):
    sns.regplot(x, y, **kwargs)
    margin = (max(y) - min(y)) * 0.1
    plt.ylim(min(y) - margin, max(y) + margin)


table = pd.read_csv('../out/plotting_data_for_analysis.csv')
df = pd.DataFrame(table)

df = df.sort_values(by=['k_pnm'])
df.index = df.k_pnm
df['error_rel'] = (df.k_edm - df.k_pnm) / df.k_pnm

sns.set()
g = sns.pairplot(df, kind='reg', diag_kind='kde')
g = g.map_offdiag(better_regplot)
plt.savefig('../out/seaborn_pairplot.eps', format="eps", bbox_inches='tight')
