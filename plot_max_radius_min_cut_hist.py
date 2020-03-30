import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rc

rc('text', usetex=True)

bead_pack = np.loadtxt('out/bead_pack_512_min_cut_radii.txt') * 1.e+6
bead_pack_max_radius = np.loadtxt('out/bead_pack_512_max_radius.txt') * 1.e+6

castle = np.loadtxt('out/castle_512_min_cut_radii.txt') * 1.e+6
castle_max_radius = np.loadtxt('out/castle_512_max_radius.txt') * 1.e+6

gambier = np.loadtxt('out/gambier_512_min_cut_radii.txt') * 1.e+6
gambier_max_radius = np.loadtxt('out/gambier_512_max_radius.txt') * 1.e+6

lrc32 = np.loadtxt('out/lrc32_512_min_cut_radii.txt') * 1.e+6
lrc32_max_radius = np.loadtxt('out/lrc32_512_max_radius.txt') * 1.e+6

fig_width = 3.5
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2,
                                             figsize=(fig_width, fig_width),
                                             tight_layout=True)

ax1.hist(bead_pack, bins=20)
x1 = np.array([bead_pack_max_radius, bead_pack_max_radius])
y1 = np.array(ax1.get_ylim())
ax1.plot(x1, y1, lw=4, label='critical radius')
ax1.set_title('(a)')
ax1.set_ylim(y1 * 1)

ax2.hist(castle, bins=10)
x2 = np.array([castle_max_radius, castle_max_radius])
y2 = np.array(ax2.get_ylim()) * 2.2
ax2.plot(x2, y2 * 0.48, lw=4)
ax2.set_title('(b)')
ax2.set_ylim(y2 * 0.45)

ax3.hist(lrc32, bins=15)
x3 = np.array([lrc32_max_radius, lrc32_max_radius])
y3 = np.array(ax3.get_ylim())
ax3.plot(x3, y3, lw=4)
ax3.set_title('(c)')
ax3.set_ylim(y3 * 1)

ax4.hist(gambier, bins=20)
x4 = np.array([gambier_max_radius, gambier_max_radius])
y4 = np.array(ax4.get_ylim())
ax4.plot(x4, y4, lw=4)
ax4.set_title('(d)')
ax4.set_ylim(y4 * 1)

fig.text(0.005, 0.5, 'throats (edges) number', va='center', rotation='vertical')
fig.text(0.5, 0.005, 'throats (edges) radius, ' + r'$\mu$' + 'm', ha='center')

handles, labels = ax1.get_legend_handles_labels()
fig.legend(handles, labels, loc=(0.365, 0.47))

plt.savefig('out/max_radius_min_cut_hist.eps', format='eps', bbox_inches='tight')

plt.show()
