"""
Patent Architecture & Workflow Figures — REBIRTH System
Accurately matches the MSPP Algorithm from IDF-B Patent Document.

Architecture: 3-Stage MSPP + Stage 4 Post-Processing (LSA + CSM)
  Stage 1: Emotion Signal Processor (ESP) — BERT classification
  Stage 2: Response Strategy Controller (RSC) + Constraint Generator
  Stage 3: Constrained Output Generator (COG) — SRB + LLM generation
  Stage 4: State Update — Store, LSA update, CSM evaluate

Reference Numerals (from patent):
  100: Mobile Client Tier
  200: Backend Server Tier
  210: Multi-Stage Processing Pipeline (MSPP)
  300: External Services Tier
  400: User Input Stage
  410: Stage 1 - ESP
  430: Stage 2 - RSC
  440: Stage 3 - SRB
  450: Response Generation
  460: Output Stage
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import numpy as np
import os

OUT_DIR = os.path.dirname(os.path.abspath(__file__))

# ── Color Palette (Light Theme) ──
BG        = '#ffffff'
BG_CARD   = '#f5f5f5'
TEXT      = '#1a1a2e'
TEXT_DIM  = '#555555'
GREEN     = '#2e7d32'
RED       = '#c62828'
YELLOW    = '#e65100'
BLUE      = '#1565c0'
PURPLE    = '#7b1fa2'
CYAN      = '#00838f'
ORANGE    = '#e65100'
PINK      = '#ad1457'
TEAL      = '#00695c'
BORDER    = '#cccccc'
BG_TIER   = '#f0f4f8'


# ═══════════════════════════════════════════════════════════════
# FIGURE: System Architecture (Matching Patent Algorithm)
# ═══════════════════════════════════════════════════════════════

def fig_system_architecture():
    fig, ax = plt.subplots(figsize=(20, 16), facecolor=BG)
    ax.set_facecolor(BG)
    ax.set_xlim(0, 20)
    ax.set_ylim(0, 16)
    ax.axis('off')

    # ── Title ──
    ax.text(10, 15.5, 'REBIRTH — System Architecture',
            ha='center', fontsize=24, fontweight='bold', color=TEXT)
    ax.text(10, 15.1, 'Multi-Stage Emotion-Aware Response Regulation System (Patent IDF-B)',
            ha='center', fontsize=12, color=TEXT_DIM)

    # ═══════════════════════════════════════
    # TIER [100]: Mobile Client (Presentation)
    # ═══════════════════════════════════════
    tier1_bg = FancyBboxPatch((0.5, 12.7), 19, 2.0,
                               boxstyle="round,pad=0.15",
                               facecolor=BG_TIER, edgecolor=BLUE,
                               linewidth=2.5, alpha=0.8)
    ax.add_patch(tier1_bg)
    ax.text(1.3, 14.35, '[100] Mobile Client Tier',
            fontsize=13, fontweight='bold', color=BLUE)
    ax.text(1.3, 14.0, 'Flutter Cross-Platform Application (iOS + Android)',
            fontsize=9, color=TEXT_DIM)

    client_items = [
        ('Onboarding\nModule', 'User profiling\n& goals', BLUE),
        ('Chat Interface', 'Real-time\nconversation', BLUE),
        ('Analytics\nDashboard', 'LSA output\nvisualization', BLUE),
        ('Settings', 'Constraint\nconfig', BLUE),
        ('API Service\nLayer', 'REST + JWT\nauthentication', CYAN),
    ]
    for i, (name, desc, color) in enumerate(client_items):
        x = 2.0 + i * 3.5
        box = FancyBboxPatch((x - 1.3, 12.9), 2.7, 1.2,
                             boxstyle="round,pad=0.08",
                             facecolor=BG_CARD, edgecolor=color,
                             linewidth=1.5, alpha=0.9)
        ax.add_patch(box)
        ax.text(x + 0.05, 13.8, name, ha='center', va='center',
                fontsize=8, fontweight='bold', color=color, linespacing=1.2)
        ax.text(x + 0.05, 13.15, desc, ha='center', va='center',
                fontsize=6.5, color=TEXT_DIM, linespacing=1.2)

    # ── Arrow: Tier 100 ↔ Tier 200 ──
    ax.annotate('', xy=(10.5, 12.0), xytext=(10.5, 12.7),
                arrowprops=dict(arrowstyle='->', color=GREEN, lw=2.5))
    ax.text(11.5, 12.25, 'REST API (HTTPS / JSON)', fontsize=8,
            color=GREEN, fontstyle='italic')
    ax.annotate('', xy=(9, 12.7), xytext=(9, 12.0),
                arrowprops=dict(arrowstyle='->', color=ORANGE, lw=2.5))
    ax.text(6.5, 12.25, 'Response + EmotionMetadata', fontsize=8,
            color=ORANGE, fontstyle='italic')

    # ═══════════════════════════════════════
    # TIER [200]: Backend Server (Application)
    # ═══════════════════════════════════════
    tier2_bg = FancyBboxPatch((0.5, 3.5), 19, 8.3,
                               boxstyle="round,pad=0.15",
                               facecolor=BG_TIER, edgecolor=GREEN,
                               linewidth=2.5, alpha=0.8)
    ax.add_patch(tier2_bg)
    ax.text(1.3, 11.45, '[200] Backend Server Tier',
            fontsize=13, fontweight='bold', color=GREEN)
    ax.text(1.3, 11.1, 'Node.js + Express (Vercel Serverless)',
            fontsize=9, color=TEXT_DIM)

    # ── Security / Middleware Row ──
    middleware = ['JWT Auth', 'Rate Limiter', 'CORS / Helmet', 'Input Validation']
    for i, name in enumerate(middleware):
        x = 2.5 + i * 3.8
        box = FancyBboxPatch((x - 1.0, 10.4), 2.2, 0.5,
                             boxstyle="round,pad=0.05",
                             facecolor=BG_CARD, edgecolor=YELLOW,
                             linewidth=1, alpha=0.7)
        ax.add_patch(box)
        ax.text(x + 0.1, 10.65, name, ha='center', va='center',
                fontsize=7.5, color=YELLOW)
    ax.text(17.5, 10.65, 'Security Layer [720]', ha='center', va='center',
            fontsize=8, color=YELLOW, fontweight='bold')

    # ══════════════════════════════════════════════════
    # [210] MSPP — Multi-Stage Processing Pipeline
    # ══════════════════════════════════════════════════
    mspp_bg = FancyBboxPatch((1.0, 6.8), 18, 3.2,
                              boxstyle="round,pad=0.12",
                              facecolor='#eee8f5', edgecolor=PURPLE,
                              linewidth=3, linestyle='--', alpha=0.9)
    ax.add_patch(mspp_bg)
    ax.text(10, 9.7, '[210] MULTI-STAGE PROCESSING PIPELINE (MSPP) — NOVEL',
            ha='center', fontsize=11, fontweight='bold', color=PURPLE)

    # ── Stage 1 [410]: ESP ──
    s1_box = FancyBboxPatch((1.7, 7.0), 4.5, 2.4,
                             boxstyle="round,pad=0.1",
                             facecolor=BG_CARD, edgecolor=GREEN,
                             linewidth=2, alpha=0.95)
    ax.add_patch(s1_box)
    badge1 = FancyBboxPatch((3.2, 8.9), 1.5, 0.35,
                             boxstyle="round,pad=0.04",
                             facecolor=GREEN, edgecolor=GREEN, alpha=0.9)
    ax.add_patch(badge1)
    ax.text(3.95, 9.07, 'STAGE 1', ha='center', fontsize=7.5,
            fontweight='bold', color='#ffffff')
    ax.text(3.95, 8.45, 'Emotion Signal\nProcessor (ESP)', ha='center',
            fontsize=9.5, fontweight='bold', color=GREEN, linespacing=1.2)
    ax.text(3.95, 7.6, '[410] BERT classification\n→ signalLabel, confidence\n→ severity, category\n→ EmotionMetadata object',
            ha='center', fontsize=7, color=TEXT_DIM, linespacing=1.3)

    # ── Stage 2 [430]: RSC ──
    s2_box = FancyBboxPatch((7.0, 7.0), 4.5, 2.4,
                             boxstyle="round,pad=0.1",
                             facecolor=BG_CARD, edgecolor=BLUE,
                             linewidth=2, alpha=0.95)
    ax.add_patch(s2_box)
    badge2 = FancyBboxPatch((8.5, 8.9), 1.5, 0.35,
                             boxstyle="round,pad=0.04",
                             facecolor=BLUE, edgecolor=BLUE, alpha=0.9)
    ax.add_patch(badge2)
    ax.text(9.25, 9.07, 'STAGE 2', ha='center', fontsize=7.5,
            fontweight='bold', color='#ffffff')
    ax.text(9.25, 8.45, 'Response Strategy\nController (RSC)', ha='center',
            fontsize=9.5, fontweight='bold', color=BLUE, linespacing=1.2)
    ax.text(9.25, 7.6, '[430] Deterministic mapping\n→ StrategyParameters\n→ ConstraintSpec\n→ Severity-based modification',
            ha='center', fontsize=7, color=TEXT_DIM, linespacing=1.3)

    # ── Stage 3 [440+450]: SRB + COG ──
    s3_box = FancyBboxPatch((12.3, 7.0), 6.0, 2.4,
                             boxstyle="round,pad=0.1",
                             facecolor=BG_CARD, edgecolor=ORANGE,
                             linewidth=2, alpha=0.95)
    ax.add_patch(s3_box)
    badge3 = FancyBboxPatch((14.5, 8.9), 1.5, 0.35,
                             boxstyle="round,pad=0.04",
                             facecolor=ORANGE, edgecolor=ORANGE, alpha=0.9)
    ax.add_patch(badge3)
    ax.text(15.25, 9.07, 'STAGE 3', ha='center', fontsize=7.5,
            fontweight='bold', color='#ffffff')
    ax.text(15.3, 8.45, 'Constrained Output Generator', ha='center',
            fontsize=9.5, fontweight='bold', color=ORANGE)
    ax.text(13.8, 7.55, '[440] SRB:\nRole + Context\n+ Strategy\n+ Constraints\n+ Safety Rules',
            ha='center', fontsize=6.5, color=TEXT_DIM, linespacing=1.2)
    ax.text(16.8, 7.55, '[450] COG:\nLLM generation\nwithin constraint\nbounds\n→ Response R',
            ha='center', fontsize=6.5, color=TEXT_DIM, linespacing=1.2)
    # Sub-divider
    ax.plot([15.3, 15.3], [7.15, 8.65], color=BORDER, lw=1, alpha=0.5, linestyle=':')

    # ── Pipeline Arrows ──
    ax.annotate('', xy=(6.95, 8.2), xytext=(6.25, 8.2),
                arrowprops=dict(arrowstyle='->', color=GREEN, lw=2.5))
    ax.text(6.6, 8.55, 'E', ha='center', fontsize=8, fontweight='bold', color=GREEN)

    ax.annotate('', xy=(12.25, 8.2), xytext=(11.55, 8.2),
                arrowprops=dict(arrowstyle='->', color=BLUE, lw=2.5))
    ax.text(11.9, 8.55, 'E,S,C', ha='center', fontsize=7, fontweight='bold', color=BLUE)

    # ── EMPP Line ──
    ax.plot([1.5, 18.5], [6.75, 6.75], color=CYAN, lw=2,
            alpha=0.6, linestyle='--')
    ax.text(10, 6.5, 'Emotion Metadata Propagation Protocol (EMPP) — E propagates through ALL stages',
            ha='center', fontsize=8, color=CYAN, fontstyle='italic')

    # ══════════════════════════════════════════════════
    # Stage 4: State Update (Post-Processing)
    # ══════════════════════════════════════════════════
    ax.text(10, 6.15, 'Stage 4: State Update (Post-Processing)', ha='center',
            fontsize=10, fontweight='bold', color=TEXT_DIM)

    # ── LSA (Longitudinal State Accumulator) ──
    lsa_box = FancyBboxPatch((1.5, 4.0), 7.5, 1.8,
                              boxstyle="round,pad=0.1",
                              facecolor=BG_CARD, edgecolor=CYAN,
                              linewidth=2, alpha=0.95)
    ax.add_patch(lsa_box)
    ax.text(5.25, 5.45, 'Longitudinal State Accumulator (LSA)', ha='center',
            fontsize=10, fontweight='bold', color=CYAN)
    ax.text(5.25, 4.6, 'Emotion distribution | Positivity ratio | Stability score\n'
            'Trajectory (IMPROVING/STABLE/DECLINING) | Warning flags',
            ha='center', fontsize=7.5, color=TEXT_DIM, linespacing=1.3)
    ax.text(5.25, 4.2, 'NOVEL', ha='center', fontsize=8,
            fontweight='bold', color=YELLOW)

    # ── CSM (Crisis State Machine) ──
    csm_box = FancyBboxPatch((10.5, 4.0), 8.5, 1.8,
                              boxstyle="round,pad=0.1",
                              facecolor=BG_CARD, edgecolor=RED,
                              linewidth=2, alpha=0.95)
    ax.add_patch(csm_box)
    ax.text(14.75, 5.45, 'Crisis State Machine (CSM)', ha='center',
            fontsize=10, fontweight='bold', color=RED)
    ax.text(14.75, 4.7, 'States: NORMAL → ELEVATED → HIGH_ALERT → CRITICAL',
            ha='center', fontsize=8, color=TEXT_DIM)
    ax.text(14.75, 4.3, 'Inputs: EmotionMetadata + AccumulatedState + LinguisticSignals',
            ha='center', fontsize=7, color=TEXT_DIM)
    ax.text(14.75, 4.05, 'NOVEL', ha='center', fontsize=8,
            fontweight='bold', color=YELLOW)

    # ── Arrows: MSPP → State Update ──
    ax.annotate('', xy=(5.25, 5.8), xytext=(5.25, 6.5),
                arrowprops=dict(arrowstyle='->', color=CYAN, lw=1.8, alpha=0.7))
    ax.text(4, 6.17, 'E → store\n→ accumulate', fontsize=6.5, color=CYAN)

    ax.annotate('', xy=(14.75, 5.8), xytext=(14.75, 6.5),
                arrowprops=dict(arrowstyle='->', color=RED, lw=1.8, alpha=0.7))
    ax.text(15.5, 6.17, 'E, A, L\n→ evaluate', fontsize=6.5, color=RED)

    # ── LSA → RSC feedback ──
    ax.annotate('', xy=(9.25, 6.95), xytext=(9.0, 5.8),
                arrowprops=dict(arrowstyle='->', color=CYAN, lw=1.5,
                                alpha=0.5, connectionstyle='arc3,rad=-0.3',
                                linestyle='dashed'))
    ax.text(10.3, 5.95, 'Warning flags\nfeed back to\nStage 2 (RSC)',
            fontsize=6, color=CYAN, fontstyle='italic', linespacing=1.1)

    # ═══════════════════════════════════════
    # TIER [300]: External Services
    # ═══════════════════════════════════════
    tier3_bg = FancyBboxPatch((0.5, 0.5), 19, 3.2,
                               boxstyle="round,pad=0.15",
                               facecolor=BG_TIER, edgecolor=ORANGE,
                               linewidth=2.5, alpha=0.8)
    ax.add_patch(tier3_bg)
    ax.text(1.3, 3.35, '[300] External Services Tier',
            fontsize=13, fontweight='bold', color=ORANGE)

    services = [
        ('HuggingFace\nInference API', 'BERT emotion\nclassification\n(6 classes)', GREEN, 3.0),
        ('Google Gemini\nLLM API', 'Constrained text\ngeneration', PURPLE, 7.5),
        ('MongoDB Atlas', 'Users, sessions,\nmessages,\nEmotionMetadata', BLUE, 12.0),
        ('Vercel Cloud', 'Serverless\ndeployment\ninfrastructure', TEXT_DIM, 16.5),
    ]

    for name, desc, color, x in services:
        box = FancyBboxPatch((x - 1.5, 0.7), 3.0, 2.3,
                             boxstyle="round,pad=0.08",
                             facecolor=BG_CARD, edgecolor=color,
                             linewidth=1.5, alpha=0.9)
        ax.add_patch(box)
        ax.text(x, 2.5, name, ha='center', va='center',
                fontsize=9, fontweight='bold', color=color, linespacing=1.2)
        ax.text(x, 1.5, desc, ha='center', va='center',
                fontsize=7, color=TEXT_DIM, linespacing=1.2)

    # ── Arrows: Tier 200 → Tier 300 ──
    ax.annotate('', xy=(3.0, 3.0), xytext=(3.95, 4.0),
                arrowprops=dict(arrowstyle='->', color=GREEN, lw=1.5, alpha=0.5))
    ax.annotate('', xy=(7.5, 3.0), xytext=(15.3, 7.0),
                arrowprops=dict(arrowstyle='->', color=PURPLE, lw=1.5, alpha=0.5,
                                connectionstyle='arc3,rad=0.2'))
    ax.annotate('', xy=(12.0, 3.0), xytext=(10, 4.0),
                arrowprops=dict(arrowstyle='->', color=BLUE, lw=1.5, alpha=0.5,
                                connectionstyle='arc3,rad=-0.1'))

    out = os.path.join(OUT_DIR, 'FIG_system_architecture.png')
    plt.savefig(out, dpi=200, bbox_inches='tight', facecolor=BG, pad_inches=0.4)
    plt.close()
    print(f'✅ {out}')


# ═══════════════════════════════════════════════════════════════
# FIGURE: End-to-End Workflow (Matching MSPP Algorithm)
# ═══════════════════════════════════════════════════════════════

def fig_workflow_diagram():
    fig, ax = plt.subplots(figsize=(20, 20), facecolor=BG)
    ax.set_facecolor(BG)
    ax.set_xlim(0, 20)
    ax.set_ylim(0, 20)
    ax.axis('off')

    # ── Title ──
    ax.text(10, 19.5, 'REBIRTH — MSPP Message Processing Workflow',
            ha='center', fontsize=22, fontweight='bold', color=TEXT)
    ax.text(10, 19.1, 'Algorithm: MSPP(M, U, H) → (R, E) | Matching Patent IDF-B Pseudocode',
            ha='center', fontsize=11, color=TEXT_DIM)

    # ── Swim Lanes ──
    lanes = [
        ('Client\nDevice', 2.5, BLUE),
        ('Mobile App\n(Flutter)', 5.5, CYAN),
        ('API Server\n(Node.js)', 9.0, GREEN),
        ('HuggingFace\n(BERT)', 12.5, '#3fb950'),
        ('Google\nGemini', 15.0, PURPLE),
        ('MongoDB\nAtlas', 17.5, BLUE),
    ]

    for name, x, color in lanes:
        box = FancyBboxPatch((x - 0.9, 18.0), 1.8, 0.8,
                             boxstyle="round,pad=0.08",
                             facecolor=color, edgecolor=color,
                             linewidth=0, alpha=0.25)
        ax.add_patch(box)
        ax.text(x, 18.4, name, ha='center', va='center',
                fontsize=8.5, fontweight='bold', color=color, linespacing=1.2)
        ax.plot([x, x], [0.8, 18.0], color=color, lw=0.7, alpha=0.2)

    lane_x = {i: lanes[i][1] for i in range(len(lanes))}

    # ── WORKFLOW STEPS (matching MSPP algorithm exactly) ──
    steps = [
        # (y, type, from, to, label, detail, color, step, algo_ref)
        (17.2, 'arrow', 0, 1, 'User types message', 'M = user message text', TEXT, '1', ''),
        (16.4, 'arrow', 1, 2, 'Send POST /api/chat', 'JWT token + M + U + H', CYAN, '2', ''),
        (15.6, 'self',  2, 2, 'Auth + Input Validation', 'JWT verify, sanitize, rate limit', YELLOW, '3', ''),

        # Stage 1: ESP
        (14.6, 'label', 2, 2, 'STAGE 1: EMOTION SIGNAL PROCESSING', '', GREEN, '', '[410]'),
        (13.8, 'arrow', 2, 3, 'CLASSIFY_EMOTION(M)', 'Step 1.1: External service call', GREEN, '4', ''),
        (13.0, 'self',  3, 3, 'BERT 6-class classification', 'P = probability distribution', GREEN, '5', '1.1'),
        (12.2, 'arrow', 3, 2, 'Return probabilities P', 'signalLabel = argmax(P), confidence = max(P)', GREEN, '6', '1.2-1.3'),
        (11.4, 'self',  2, 2, 'Build EmotionMetadata E', 'severity = COMPUTE_SEVERITY(confidence)\n'
                                                          'category = CLASSIFY_CATEGORY(signalLabel)', GREEN, '7', '1.4-1.6'),

        # Stage 2: RSC
        (10.2, 'label', 2, 2, 'STAGE 2: RESPONSE STRATEGY CONTROL', '', BLUE, '', '[430]'),
        (9.4,  'self',  2, 2, 'RSC_ALGORITHM(E)', 'STRATEGY_MAP[signalLabel] → baseStrategy\n'
                                                    'Severity-based modification', BLUE, '8', '2.1'),
        (8.6,  'self',  2, 2, 'CONSTRAINT_GENERATOR(E, S)', 'C.required, C.prohibited\n'
                                                              'C.safetyEnforcement, C.escalation', BLUE, '9', '2.2'),

        # Stage 3: COG
        (7.4,  'label', 2, 2, 'STAGE 3: CONSTRAINED OUTPUT GENERATION', '', ORANGE, '', '[440+450]'),
        (6.6,  'self',  2, 2, 'SRB: BUILD_STRUCTURED_REQUEST', 'Role + Context + Strategy\n'
                                                                 '+ Constraints + Safety Rules', PURPLE, '10', '3.1'),
        (5.8,  'arrow', 2, 4, 'GENERATE_CONSTRAINED(request)', 'Step 3.2: Structured prompt → LLM', ORANGE, '11', '3.2'),
        (5.0,  'self',  4, 4, 'LLM generation within constraints', 'Response within bounds', ORANGE, '12', ''),
        (4.2,  'arrow', 4, 2, 'Return constrained response R', 'Constraint-compliant response', ORANGE, '13', ''),

        # Stage 4: State Update
        (3.0,  'label', 2, 2, 'STAGE 4: STATE UPDATE', '', CYAN, '', '[460]'),
        (2.4,  'arrow', 2, 5, 'STORE_INTERACTION(M, R, E)', 'Step 4.1: Persist all data', BLUE, '14', '4.1'),
        (1.8,  'self',  2, 2, 'UPDATE_ACCUMULATED_STATE(U.id, E)', 'LSA: distribution, positivity, stability, trajectory', CYAN, '15', '4.2'),
        (1.2,  'self',  2, 2, 'EVALUATE_CRISIS_STATE(E, A)', 'CSM: riskScore → state transition', RED, '16', '4.3'),
        (0.5,  'arrow', 2, 1, 'RETURN (R, E)', 'Response + EmotionMetadata → client', GREEN, '17', ''),
    ]

    for y, typ, fi, ti, label, detail, color, step_num, algo_ref in steps:
        fx = lane_x[fi]
        tx = lane_x[ti]

        if typ == 'label':
            # Section label
            label_box = FancyBboxPatch((fx - 3.0, y - 0.25), 6.0, 0.5,
                                       boxstyle="round,pad=0.08",
                                       facecolor=color, edgecolor=color,
                                       linewidth=0, alpha=0.15)
            ax.add_patch(label_box)
            ax.text(fx, y, label, ha='center', va='center',
                    fontsize=9, fontweight='bold', color=color)
            if algo_ref:
                ax.text(fx + 3.3, y, algo_ref, ha='left', va='center',
                        fontsize=7, color=TEXT_DIM)
            continue

        if typ == 'self':
            # Self-processing box
            box = FancyBboxPatch((fx - 1.5, y - 0.3), 3.0, 0.65,
                                 boxstyle="round,pad=0.06",
                                 facecolor=BG_CARD, edgecolor=color,
                                 linewidth=1.5, alpha=0.9)
            ax.add_patch(box)
            ax.text(fx, y + 0.08, label, ha='center', va='center',
                    fontsize=7.5, fontweight='bold', color=color)
            if detail:
                lines = detail.split('\n')
                for li, line in enumerate(lines):
                    ax.text(fx, y - 0.15 - li * 0.13, line, ha='center',
                            va='center', fontsize=5.5, color=TEXT_DIM)
        else:
            # Arrow between lanes
            offset = 0.5 if tx > fx else -0.5
            ax.annotate('', xy=(tx - offset, y),
                        xytext=(fx + offset, y),
                        arrowprops=dict(arrowstyle='->', color=color,
                                        lw=1.8, alpha=0.7))
            mid_x = (fx + tx) / 2
            ax.text(mid_x, y + 0.22, label, ha='center', fontsize=7,
                    fontweight='bold', color=color)
            if detail:
                lines = detail.split('\n')
                for li, line in enumerate(lines):
                    ax.text(mid_x, y - 0.12 - li * 0.12, line, ha='center',
                            fontsize=5.5, color=TEXT_DIM)

        # Step number
        if step_num:
            badge = plt.Circle((0.7, y), 0.2, facecolor=color,
                               edgecolor=color, alpha=0.25, linewidth=0)
            ax.add_patch(badge)
            ax.text(0.7, y, step_num, ha='center', va='center',
                    fontsize=7, fontweight='bold', color=color)

        # Algorithm reference
        if algo_ref and typ != 'label':
            ax.text(19.3, y, algo_ref, ha='center', va='center',
                    fontsize=6.5, color=TEXT_DIM,
                    bbox=dict(boxstyle='round,pad=0.12', facecolor=BG_CARD,
                              edgecolor=BORDER, alpha=0.8))

    # ── Timeline arrow ──
    ax.annotate('', xy=(0.7, 0.3), xytext=(0.7, 17.7),
                arrowprops=dict(arrowstyle='->', color=TEXT_DIM, lw=1.2, alpha=0.3))

    # ── Novel badges ──
    novel_items = [
        (13.0, 'ESP', GREEN),
        (9.4,  'RSC', BLUE),
        (8.6,  'Constraints', BLUE),
        (6.6,  'SRB + EMPP', PURPLE),
        (1.8,  'LSA', CYAN),
        (1.2,  'CSM', RED),
    ]
    for y, label, color in novel_items:
        ax.text(19.3, y, f'NOVEL', ha='center', fontsize=6,
                fontweight='bold', color=YELLOW,
                bbox=dict(boxstyle='round,pad=0.1', facecolor=YELLOW,
                          edgecolor=YELLOW, alpha=0.15))

    out = os.path.join(OUT_DIR, 'FIG_workflow_diagram.png')
    plt.savefig(out, dpi=200, bbox_inches='tight', facecolor=BG, pad_inches=0.4)
    plt.close()
    print(f'✅ {out}')


# ═══════════════════════════════════════════════════════════════
if __name__ == '__main__':
    print('\n🔧 Generating corrected architecture & workflow figures...\n')
    fig_system_architecture()
    fig_workflow_diagram()
    print('\n✅ Both figures generated — now match patent algorithm!\n')
