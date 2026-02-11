import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from matplotlib.colors import ListedColormap

plt.rcParams.update({
    'figure.facecolor': '#ffffff',
    'axes.facecolor': '#ffffff',
    'text.color': '#1a1a2e',
    'font.family': 'sans-serif',
    'font.size': 12,
})

# ── Data ──
features = ['Multi-Stage\nDecoupling', 'Metadata\nPropagation',
            'Constraint\nEnforcement', 'Severity\nControl',
            'Longitudinal\nAccumulation', 'Crisis State\nMachine']

rebirth = [10, 10, 9, 9, 9, 10]
prior   = [2,  1,  2, 3, 3,  1]

prior_names = ['US 11,087,895 (2021)', 'US 2022/0343983 (2022)',
               'WO 2023/056789 (2023)', 'US 10,902,943 (2020)',
               'CN 116579467 (2023)',   'EP 4012624 (2022)']

cols = ['Stage\nDecoupling', 'Metadata\nPropagation', 'Constraint\nEnforcement',
        'Severity\nControl', 'Longitudinal\nAccumulation', 'Crisis\nFSM']

matrix = np.array([
    [0,0,0,0,0,0], [0,0,0,1,0,0], [0,0,0,0,1,0],
    [0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,1,0,0,0],
    [2,2,2,2,2,2],
])
rows = prior_names + ['REBIRTH (2026)']

fig = plt.figure(figsize=(14, 18))

# ══════════════════════════════════════
#  RADAR CHART — top half
# ══════════════════════════════════════
ax1 = fig.add_axes([0.1, 0.52, 0.8, 0.42], polar=True)

N = 6
angles = np.linspace(0, 2*np.pi, N, endpoint=False).tolist()
angles += angles[:1]

ax1.fill(angles, rebirth+rebirth[:1], color='#2e7d32', alpha=0.15)
ax1.plot(angles, rebirth+rebirth[:1], color='#2e7d32', lw=2.8,
         marker='o', ms=10, mfc='#2e7d32', mec='white', mew=2,
         label='REBIRTH (Ours)', zorder=5)

ax1.fill(angles, prior+prior[:1], color='#c62828', alpha=0.08)
ax1.plot(angles, prior+prior[:1], color='#c62828', lw=2,
         marker='D', ms=7, mfc='#c62828', mec='white', mew=1.5,
         label='Best Prior Art', zorder=4)

ax1.set_xticks(angles[:-1])
ax1.set_xticklabels(features, fontsize=12, fontweight='bold', color='#333333')
ax1.set_yticks([2, 4, 6, 8, 10])
ax1.set_yticklabels([])  # remove inner number clutter
ax1.set_ylim(0, 12)
ax1.spines['polar'].set_color('#cccccc')
ax1.grid(color='#dddddd', lw=0.6)

ax1.legend(loc='upper center', bbox_to_anchor=(0.5, -0.08),
           ncol=2, fontsize=12, framealpha=0.9,
           edgecolor='#cccccc', facecolor='#ffffff',
           labelcolor='#1a1a2e', handletextpad=0.5, columnspacing=2)

ax1.set_title('Novelty Radar — REBIRTH vs Prior Art',
              fontsize=16, fontweight='bold', color='#1a1a2e', pad=28)

# ══════════════════════════════════════
#  HEATMAP — bottom half
# ══════════════════════════════════════
ax2 = fig.add_axes([0.12, 0.04, 0.82, 0.4])

cmap = ListedColormap(['#ef5350', '#ffa726', '#66bb6a'])
ax2.imshow(matrix, cmap=cmap, aspect=0.7, vmin=0, vmax=2)

ax2.set_xticks(range(6))
ax2.set_xticklabels(cols, fontsize=10, fontweight='bold', color='#333333', ha='center')
ax2.set_yticks(range(7))
ax2.set_yticklabels(rows, fontsize=11, fontweight='bold', color='#333333')
ax2.tick_params(length=0, pad=12)
ax2.xaxis.set_ticks_position('bottom')

syms = {0: '✗', 1: '~', 2: '✓'}
tcol = {0: '#ffffff', 1: '#333333', 2: '#ffffff'}
for i in range(7):
    for j in range(6):
        v = matrix[i, j]
        ax2.text(j, i, syms[v], ha='center', va='center',
                 fontsize=20, fontweight='bold', color=tcol[v])

# REBIRTH row highlight
rect = mpatches.FancyBboxPatch((-0.5, 5.55), 6, 0.9, lw=3,
    edgecolor='#2e7d32', facecolor='none',
    boxstyle='round,pad=0.02', zorder=5, clip_on=False)
ax2.add_patch(rect)

# Grid
for i in range(8):
    ax2.axhline(y=i-0.5, color='#ffffff', lw=2.5)
for j in range(7):
    ax2.axvline(x=j-0.5, color='#ffffff', lw=2.5)

ax2.set_title('Prior Art Gap Matrix — Feature Coverage',
              fontsize=16, fontweight='bold', color='#1a1a2e', pad=20)

legend_p = [
    mpatches.Patch(fc='#ef5350', ec='#cccccc', label='✗  Missing'),
    mpatches.Patch(fc='#ffa726', ec='#cccccc', label='~  Partial'),
    mpatches.Patch(fc='#66bb6a', ec='#cccccc', label='✓  Full'),
]
ax2.legend(handles=legend_p, loc='upper right', fontsize=10,
           framealpha=0.9, edgecolor='#cccccc', facecolor='#ffffff',
           labelcolor='#1a1a2e')

# ── Title ──


import os
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'novelty_graph.png')
plt.savefig(out, dpi=200, bbox_inches='tight', facecolor='#ffffff', pad_inches=0.5)
plt.close()
print(f"✅ {out}")
