"""
Patent Novelty Figures Generator — REBIRTH System
Generates publication-ready figures for patent filing.
Uses patent-safe terminology (no medical/therapeutic language).
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np
import os

OUT_DIR = os.path.dirname(os.path.abspath(__file__))

# ── Color Palette (Light Theme) ──
BG       = '#ffffff'
BG_CARD  = '#f5f5f5'
BG_LIGHT = '#eeeeee'
TEXT     = '#1a1a2e'
TEXT_DIM = '#555555'
GREEN    = '#2e7d32'
RED      = '#c62828'
YELLOW   = '#e65100'
BLUE     = '#1565c0'
PURPLE   = '#7b1fa2'
CYAN     = '#00838f'
ORANGE   = '#e65100'
PINK     = '#ad1457'
BORDER   = '#cccccc'

# ═══════════════════════════════════════════════════════════════
# FIGURE 1: Claims-to-Features Mapping
# ═══════════════════════════════════════════════════════════════

def fig1_claims_features():
    fig, ax = plt.subplots(figsize=(16, 10), facecolor=BG)
    ax.set_facecolor(BG)
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(8, 9.5, 'REBIRTH — Claims-to-Features Mapping',
            ha='center', fontsize=20, fontweight='bold', color=TEXT)
    ax.text(8, 9.1, 'How Patent Claim Sets Protect Novel System Features',
            ha='center', fontsize=11, color=TEXT_DIM)

    # ── Claim Sets (Top Row) ──
    claims = [
        ('Set 1', 'Multi-Stage\nResponse Regulation', 'C1.1–C1.4', GREEN),
        ('Set 2', 'Longitudinal State\nAccumulation', 'C2.1–C2.3', BLUE),
        ('Set 3', 'Crisis State\nMachine', 'C3.1–C3.3', PURPLE),
        ('Set 4', 'Metadata\nPropagation', 'C4.1', CYAN),
        ('Set 5', 'Constraint\nInjection', 'C5.1', ORANGE),
    ]

    claim_positions = []
    claim_xs = [1.6, 4.8, 8.0, 11.2, 14.4]
    for i, (label, desc, refs, color) in enumerate(claims):
        x = claim_xs[i]
        box = FancyBboxPatch((x - 1.2, 7.0), 2.4, 1.6,
                             boxstyle="round,pad=0.12", linewidth=2,
                             edgecolor=color, facecolor=BG_CARD)
        ax.add_patch(box)
        ax.text(x, 8.15, label, ha='center', va='center',
                fontsize=11, fontweight='bold', color=color)
        ax.text(x, 7.6, desc, ha='center', va='center',
                fontsize=8, color=TEXT, linespacing=1.3)
        ax.text(x, 7.2, f'({refs})', ha='center', va='center',
                fontsize=7, color=TEXT_DIM)
        claim_positions.append((x, 7.0))

    # ── Novel Features (Bottom Row) ──
    features = [
        ('Emotion Signal\nProcessor', GREEN),
        ('Response Strategy\nController', GREEN),
        ('Severity-Based\nConstraint Selector', ORANGE),
        ('Multi-Signal\nSafety Gate', PURPLE),
        ('Constrained Output\nGenerator', CYAN),
        ('System State\nTransition Controller', PURPLE),
        ('Persistent Metadata\nPropagation', CYAN),
        ('Longitudinal State\nAccumulator', BLUE),
    ]

    feat_positions = []
    feat_xs = np.linspace(1.2, 14.8, 8)
    for i, (label, color) in enumerate(features):
        x = feat_xs[i]
        box = FancyBboxPatch((x - 0.85, 3.4), 1.7, 1.4,
                             boxstyle="round,pad=0.1", linewidth=1.5,
                             edgecolor=color, facecolor=BG_CARD)
        ax.add_patch(box)
        ax.text(x, 4.1, label, ha='center', va='center',
                fontsize=7, color=TEXT, linespacing=1.2)
        feat_positions.append((x, 4.8))

    # ── Connections (Claims → Features) ──
    # Set 1 → features 0,1,2,4
    connections = [
        (0, [0, 1, 2, 4], GREEN),
        (1, [7], BLUE),
        (2, [3, 5], PURPLE),
        (3, [6], CYAN),
        (4, [2, 4], ORANGE),
    ]

    for claim_idx, feat_idxs, color in connections:
        cx, cy = claim_positions[claim_idx]
        for fi in feat_idxs:
            fx, fy = feat_positions[fi]
            ax.annotate('', xy=(fx, fy), xytext=(cx, cy),
                        arrowprops=dict(arrowstyle='->', color=color,
                                        lw=1.5, alpha=0.6,
                                        connectionstyle='arc3,rad=0.05'))

    # Labels
    ax.text(8, 6.5, '── Claim Sets ──', ha='center', fontsize=9,
            color=TEXT_DIM, fontstyle='italic')
    ax.text(8, 5.2, '── Novel Features ──', ha='center', fontsize=9,
            color=TEXT_DIM, fontstyle='italic')

    # Legend
    legend_items = [
        ('Multi-Stage Regulation', GREEN),
        ('Longitudinal Accumulation', BLUE),
        ('Crisis State Machine', PURPLE),
        ('Metadata Propagation', CYAN),
        ('Constraint Injection', ORANGE),
    ]
    for i, (label, color) in enumerate(legend_items):
        ax.plot(1.5 + i * 3, 2.5, 's', color=color, markersize=8)
        ax.text(1.85 + i * 3, 2.5, label, va='center',
                fontsize=7.5, color=TEXT_DIM)

    out = os.path.join(OUT_DIR, 'FIG_claims_features.png')
    plt.savefig(out, dpi=200, bbox_inches='tight', facecolor=BG, pad_inches=0.4)
    plt.close()
    print(f'✅ {out}')


# ═══════════════════════════════════════════════════════════════
# FIGURE 2: Features vs Prior Art Gap Matrix
# ═══════════════════════════════════════════════════════════════

def fig2_prior_art_gap():
    fig, ax = plt.subplots(figsize=(16, 9), facecolor=BG)
    ax.set_facecolor(BG)
    ax.axis('off')

    ax.text(0.5, 0.96, 'REBIRTH — Novel Features vs Prior Art Gap Analysis',
            ha='center', va='center', transform=ax.transAxes,
            fontsize=20, fontweight='bold', color=TEXT)
    ax.text(0.5, 0.93, 'Demonstrates absence of disclosed features in existing prior art',
            ha='center', va='center', transform=ax.transAxes,
            fontsize=11, color=TEXT_DIM)

    # Features (columns)
    features = [
        'Emotion Signal\nProcessor',
        'Response Strategy\nController',
        'Constraint\nEnforcement',
        'Severity-Based\nModification',
        'Crisis State\nMachine',
        'Longitudinal\nAccumulation',
        'Metadata\nPropagation',
        'Multi-Signal\nSafety Gate',
    ]

    # Prior art (rows)
    prior_art = [
        'Woebot (2017)\nRule-Based CBT',
        'Wysa (2015)\nDecision Trees',
        'Youper (2018)\nBasic Sentiment',
        'Replika (2017)\nSeq2Seq Models',
        'Pi / Inflection (2023)\nCustom LLM',
        'ChatGPT Bots (2023)\nGeneric LLM',
        'REBIRTH (2026)\nHybrid BERT-LLM',
    ]

    # Coverage matrix: 0 = Missing, 1 = Partial, 2 = Full
    # rows = prior art, cols = features
    matrix = np.array([
        [0, 0, 0, 0, 0, 0, 0, 0],  # Woebot
        [0, 0, 0, 0, 0, 0, 0, 0],  # Wysa
        [1, 0, 0, 0, 0, 0, 0, 0],  # Youper (partial sentiment)
        [0, 0, 0, 0, 0, 0, 0, 0],  # Replika
        [0, 1, 0, 0, 0, 0, 0, 0],  # Pi (partial strategy)
        [0, 1, 0, 0, 0, 1, 0, 0],  # ChatGPT (partial strategy, partial logging)
        [2, 2, 2, 2, 2, 2, 2, 2],  # REBIRTH
    ])

    nrows, ncols = matrix.shape
    cell_w, cell_h = 1.4, 0.8
    start_x, start_y = 3.5, 1.0

    # Draw cells
    colors_map = {0: RED, 1: YELLOW, 2: GREEN}
    symbols = {0: '✗', 1: '~', 2: '✓'}

    for r in range(nrows):
        for c in range(ncols):
            x = start_x + c * cell_w
            y = start_y + (nrows - 1 - r) * cell_h
            val = matrix[r][c]
            fcolor = colors_map[val]
            alpha = 0.25 if r < nrows - 1 else 0.5

            rect = FancyBboxPatch((x, y), cell_w - 0.08, cell_h - 0.08,
                                   boxstyle="round,pad=0.04",
                                   facecolor=fcolor, alpha=alpha,
                                    edgecolor=fcolor if r == nrows - 1 else BORDER,
                                   linewidth=2 if r == nrows - 1 else 0.8)
            ax.add_patch(rect)

            sym_color = TEXT if r == nrows - 1 else TEXT_DIM
            ax.text(x + (cell_w - 0.08) / 2, y + (cell_h - 0.08) / 2,
                    symbols[val], ha='center', va='center',
                    fontsize=14 if r == nrows - 1 else 11,
                    fontweight='bold', color=sym_color)

    # Row labels (prior art)
    for r in range(nrows):
        y = start_y + (nrows - 1 - r) * cell_h + (cell_h - 0.08) / 2
        color = GREEN if r == nrows - 1 else TEXT_DIM
        weight = 'bold' if r == nrows - 1 else 'normal'
        ax.text(start_x - 0.2, y, prior_art[r], ha='right', va='center',
                fontsize=7.5, color=color, fontweight=weight, linespacing=1.2)

    # Column labels (features)
    for c in range(ncols):
        x = start_x + c * cell_w + (cell_w - 0.08) / 2
        y = start_y + nrows * cell_h + 0.05
        ax.text(x, y, features[c], ha='center', va='bottom',
                fontsize=7, color=TEXT, rotation=0, linespacing=1.2)

    # Legend
    legend_data = [('✗ Missing', RED), ('~ Partial', YELLOW), ('✓ Full', GREEN)]
    for i, (label, color) in enumerate(legend_data):
        lx = start_x + ncols * cell_w + 0.5
        ly = start_y + (nrows - 1) * cell_h - i * 0.5
        rect = FancyBboxPatch((lx, ly), 0.35, 0.3,
                               boxstyle="round,pad=0.03",
                               facecolor=color, alpha=0.35,
                               edgecolor=color, linewidth=1)
        ax.add_patch(rect)
        ax.text(lx + 0.55, ly + 0.15, label, va='center',
                fontsize=8, color=TEXT_DIM)

    total_w = start_x + ncols * cell_w + 3.5
    total_h = start_y + nrows * cell_h + 2.5
    ax.set_xlim(0, total_w)
    ax.set_ylim(0, total_h)

    out = os.path.join(OUT_DIR, 'FIG_prior_art_gap.png')
    plt.savefig(out, dpi=200, bbox_inches='tight', facecolor=BG, pad_inches=0.4)
    plt.close()
    print(f'✅ {out}')


# ═══════════════════════════════════════════════════════════════
# FIGURE 3: Multi-Stage Processing Pipeline (Novelty Flow)
# ═══════════════════════════════════════════════════════════════

def fig3_pipeline_novelty():
    fig, ax = plt.subplots(figsize=(18, 8), facecolor=BG)
    ax.set_facecolor(BG)
    ax.set_xlim(0, 18)
    ax.set_ylim(0, 8)
    ax.axis('off')

    ax.text(9, 7.5, 'REBIRTH — Multi-Stage Processing Pipeline (MSPP)',
            ha='center', fontsize=20, fontweight='bold', color=TEXT)
    ax.text(9, 7.1, 'Novel Architecture: Mandatory Emotion Metadata Propagation Across All Stages',
            ha='center', fontsize=11, color=TEXT_DIM)

    # ── Pipeline Stages ──
    stages = [
        ('STAGE 1', 'Emotion Signal\nProcessor (ESP)', 'BERT-based\nclassification\n→ 6 emotions\n→ confidence\n→ severity', GREEN),
        ('STAGE 2', 'Response Strategy\nController (RSC)', 'Deterministic\nmapping logic\n→ approach\n→ constraints\n→ escalation', BLUE),
        ('STAGE 3', 'Structured Request\nBuilder (SRB)', 'Constraint\ninjection\n→ role definition\n→ safety rules\n→ prohibited list', PURPLE),
        ('STAGE 4', 'Constrained Output\nGenerator', 'LLM generation\nwith enforced\nconstraints\n→ compliant\nresponse', ORANGE),
    ]

    stage_xs = [2.0, 6.5, 11.0, 15.5]
    box_w, box_h = 3.0, 4.0

    for i, (label, title, detail, color) in enumerate(stages):
        x = stage_xs[i]
        # Main box
        box = FancyBboxPatch((x - box_w/2, 2.0), box_w, box_h,
                             boxstyle="round,pad=0.15", linewidth=2.5,
                             edgecolor=color, facecolor=BG_CARD)
        ax.add_patch(box)

        # Stage label
        label_box = FancyBboxPatch((x - 0.6, 5.5), 1.2, 0.4,
                                    boxstyle="round,pad=0.06",
                                    facecolor=color, edgecolor=color,
                                    linewidth=0, alpha=0.9)
        ax.add_patch(label_box)
        ax.text(x, 5.7, label, ha='center', va='center',
                fontsize=8, fontweight='bold', color='#ffffff')

        # Title
        ax.text(x, 5.1, title, ha='center', va='center',
                fontsize=10, fontweight='bold', color=color, linespacing=1.3)

        # Details
        ax.text(x, 3.5, detail, ha='center', va='center',
                fontsize=8, color=TEXT_DIM, linespacing=1.4)

        # NOVEL badge
        ax.text(x, 2.3, '★ NOVEL', ha='center', va='center',
                fontsize=8, fontweight='bold', color=YELLOW)

    # ── Arrows between stages ──
    for i in range(len(stage_xs) - 1):
        x1 = stage_xs[i] + box_w / 2 + 0.1
        x2 = stage_xs[i + 1] - box_w / 2 - 0.1
        mid = (x1 + x2) / 2
        ax.annotate('', xy=(x2, 4.0), xytext=(x1, 4.0),
                    arrowprops=dict(arrowstyle='->', color=GREEN,
                                    lw=2.5, alpha=0.8))

    # ── Metadata propagation line ──
    ax.plot([stage_xs[0], stage_xs[-1]], [1.5, 1.5],
            color=CYAN, lw=2, alpha=0.6, linestyle='--')
    ax.text(9, 1.2, '◆ Emotion Metadata Object propagates through ALL stages (EMPP)',
            ha='center', fontsize=9, color=CYAN, fontstyle='italic')

    # Input / Output labels
    ax.text(0.3, 4.0, 'User\nInput', ha='center', va='center',
            fontsize=10, color=TEXT_DIM, fontweight='bold')
    ax.annotate('', xy=(stage_xs[0] - box_w/2 - 0.1, 4.0),
                xytext=(0.8, 4.0),
                arrowprops=dict(arrowstyle='->', color=TEXT_DIM, lw=1.5))

    ax.text(17.7, 4.0, 'Emotion-\nAware\nResponse', ha='center', va='center',
            fontsize=10, color=GREEN, fontweight='bold')
    ax.annotate('', xy=(17.2, 4.0),
                xytext=(stage_xs[-1] + box_w/2 + 0.1, 4.0),
                arrowprops=dict(arrowstyle='->', color=GREEN, lw=1.5))

    out = os.path.join(OUT_DIR, 'FIG_pipeline_novelty.png')
    plt.savefig(out, dpi=200, bbox_inches='tight', facecolor=BG, pad_inches=0.4)
    plt.close()
    print(f'✅ {out}')


# ═══════════════════════════════════════════════════════════════
# FIGURE 4: Crisis State Machine Diagram
# ═══════════════════════════════════════════════════════════════

def fig4_crisis_state_machine():
    fig, ax = plt.subplots(figsize=(14, 8), facecolor=BG)
    ax.set_facecolor(BG)
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 8)
    ax.axis('off')

    ax.text(7, 7.5, 'REBIRTH — Crisis State Machine (CSM)',
            ha='center', fontsize=20, fontweight='bold', color=TEXT)
    ax.text(7, 7.1, 'Finite State Machine with Multi-Signal Risk Scoring',
            ha='center', fontsize=11, color=TEXT_DIM)

    # ── States ──
    states = [
        ('NORMAL', 'Risk < 20', 'Standard\nprocessing', GREEN, 2.5, 4.5),
        ('ELEVATED', '20 ≤ Risk < 40', 'Enhanced\nvalidation', YELLOW, 5.5, 4.5),
        ('HIGH\nALERT', '40 ≤ Risk < 60', 'Safety priority\n+ support', ORANGE, 8.5, 4.5),
        ('CRITICAL', 'Risk ≥ 60', 'Crisis mode\n+ resources', RED, 11.5, 4.5),
    ]

    for name, threshold, action, color, x, y in states:
        circle = plt.Circle((x, y), 1.1, facecolor=BG_CARD,
                            edgecolor=color, linewidth=3, alpha=0.9)
        ax.add_patch(circle)
        ax.text(x, y + 0.35, name, ha='center', va='center',
                fontsize=11, fontweight='bold', color=color)
        ax.text(x, y - 0.2, threshold, ha='center', va='center',
                fontsize=7.5, color=TEXT_DIM)
        ax.text(x, y - 0.6, action, ha='center', va='center',
                fontsize=7, color=TEXT_DIM, linespacing=1.2)

    # ── Transition Arrows ──
    transitions = [
        (2.5, 5.5, 'arrowstyle=->,lw=2', GREEN, 'Risk ↑'),
        (5.5, 8.5, 'arrowstyle=->,lw=2', YELLOW, 'Risk ↑'),
        (8.5, 11.5, 'arrowstyle=->,lw=2', ORANGE, 'Risk ↑'),
    ]

    for x1, x2, style, color, label in transitions:
        ax.annotate('', xy=(x2 - 1.15, 5.3), xytext=(x1 + 1.15, 5.3),
                    arrowprops=dict(arrowstyle='->', color=color,
                                    lw=2, alpha=0.7))
        ax.text((x1 + x2) / 2, 5.6, label, ha='center', fontsize=7, color=color)

    # Back arrows (recovery)
    for x1, x2 in [(11.5, 8.5), (8.5, 5.5), (5.5, 2.5)]:
        ax.annotate('', xy=(x2 + 1.15, 3.7), xytext=(x1 - 1.15, 3.7),
                    arrowprops=dict(arrowstyle='->', color=TEXT_DIM,
                                    lw=1.2, alpha=0.4, linestyle='dashed'))

    ax.text(7, 3.2, '← Recovery (Risk score decreases) ←',
            ha='center', fontsize=8, color=TEXT_DIM, fontstyle='italic')

    # ── Risk Signal Sources ──
    ax.text(7, 2.2, 'Risk Score = Σ Signal Weights',
            ha='center', fontsize=11, fontweight='bold', color=TEXT)

    signals = [
        ('Emotion Severity Signal', '+25', GREEN),
        ('Linguistic Crisis Pattern', '+35', RED),
        ('Longitudinal Warning', '+20', BLUE),
        ('Trajectory Decline', '+15', PURPLE),
        ('Session Negativity', '+10', ORANGE),
    ]

    for i, (label, weight, color) in enumerate(signals):
        x = 1.5 + i * 2.6
        ax.text(x, 1.6, label, ha='center', fontsize=7.5, color=TEXT_DIM)
        ax.text(x, 1.2, weight, ha='center', fontsize=10,
                fontweight='bold', color=color)

    out = os.path.join(OUT_DIR, 'FIG_crisis_state_machine.png')
    plt.savefig(out, dpi=200, bbox_inches='tight', facecolor=BG, pad_inches=0.4)
    plt.close()
    print(f'✅ {out}')


# ═══════════════════════════════════════════════════════════════
# FIGURE 5: Comparative Performance Bar Chart
# ═══════════════════════════════════════════════════════════════

def fig5_performance_comparison():
    fig, axes = plt.subplots(1, 2, figsize=(16, 6), facecolor=BG)

    # ── Left: Response Quality Metrics ──
    ax1 = axes[0]
    ax1.set_facecolor(BG_CARD)

    metrics = ['Emotional\nAppropriateness', 'Constraint\nCompliance',
               'Empathy Score\n(scaled)', 'User\nSatisfaction']
    baseline = [62, 45, 64, 58]
    rebirth  = [94, 97.3, 92, 89]

    x = np.arange(len(metrics))
    w = 0.35

    bars1 = ax1.bar(x - w/2, baseline, w, color=RED, alpha=0.7, label='Baseline LLM')
    bars2 = ax1.bar(x + w/2, rebirth, w, color=GREEN, alpha=0.8, label='REBIRTH System')

    ax1.set_ylabel('Score (%)', color=TEXT, fontsize=10)
    ax1.set_title('Response Quality Metrics', color=TEXT,
                  fontsize=13, fontweight='bold', pad=12)
    ax1.set_xticks(x)
    ax1.set_xticklabels(metrics, fontsize=8, color=TEXT_DIM)
    ax1.set_ylim(0, 110)
    ax1.tick_params(axis='y', colors=TEXT_DIM)
    ax1.spines['bottom'].set_color(BORDER)
    ax1.spines['left'].set_color(BORDER)
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)

    # Value labels
    for bar in bars1:
        ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1.5,
                 f'{bar.get_height():.0f}%', ha='center', fontsize=7.5, color=RED)
    for bar in bars2:
        ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1.5,
                 f'{bar.get_height():.1f}%', ha='center', fontsize=7.5, color=GREEN)

    ax1.legend(facecolor=BG_CARD, edgecolor=BORDER, labelcolor=TEXT,
               fontsize=9, loc='upper left')

    # ── Right: System Latency Performance ──
    ax2 = axes[1]
    ax2.set_facecolor(BG_CARD)

    components = ['Stage 1:\nEmotion Signal\nProcessing',
                  'Stage 2:\nStrategy\nController',
                  'Stage 3:\nConstrained\nGeneration',
                  'Total\nPipeline']
    latency   = [200, 5, 1000, 1500]
    req_limit = [500, 50, 2000, 3000]
    colors = [GREEN, GREEN, GREEN, BLUE]

    x2 = np.arange(len(components))
    bars = ax2.bar(x2, latency, 0.5, color=colors, alpha=0.8)

    # Requirement threshold line
    for i, rl in enumerate(req_limit):
        ax2.plot([i - 0.3, i + 0.3], [rl, rl], '--', color=RED, alpha=0.5, lw=1.5)

    ax2.set_ylabel('Latency (ms)', color=TEXT, fontsize=10)
    ax2.set_title('System Latency Performance', color=TEXT,
                  fontsize=13, fontweight='bold', pad=12)
    ax2.set_xticks(x2)
    ax2.set_xticklabels(components, fontsize=7.5, color=TEXT_DIM)
    ax2.tick_params(axis='y', colors=TEXT_DIM)
    ax2.spines['bottom'].set_color(BORDER)
    ax2.spines['left'].set_color(BORDER)
    ax2.spines['top'].set_visible(False)
    ax2.spines['right'].set_visible(False)

    for bar in bars:
        ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 40,
                 f'{bar.get_height():.0f}ms', ha='center', fontsize=8, color=TEXT)

    # Dashed line legend
    ax2.plot([], [], '--', color=RED, alpha=0.5, lw=1.5, label='Requirement Limit')
    ax2.legend(facecolor=BG_CARD, edgecolor=BORDER, labelcolor=TEXT, fontsize=9)

    plt.tight_layout(pad=2)
    out = os.path.join(OUT_DIR, 'FIG_performance_comparison.png')
    plt.savefig(out, dpi=200, bbox_inches='tight', facecolor=BG, pad_inches=0.4)
    plt.close()
    print(f'✅ {out}')


# ═══════════════════════════════════════════════════════════════
# MAIN — Generate All Figures
# ═══════════════════════════════════════════════════════════════

if __name__ == '__main__':
    print('\n🔧 Generating patent novelty figures...\n')
    fig1_claims_features()
    fig2_prior_art_gap()
    fig3_pipeline_novelty()
    fig4_crisis_state_machine()
    fig5_performance_comparison()
    print('\n✅ All 5 patent figures generated successfully!')
    print(f'📁 Output directory: {OUT_DIR}\n')
