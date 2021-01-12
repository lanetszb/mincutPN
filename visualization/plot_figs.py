import sys
import os

current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_path, '../'))

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from scipy import stats

from matplotlib import rc

rc('text', usetex=True)

fig_width = 3.5

table = pd.read_csv('../out/plotting_data_for_analysis.csv')
df = pd.DataFrame(table)

df = df.sort_values(by=['k_pnm'])
df.index = df.k_pnm
df['error_rel'] = (df.k_edm - df.k_pnm) / df.k_pnm


def implement_filter(table, threshold, remove_rate):
    remove_n = int(len(table.index[table.index < threshold]) * remove_rate)
    drop_indices = np.random.choice(table.index[table.index < threshold], remove_n,
                                    replace=False)

    return table.drop(drop_indices)


# df = implement_filter(df, 1.e-10, 0.6)

# Plot 1
fig1, ax1 = plt.subplots(figsize=(fig_width, fig_width), tight_layout=True)
ax1 = df.plot(x='k_pnm', y='k_edm', style='o', label='artificial', legend=False, zorder=1,
              ax=ax1, alpha=0.3)

k_min = 5.e-14
k_max = 5.e-10

ax1.set_xlim(k_min, k_max)
ax1.set_ylim(k_min, k_max)

ax1.set_xlabel('$K_{pnm}, m^2$')
ax1.set_ylabel('$K_{edm}, m^2$')

plt.gca().set_aspect('equal', adjustable='box')
plt.plot([k_min, k_max], [k_min, k_max], label='diagonal', zorder=2, alpha=0.7)

plt.scatter(1.067776E-11, 1.013048E-11, c="r", marker='s', label='(a)', zorder=3, s=50)
plt.scatter(2.298116E-13, 1.889883E-13, c="cyan", marker='s', label='(b)', zorder=3, s=50)
plt.scatter(4.194141E-10, 3.555365E-10, c="y", marker='s', label='(c)', zorder=3, s=50)
plt.scatter(3.622896E-12, 1.487646E-12, c="m", marker='s', label='(d)', zorder=3, s=50)

plt.legend(fancybox=True, framealpha=1)

plt.yscale("log")
plt.xscale("log")

plt.savefig('../out/k_pnm_edm.pdf', format="pdf", bbox_inches='tight')

plt.show()

# Plot 2

fig2, ax2 = plt.subplots(figsize=(fig_width, fig_width), tight_layout=True)
df.plot(x='k_pnm', y='error_rel', style='o', label='artificial', legend=False, ax=ax2,
        zorder=1, alpha=0.3)

mean_err = df.error_rel.mean()
plt.plot([k_min, k_max], [mean_err, mean_err], label='average')

ax2.set_xlim(k_min, k_max)
ax2.set_ylim(-1, 1)

ax2.set_xlabel('$K_{pnm}, m^2$')
ax2.set_ylabel('Relative error')

plt.scatter(1.067776E-11, (1.013048E-11 - 1.067776E-11) / 1.067776E-11, c="r", marker='s',
            label='(a)', zorder=2, s=50)
plt.scatter(2.298116E-13, (1.889883E-13 - 2.298116E-13) / 2.298116E-13, c="cyan",
            marker='s', label='(b)', zorder=2, s=50)
plt.scatter(4.194141E-10, (3.555365E-10 - 4.194141E-10) / 4.194141E-10, c="y", marker='s',
            label='(c)', zorder=2, s=50)
plt.scatter(3.622896E-12, (1.487646E-12 - 3.622896E-12) / 3.622896E-12, c="m", marker='s',
            label='(d)', zorder=2, s=50)

plt.legend(loc=2, ncol=2)

plt.xscale("log")

plt.savefig('../out/error_rel.pdf', format="pdf", bbox_inches='tight')

plt.show()

# Plot 3

fig3, ax3 = plt.subplots(figsize=(fig_width, fig_width), tight_layout=True)
sns.regplot(x='connection_n_avg', y='error_rel', data=df, ax=ax3,
            line_kws={"color": "#ff7f0e"})
R2 = round(stats.pearsonr(df['connection_n_avg'], df['error_rel'])[0] ** 2, 3)
plt.ylim(-0.84, 0.32)
plt.text(0.75, 0.25, '$R^2$ = ' + str(R2), ha='center', va='center',
         transform=ax3.transAxes)
xlim = ax3.get_xlim()
plt.plot(xlim, [0, 0], color='black', linewidth=0.5, zorder=0)
plt.xlim(xlim)
ax3.set_xlabel('Coordination number')
ax3.set_ylabel('Relative error')
plt.savefig('../out/error_rel_vs_connection_n_avg.pdf', format="pdf", bbox_inches='tight')
plt.show()
