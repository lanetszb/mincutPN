import matplotlib.pyplot as plt
import numpy as np

bead_pack = np.loadtxt('out/bead_pack_512_min_cut_radii.txt')
bead_pack_max_radius = np.loadtxt('out/bead_pack_512_max_radius.txt')

castle = np.loadtxt('out/castle_512_min_cut_radii.txt')
castle_max_radius = np.loadtxt('out/castle_512_max_radius.txt')

gambier = np.loadtxt('out/gambier_512_min_cut_radii.txt')
gambier_max_radius = np.loadtxt('out/gambier_512_max_radius.txt')

lrc32 = np.loadtxt('out/lrc32_512_min_cut_radii.txt')
lrc32_max_radius = np.loadtxt('out/lrc32_512_max_radius.txt')

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2, tight_layout=True)

ax1.hist(bead_pack, bins=20)
x = np.array([bead_pack_max_radius, bead_pack_max_radius])
y = np.array([ax1.get_ylim()[0], ax1.get_ylim()[1]])
ax1.plot(x, y, lw=4)
ax1.ticklabel_format(style='sci', axis='x', scilimits=(0, 0), useMathText=True)
# plt.ylim(y * 1.1)

ax2.hist(gambier, bins=20)
x = np.array([gambier_max_radius, gambier_max_radius])
y = np.array([ax2.get_ylim()[0], ax2.get_ylim()[1]])
ax2.plot(x, y, lw=4)
ax2.ticklabel_format(style='sci', axis='x', scilimits=(0, 0), useMathText=True)
plt.ylim(y * 1.1)

ax3.hist(lrc32, bins=15)
x = np.array([lrc32_max_radius, lrc32_max_radius])
y = np.array([ax3.get_ylim()[0], ax3.get_ylim()[1]])
ax3.plot(x, y, lw=4)
ax3.ticklabel_format(style='sci', axis='x', scilimits=(0, 0), useMathText=True)
plt.ylim(y * 1.1)

ax4.hist(castle, bins=10)
x = np.array([castle_max_radius, castle_max_radius])
y = np.array([ax4.get_ylim()[0], ax4.get_ylim()[1]])
ax4.plot(x, y * 0.48, lw=4)
ax4.ticklabel_format(style='sci', axis='x', scilimits=(0, 0), useMathText=True)
plt.ylim(y * 0.5)

plt.show()
