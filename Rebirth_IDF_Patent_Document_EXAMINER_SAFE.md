# ©VIT IPR&TT CELL

## Invention Disclosure Format (IDF)-B

| Document No. | Issue No/Date | Amd. No/Date |
|--------------|---------------|--------------|
| 02-IPR-R004  | 1/07.02.2026  | 1/08.02.2026 |

**Inventor(s):** Oshim Pathan  
**Affiliation:** VIT Chennai  
**Filing Date:** February 7, 2026  
**Amendment Date:** February 8, 2026

---

## 1. Title of the Invention

**MULTI-STAGE EMOTION-AWARE RESPONSE REGULATION SYSTEM WITH SEVERITY-BASED STATE CONTROL AND LONGITUDINAL BEHAVIOR MODIFICATION FOR CONVERSATIONAL INTERFACES**

---

## 2. Field/Area of Invention

This invention relates to the field of **computer-implemented conversational systems** with **emotion-aware response regulation**, **multi-stage processing architectures**, **state-based control systems**, and **runtime behavior modification based on accumulated user interaction patterns**. Specifically, the invention addresses the technical problem of constraining and regulating automated response generation in conversational interfaces based on detected emotional signals, severity classification, and longitudinal state accumulation.

The invention is applicable to any conversational computing system requiring:
- Emotion-signal-conditioned output regulation
- Multi-stage processing with metadata propagation
- Severity-aware response constraint enforcement
- Longitudinal state accumulation affecting runtime behavior
- Crisis-triggered system state transitions

---

## 3. Prior Art and Technical Limitations

### Patent Literature:

| Year | Patent ID | Title | Technical Limitations |
|------|-----------|-------|----------------------|
| 2021 | US 11,087,895 B2 | Machine Learning Conversational Agent | 1. Rule-based architecture without multi-stage emotion signal processing.<br>2. No metadata propagation between processing stages.<br>3. No severity-aware response constraint mechanism.<br>4. No longitudinal state accumulation affecting runtime behavior. |
| 2022 | US 2022/0343983 A1 | Emotion Recognition System | 1. Single-stage emotion detection without downstream integration.<br>2. Emotion data not propagated to response generation.<br>3. No constraint enforcement layer.<br>4. No state-based crisis handling. |
| 2023 | WO 2023/056789 A1 | AI Assessment Platform | 1. Static assessment without real-time signal processing.<br>2. Single-model approach without stage decoupling.<br>3. No emotion-conditioned output regulation.<br>4. No longitudinal behavior modification. |
| 2020 | US 10,902,943 B2 | Conversational Agent System | 1. Scripted response trees without emotion signal input.<br>2. No preprocessing stage for emotional classification.<br>3. No constraint injection into generation stage.<br>4. No crisis state detection or escalation. |
| 2023 | CN 116579467 A | Dialogue System | 1. Basic polarity classification (positive/negative/neutral) only.<br>2. No multi-class emotion signal processing.<br>3. No response strategy selection module.<br>4. No structured constraint propagation. |
| 2022 | EP 4012624 A1 | Digital Intervention System | 1. Static content delivery without adaptive response.<br>2. No real-time emotion signal processing.<br>3. No severity-based behavior modification.<br>4. No crisis state transition mechanism. |

### Technical Problem Statement:

Existing conversational systems suffer from the following technical deficiencies:

1. **Lack of Stage Decoupling:** Prior art conflates emotion detection and response generation into monolithic systems, preventing independent optimization and constraint enforcement at each stage.

2. **No Metadata Propagation:** Detected emotional signals are not systematically propagated through all processing stages, resulting in response generation that is unaware of emotional context.

3. **Absence of Constraint Enforcement:** Response generation operates without structured constraints derived from emotional signals, leading to contextually inappropriate outputs.

4. **No Severity-Based Control:** Systems lack graduated response regulation based on severity classification of detected emotional states.

5. **Stateless Operation:** Each interaction is processed independently without longitudinal state accumulation, preventing pattern-based behavior modification.

6. **No Crisis State Handling:** Systems lack defined state transitions for handling high-severity situations requiring escalated responses.

---

## 4. Summary of the Invention

### Technical Solution:

This invention provides a **computer-implemented multi-stage response regulation system** that decouples emotion signal processing, response strategy selection, and constrained output generation into distinct stages with mandatory metadata propagation between stages.

### Core Inventive Concept:

A computer-implemented conversational response regulation system comprising:
- A multi-stage processing architecture with decoupled inference and decision stages
- Mandatory emotion metadata propagation through all processing stages
- Severity-aware response constraint enforcement
- Structured output generation constrained by emotion-derived parameters
- Longitudinal emotional state accumulation that modifies runtime behavior
- Crisis escalation implemented as system state transitions

### Key Technical Contributions:

**1. Multi-Stage Processing Architecture (MSPA)**

The invention implements a three-stage processing pipeline where:
- **Stage 1 (Signal Processing):** Receives natural language input and produces structured emotion signal data including classification label, confidence value, and severity indicator
- **Stage 2 (Strategy Selection):** Receives emotion signal data and produces response strategy parameters including approach identifier, constraint set, and escalation flags
- **Stage 3 (Constrained Output):** Receives strategy parameters and produces response output constrained by the emotion-derived parameters

Each stage produces structured output that is mandatory input for the subsequent stage, creating data dependencies that enforce emotion-aware processing throughout.

**2. Emotion Metadata Propagation Protocol (EMPP)**

The invention defines a structured metadata schema that persists through all processing stages:

```
EmotionMetadata {
    signalLabel: String          // Classified emotion signal
    confidence: Float [0,1]      // Classification confidence
    severity: Enum {LOW, MEDIUM, HIGH}
    category: Enum {POSITIVE, NEGATIVE, NEUTRAL}
    timestamp: DateTime
    escalationFlag: Boolean
}
```

This metadata object is attached to every processing request and response, ensuring downstream stages have access to emotion context.

**3. Response Constraint Enforcement Module (RCEM)**

The invention implements a constraint enforcement module that:
- Receives emotion metadata and strategy parameters
- Produces a structured constraint specification
- Injects constraints into the output generation stage
- Validates output compliance with constraints

The constraint specification includes:
- Required response characteristics (tone, approach)
- Prohibited content patterns (avoidance rules)
- Escalation triggers (severity thresholds)
- Safety enforcement rules

**4. Longitudinal State Accumulation Engine (LSAE)**

The invention maintains accumulated emotional state across multiple interactions:

```
AccumulatedState {
    emotionDistribution: Map<SignalLabel, Count>
    positivityRatio: Float
    stabilityScore: Float
    trajectory: Enum {IMPROVING, STABLE, DECLINING}
    warningFlags: List<WarningType>
}
```

This accumulated state modifies runtime behavior:
- Response strategy selection is influenced by historical patterns
- Warning thresholds trigger proactive system responses
- Trajectory analysis enables early intervention

**5. Crisis State Machine (CSM)**

The invention implements a state machine for crisis handling:

```
States: {NORMAL, ELEVATED, HIGH_ALERT, CRITICAL}

Transitions:
    NORMAL → ELEVATED: severity=HIGH OR warningFlag=TRUE
    ELEVATED → HIGH_ALERT: multipleSignals=TRUE
    HIGH_ALERT → CRITICAL: crisisIndicator=TRUE
    Any → NORMAL: stabilityConfirmed=TRUE
```

Each state has associated:
- Response modification rules
- Escalation actions
- Safety enforcement requirements

---

## 5. Objectives of the Invention

The principal objectives are to:

1. **Implement a multi-stage processing architecture** that decouples emotion signal processing from response generation, enabling independent constraint enforcement at each stage.

2. **Enable mandatory emotion metadata propagation** ensuring all downstream processing stages have access to emotional context for informed decision-making.

3. **Provide severity-aware response regulation** that adjusts response characteristics based on the severity classification of detected emotional signals.

4. **Implement constraint enforcement** that structures and limits output generation based on emotion-derived parameters.

5. **Enable longitudinal state accumulation** that tracks emotional patterns across interactions and modifies runtime behavior accordingly.

6. **Implement crisis state handling** through defined state transitions that trigger appropriate escalation responses.

7. **Ensure deterministic control flow** where response generation is governed by explicit rules and constraints rather than unconstrained model output.

---

## 6. Working Principle

### System Architecture Overview:

```
┌─────────────────────────────────────────────────────────────────────┐
│                    CONVERSATIONAL INTERFACE                          │
├─────────────────────────────────────────────────────────────────────┤
│  User Input                                                          │
│      │                                                               │
│      ▼                                                               │
│  ┌─────────────────────────────────────────────────────────────┐    │
│  │ STAGE 1: EMOTION SIGNAL PROCESSOR                           │    │
│  │ Input: Natural language text                                │    │
│  │ Output: EmotionMetadata object                              │    │
│  │ Function: Classification, confidence scoring, severity      │    │
│  └─────────────────────────────────────────────────────────────┘    │
│      │                                                               │
│      │ EmotionMetadata (mandatory propagation)                      │
│      ▼                                                               │
│  ┌─────────────────────────────────────────────────────────────┐    │
│  │ STAGE 2: RESPONSE STRATEGY CONTROLLER                       │    │
│  │ Input: EmotionMetadata                                      │    │
│  │ Output: StrategyParameters + ConstraintSpec                 │    │
│  │ Function: Strategy selection, constraint generation         │    │
│  └─────────────────────────────────────────────────────────────┘    │
│      │                                                               │
│      │ StrategyParameters + ConstraintSpec (mandatory)              │
│      ▼                                                               │
│  ┌─────────────────────────────────────────────────────────────┐    │
│  │ STAGE 3: CONSTRAINED OUTPUT GENERATOR                       │    │
│  │ Input: User message + StrategyParameters + ConstraintSpec   │    │
│  │ Output: Constrained response                                │    │
│  │ Function: Response generation within constraint bounds      │    │
│  └─────────────────────────────────────────────────────────────┘    │
│      │                                                               │
│      ▼                                                               │
│  Response to User + Stored EmotionMetadata                          │
└─────────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────────┐
│              LONGITUDINAL STATE ACCUMULATION ENGINE                  │
├─────────────────────────────────────────────────────────────────────┤
│  • Accumulates emotion signals over time                             │
│  • Computes aggregate metrics (distribution, stability, trajectory)  │
│  • Generates warning flags based on pattern thresholds               │
│  • Feeds back into Stage 2 for strategy modification                 │
└─────────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────────┐
│                      CRISIS STATE MACHINE                            │
├─────────────────────────────────────────────────────────────────────┤
│  Current State: {NORMAL | ELEVATED | HIGH_ALERT | CRITICAL}         │
│  • Monitors severity signals and warning flags                       │
│  • Triggers state transitions based on defined rules                 │
│  • Modifies response constraints based on current state              │
│  • Generates escalation actions when required                        │
└─────────────────────────────────────────────────────────────────────┘
```

### Stage 1: Emotion Signal Processor

**Function:** Converts natural language input into structured emotion signal data.

**Input:** Raw text string from user

**Processing:**
1. Text is submitted to an emotion classification service
2. Service returns probability distribution across emotion categories
3. Primary emotion is selected based on highest probability
4. Severity is computed based on confidence threshold
5. Metadata object is constructed

**Output:**
```
EmotionMetadata {
    signalLabel: "fear"
    confidence: 0.92
    severity: HIGH
    category: NEGATIVE
    timestamp: 2026-02-08T10:30:00Z
    escalationFlag: false
}
```

**Technical Contribution:** This stage produces structured signal data that is mandatory input for downstream stages. The emotion classification itself uses existing machine learning services—the novelty is in the structured output format and mandatory propagation requirement.

### Stage 2: Response Strategy Controller

**Function:** Translates emotion metadata into response strategy parameters and constraint specifications.

**Input:** EmotionMetadata from Stage 1

**Processing:**
1. Emotion signal label is mapped to response approach identifier
2. Severity level triggers constraint intensity selection
3. Contraindication rules are loaded based on emotion category
4. Escalation flags are evaluated
5. Constraint specification is constructed

**Strategy Mapping Logic:**

```
STRATEGY_MAP = {
    "fear": {
        approach: "reassurance_grounding",
        tone: ["calm", "supportive", "validating"],
        techniques: ["validation", "normalization", "grounding"],
        contraindications: ["catastrophizing", "invalidation", "rushing"]
    },
    "sadness": {
        approach: "compassionate_presence",
        tone: ["warm", "empathetic", "patient"],
        techniques: ["validation", "active_listening", "exploration"],
        contraindications: ["toxic_positivity", "minimization"]
    },
    "anger": {
        approach: "de_escalation",
        tone: ["steady", "non_judgmental", "calm"],
        techniques: ["acknowledgment", "reflection", "perspective"],
        contraindications: ["confrontation", "blame", "dismissal"]
    },
    "joy": {
        approach: "positive_reinforcement",
        tone: ["warm", "celebratory", "encouraging"],
        techniques: ["celebration", "reinforcement", "reflection"],
        contraindications: []
    },
    "surprise": {
        approach: "curious_engagement",
        tone: ["interested", "curious", "open"],
        techniques: ["exploration", "curiosity", "context_gathering"],
        contraindications: []
    },
    "love": {
        approach: "connection_affirmation",
        tone: ["warm", "affirming", "supportive"],
        techniques: ["affirmation", "positive_reinforcement"],
        contraindications: []
    }
}
```

**Severity Modification Logic:**

```
IF severity = HIGH AND category = NEGATIVE:
    constraintIntensity = ELEVATED
    escalationCheck = TRUE
    prependTechnique("crisis_assessment")
    appendAction("resource_provision")
ELSE IF severity = MEDIUM:
    constraintIntensity = STANDARD
ELSE:
    constraintIntensity = LIGHT
```

**Output:**
```
StrategyParameters {
    approach: "reassurance_grounding"
    tone: ["calm", "supportive", "validating"]
    techniques: ["validation", "normalization", "grounding"]
    intensity: ELEVATED
    escalationFlag: true
}

ConstraintSpec {
    required: ["validation_first", "calm_tone", "grounding_offer"]
    prohibited: ["catastrophizing", "invalidation", "rushing"]
    escalation: true
    safetyEnforcement: true
}
```

**Technical Contribution:** This stage implements response control logic that transforms emotional signals into actionable constraints. The mapping is implemented as deterministic control logic, not as abstract psychological concepts.

### Stage 3: Constrained Output Generator

**Function:** Generates response output within the bounds specified by ConstraintSpec.

**Input:** 
- Original user message
- StrategyParameters from Stage 2
- ConstraintSpec from Stage 2
- Conversation context

**Processing:**
1. Construct structured generation request incorporating all constraints
2. Include emotional context section
3. Include strategy directive section  
4. Include safety constraint section
5. Submit to text generation service
6. Validate output against ConstraintSpec
7. Return constrained response

**Structured Generation Request:**

```
SECTION 1: ROLE DEFINITION
    "You are a supportive conversational companion. Respond with 
     empathy and support."

SECTION 2: EMOTIONAL CONTEXT
    "Current emotional signal: {signalLabel} ({confidence}%)
     Severity level: {severity}
     Category: {category}"

SECTION 3: STRATEGY DIRECTIVE
    "Use approach: {approach}
     Maintain tone: {tone}
     Apply techniques: {techniques}
     Response intensity: {intensity}"

SECTION 4: CONSTRAINT ENFORCEMENT
    "REQUIRED elements: {ConstraintSpec.required}
     PROHIBITED elements: {ConstraintSpec.prohibited}
     Safety enforcement: {ConstraintSpec.safetyEnforcement}"

SECTION 5: SAFETY RULES
    "1. Never provide professional advice beyond your scope
     2. Validate feelings without minimization
     3. Maintain supportive boundaries
     4. Include resource information if escalation=true"

SECTION 6: USER MESSAGE
    "{originalMessage}"
```

**Technical Contribution:** This stage implements constraint injection into text generation. The generation service is treated as a black box; the novelty is in the structured constraint framework that governs its output.

### Longitudinal State Accumulation Engine

**Function:** Maintains accumulated emotional state across interactions and generates pattern-based warnings.

**Data Model:**
```
AccumulatedState {
    userId: String
    period: {DAY | WEEK | MONTH | ALL}
    emotionDistribution: Map<SignalLabel, Count>
    totalSignals: Integer
    positivityRatio: Float          // (joy + love) / total
    stabilityScore: Float           // 1 - transitionRate
    trajectory: {IMPROVING | STABLE | DECLINING}
    trajectoryDelta: Float
    warningFlags: List<Warning>
    lastUpdated: DateTime
}

Warning {
    type: {PERSISTENT_NEGATIVITY | HIGH_VOLATILITY | 
           TRAJECTORY_DECLINE | CRISIS_PATTERN}
    severity: {LOW | MEDIUM | HIGH | CRITICAL}
    triggeredAt: DateTime
}
```

**Computation Logic:**

```
FUNCTION computeAccumulatedState(userId, period):
    signals = fetchEmotionSignals(userId, period)
    
    // Distribution
    FOR each signal IN signals:
        distribution[signal.label] += 1
    
    // Positivity Ratio
    positiveCount = distribution[joy] + distribution[love]
    positivityRatio = positiveCount / totalSignals
    
    // Stability Score (based on transition frequency)
    transitions = countTransitions(signals)
    transitionRate = transitions / (totalSignals - 1)
    stabilityScore = 1 - transitionRate
    
    // Trajectory (compare to previous period)
    previousPositivity = fetchPreviousPositivity(userId, period)
    trajectoryDelta = positivityRatio - previousPositivity
    IF trajectoryDelta > 0.1:
        trajectory = IMPROVING
    ELSE IF trajectoryDelta < -0.1:
        trajectory = DECLINING
    ELSE:
        trajectory = STABLE
    
    // Warning Generation
    warnings = []
    IF positivityRatio < 0.3 AND totalSignals > 10:
        warnings.add(Warning(PERSISTENT_NEGATIVITY, HIGH))
    IF stabilityScore < 0.3:
        warnings.add(Warning(HIGH_VOLATILITY, MEDIUM))
    IF trajectory = DECLINING AND trajectoryDelta < -0.2:
        warnings.add(Warning(TRAJECTORY_DECLINE, HIGH))
    IF distribution[fear] + distribution[sadness] > 0.7 * totalSignals:
        warnings.add(Warning(CRISIS_PATTERN, CRITICAL))
    
    RETURN AccumulatedState(...)
```

**Runtime Behavior Modification:**

The accumulated state feeds back into Stage 2:
- Warning flags influence strategy selection
- Trajectory affects response intensity
- Pattern detection triggers proactive responses

**Technical Contribution:** This engine transforms passive data collection into active runtime behavior modification. The system's responses are influenced by historical patterns, not just current input.

### Crisis State Machine

**Function:** Manages system states for crisis handling with defined state transitions.

**State Definitions:**

```
State NORMAL:
    description: "Standard operation"
    responseModification: NONE
    escalationActions: NONE

State ELEVATED:
    description: "Heightened attention required"
    responseModification: ENHANCED_VALIDATION
    escalationActions: [flag_session]

State HIGH_ALERT:
    description: "Active crisis indicators present"
    responseModification: SAFETY_PRIORITY
    escalationActions: [flag_session, prepare_resources]

State CRITICAL:
    description: "Immediate crisis intervention needed"
    responseModification: CRISIS_RESPONSE
    escalationActions: [flag_session, provide_resources, 
                        express_concern, encourage_help]
```

**Transition Rules:**

```
FUNCTION evaluateTransition(currentState, emotionMetadata, 
                            accumulatedState, linguisticSignals):
    
    riskScore = 0
    
    // Signal 1: Current emotion severity
    IF emotionMetadata.severity = HIGH AND emotionMetadata.category = NEGATIVE:
        riskScore += 25
    
    // Signal 2: Linguistic crisis indicators
    IF linguisticSignals.crisisKeywordDetected:
        riskScore += 35
    
    // Signal 3: Longitudinal warning
    IF accumulatedState.warningFlags CONTAINS CRISIS_PATTERN:
        riskScore += 20
    
    // Signal 4: Session pattern
    IF sessionNegativeRatio > 0.8:
        riskScore += 10
    
    // Determine new state
    IF riskScore >= 60:
        RETURN CRITICAL
    ELSE IF riskScore >= 40:
        RETURN HIGH_ALERT
    ELSE IF riskScore >= 20:
        RETURN ELEVATED
    ELSE:
        RETURN NORMAL
```

**Technical Contribution:** The crisis state machine implements graduated response handling through defined states and transitions. This is a control system, not a clinical protocol.

---

## 6A. Formal Algorithm Specifications

### Algorithm 1: Multi-Stage Processing Pipeline (MSPP)

**Technical Classification:** Control Flow Architecture

**Formal Specification:**

```
ALGORITHM: Multi-Stage Processing Pipeline (MSPP)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

INPUT: 
    M = User message text (string)
    U = User context object
    H = Conversation history

OUTPUT:
    R = Constrained response
    E = Emotion metadata object

PROCEDURE MSPP(M, U, H):
    
    ┌─────────────────────────────────────────────────────────┐
    │ STAGE 1: EMOTION SIGNAL PROCESSING                      │
    └─────────────────────────────────────────────────────────┘
    
    1.1  P ← CLASSIFY_EMOTION(M)          // External service
    1.2  signalLabel ← argmax(P)          // Primary classification
    1.3  confidence ← max(P)              // Confidence value
    1.4  severity ← COMPUTE_SEVERITY(confidence)
    1.5  category ← CLASSIFY_CATEGORY(signalLabel)
    1.6  E ← EmotionMetadata(signalLabel, confidence, severity, 
                             category, NOW())
    
    ┌─────────────────────────────────────────────────────────┐
    │ STAGE 2: RESPONSE STRATEGY CONTROL                      │
    └─────────────────────────────────────────────────────────┘
    
    2.1  S ← STRATEGY_CONTROLLER(E)       // Map to strategy
    2.2  C ← CONSTRAINT_GENERATOR(E, S)   // Generate constraints
    
    ┌─────────────────────────────────────────────────────────┐
    │ STAGE 3: CONSTRAINED OUTPUT GENERATION                  │
    └─────────────────────────────────────────────────────────┘
    
    3.1  request ← BUILD_STRUCTURED_REQUEST(M, E, S, C, U, H)
    3.2  R ← GENERATE_CONSTRAINED(request)
    
    ┌─────────────────────────────────────────────────────────┐
    │ STAGE 4: STATE UPDATE                                   │
    └─────────────────────────────────────────────────────────┘
    
    4.1  STORE_INTERACTION(M, R, E)
    4.2  UPDATE_ACCUMULATED_STATE(U.id, E)
    
    RETURN (R, E)

END PROCEDURE
```

### Algorithm 2: Response Strategy Controller (RSC)

**Technical Classification:** Rule-Based Control Module

**Formal Specification:**

```
ALGORITHM: Response Strategy Controller (RSC)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

INPUT:
    E = EmotionMetadata object

OUTPUT:
    S = StrategyParameters object
    C = ConstraintSpec object

CONSTANT STRATEGY_MAP: (as defined in Section 6)

PROCEDURE RSC(E):
    
    1.  baseStrategy ← STRATEGY_MAP[E.signalLabel]
    
    2.  // SEVERITY-BASED MODIFICATION
        IF E.severity = HIGH AND E.category = NEGATIVE:
            baseStrategy.intensity ← ELEVATED
            baseStrategy.techniques.prepend("crisis_assessment")
            baseStrategy.escalationFlag ← TRUE
        ELSE IF E.severity = MEDIUM:
            baseStrategy.intensity ← STANDARD
        ELSE:
            baseStrategy.intensity ← LIGHT
    
    3.  // CONSTRAINT GENERATION
        C ← ConstraintSpec()
        C.required ← baseStrategy.techniques
        C.prohibited ← baseStrategy.contraindications
        C.escalation ← baseStrategy.escalationFlag
        
        IF E.category = NEGATIVE:
            C.safetyEnforcement ← TRUE
    
    4.  S ← StrategyParameters(baseStrategy)
    
    RETURN (S, C)

END PROCEDURE
```

### Algorithm 3: Longitudinal State Accumulator (LSA)

**Technical Classification:** Stateful Analytics Engine

**Formal Specification:**

```
ALGORITHM: Longitudinal State Accumulator (LSA)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

INPUT:
    userId = User identifier
    period = Analysis period {DAY | WEEK | MONTH | ALL}

OUTPUT:
    A = AccumulatedState object

PROCEDURE LSA_COMPUTE(userId, period):
    
    1.  signals ← QUERY_SIGNALS(userId, period)
        N ← LENGTH(signals)
        IF N = 0: RETURN AccumulatedState(insufficientData=TRUE)
    
    ┌─────────────────────────────────────────────────────────┐
    │ METRIC 1: EMOTION DISTRIBUTION                          │
    └─────────────────────────────────────────────────────────┘
    
    2.  distribution ← {}
        FOR EACH label IN {joy, sadness, anger, fear, surprise, love}:
            count ← COUNT(signals WHERE signalLabel = label)
            distribution[label] ← count / N
    
    ┌─────────────────────────────────────────────────────────┐
    │ METRIC 2: POSITIVITY RATIO                              │
    └─────────────────────────────────────────────────────────┘
    
    3.  positiveCount ← COUNT(signals WHERE signalLabel IN {joy, love})
        positivityRatio ← positiveCount / N
    
    ┌─────────────────────────────────────────────────────────┐
    │ METRIC 3: STABILITY SCORE                               │
    └─────────────────────────────────────────────────────────┘
    
    4.  transitions ← 0
        FOR i ← 1 TO N-1:
            IF signals[i].signalLabel ≠ signals[i-1].signalLabel:
                transitions ← transitions + 1
        transitionRate ← transitions / (N - 1)
        stabilityScore ← 1 - transitionRate
    
    ┌─────────────────────────────────────────────────────────┐
    │ METRIC 4: TRAJECTORY                                    │
    └─────────────────────────────────────────────────────────┘
    
    5.  previousPositivity ← QUERY_PREVIOUS_POSITIVITY(userId, period)
        trajectoryDelta ← positivityRatio - previousPositivity
        IF trajectoryDelta > 0.1: trajectory ← IMPROVING
        ELSE IF trajectoryDelta < -0.1: trajectory ← DECLINING
        ELSE: trajectory ← STABLE
    
    ┌─────────────────────────────────────────────────────────┐
    │ WARNING FLAG GENERATION                                 │
    └─────────────────────────────────────────────────────────┘
    
    6.  warnings ← []
        IF positivityRatio < 0.3 AND N > 10:
            warnings.add(Warning(PERSISTENT_NEGATIVITY, HIGH))
        IF stabilityScore < 0.3:
            warnings.add(Warning(HIGH_VOLATILITY, MEDIUM))
        IF trajectory = DECLINING AND trajectoryDelta < -0.2:
            warnings.add(Warning(TRAJECTORY_DECLINE, HIGH))
    
    7.  A ← AccumulatedState(distribution, positivityRatio, 
                             stabilityScore, trajectory, warnings)
    
    RETURN A

END PROCEDURE
```

### Algorithm 4: Crisis State Machine (CSM)

**Technical Classification:** Finite State Machine with Multi-Signal Input

**Formal Specification:**

```
ALGORITHM: Crisis State Machine (CSM)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

INPUT:
    currentState = Current system state
    E = Current EmotionMetadata
    A = AccumulatedState
    L = LinguisticSignals (crisis keyword detection)

OUTPUT:
    newState = Updated system state
    actions = List of escalation actions

STATES: {NORMAL, ELEVATED, HIGH_ALERT, CRITICAL}

PROCEDURE CSM_EVALUATE(currentState, E, A, L):
    
    riskScore ← 0
    signals ← []
    
    ┌─────────────────────────────────────────────────────────┐
    │ SIGNAL 1: EMOTION-BASED RISK                            │
    └─────────────────────────────────────────────────────────┘
    
    1.1  IF E.severity = HIGH AND E.category = NEGATIVE:
            riskScore += 25
            signals.add("high_severity_negative")
    
    ┌─────────────────────────────────────────────────────────┐
    │ SIGNAL 2: LINGUISTIC PATTERN RISK                       │
    └─────────────────────────────────────────────────────────┘
    
    2.1  IF L.crisisKeywordDetected:
            riskScore += 35
            signals.add("crisis_keyword")
    
    ┌─────────────────────────────────────────────────────────┐
    │ SIGNAL 3: LONGITUDINAL PATTERN RISK                     │
    └─────────────────────────────────────────────────────────┘
    
    3.1  IF A.warnings CONTAINS CRISIS_PATTERN:
            riskScore += 20
            signals.add("longitudinal_warning")
    
    3.2  IF A.trajectory = DECLINING AND A.trajectoryDelta < -0.3:
            riskScore += 15
            signals.add("trajectory_decline")
    
    ┌─────────────────────────────────────────────────────────┐
    │ STATE TRANSITION LOGIC                                  │
    └─────────────────────────────────────────────────────────┘
    
    4.  IF riskScore >= 60:
            newState ← CRITICAL
        ELSE IF riskScore >= 40:
            newState ← HIGH_ALERT
        ELSE IF riskScore >= 20:
            newState ← ELEVATED
        ELSE:
            newState ← NORMAL
    
    ┌─────────────────────────────────────────────────────────┐
    │ ACTION DETERMINATION                                    │
    └─────────────────────────────────────────────────────────┘
    
    5.  actions ← []
        IF newState = CRITICAL:
            actions ← [modify_response_safety, provide_resources,
                       express_concern, flag_session]
        ELSE IF newState = HIGH_ALERT:
            actions ← [modify_response_safety, mention_support]
        ELSE IF newState = ELEVATED:
            actions ← [enhanced_validation]
    
    RETURN (newState, actions)

END PROCEDURE
```

---

## 7. System Architecture Diagrams

### 7.1 High-Level Control Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                    CLIENT APPLICATION TIER                           │
├─────────────────────────────────────────────────────────────────────┤
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────────────────┐  │
│  │ Conversation │  │  Analytics   │  │  State Visualization      │  │
│  │  Interface   │  │  Dashboard   │  │                           │  │
│  └──────┬───────┘  └──────┬───────┘  └───────────┬───────────────┘  │
└─────────┼──────────────────┼──────────────────────┼──────────────────┘
          │                  │                      │
          └──────────────────┼──────────────────────┘
                             │ API
                             ▼
┌─────────────────────────────────────────────────────────────────────┐
│                    PROCESSING SERVER TIER                            │
├─────────────────────────────────────────────────────────────────────┤
│  ┌───────────────────────────────────────────────────────────────┐  │
│  │                 MULTI-STAGE PROCESSING PIPELINE               │  │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐   │  │
│  │  │  Stage 1:   │  │  Stage 2:   │  │     Stage 3:        │   │  │
│  │  │  Emotion    │──│  Strategy   │──│   Constrained       │   │  │
│  │  │  Signal     │  │  Controller │  │    Generator        │   │  │
│  │  │  Processor  │  │             │  │                     │   │  │
│  │  └─────────────┘  └─────────────┘  └─────────────────────┘   │  │
│  │        │                │                    │               │  │
│  │        └────────────────┴────────────────────┘               │  │
│  │                         │                                    │  │
│  │         EmotionMetadata propagation throughout               │  │
│  └───────────────────────────────────────────────────────────────┘  │
│                             │                                       │
│  ┌───────────────────────────────────────────────────────────────┐  │
│  │           LONGITUDINAL STATE ACCUMULATION ENGINE              │  │
│  └───────────────────────────────────────────────────────────────┘  │
│                             │                                       │
│  ┌───────────────────────────────────────────────────────────────┐  │
│  │                   CRISIS STATE MACHINE                        │  │
│  └───────────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────┘
          │                  │                      │
          ▼                  ▼                      ▼
┌───────────────┐  ┌─────────────────┐  ┌─────────────────────────────┐
│  Emotion      │  │  Text           │  │  Persistent                 │
│  Classifier   │  │  Generator      │  │  Storage                    │
│  (External)   │  │  (External)     │  │                             │
└───────────────┘  └─────────────────┘  └─────────────────────────────┘
```

### 7.2 Data Flow Diagram

```
User Input
    │
    ▼
┌───────────────────────────────────────────────────────────────┐
│  STAGE 1: Emotion Signal Processor                            │
│  ─────────────────────────────────                            │
│  Input: "I'm feeling really anxious about tomorrow"           │
│  Processing: External emotion classification service          │
│  Output: EmotionMetadata {                                    │
│      signalLabel: "fear",                                     │
│      confidence: 0.92,                                        │
│      severity: HIGH,                                          │
│      category: NEGATIVE                                       │
│  }                                                            │
└───────────────────────────────────────────────────────────────┘
    │
    │ EmotionMetadata (mandatory propagation)
    ▼
┌───────────────────────────────────────────────────────────────┐
│  STAGE 2: Response Strategy Controller                        │
│  ─────────────────────────────────────                        │
│  Input: EmotionMetadata                                       │
│  Processing: Strategy mapping + severity modification         │
│  Output: StrategyParameters {                                 │
│      approach: "reassurance_grounding",                       │
│      tone: ["calm", "supportive"],                            │
│      intensity: ELEVATED                                      │
│  }                                                            │
│  Output: ConstraintSpec {                                     │
│      required: ["validation_first", "grounding_offer"],       │
│      prohibited: ["catastrophizing", "rushing"],              │
│      safetyEnforcement: true                                  │
│  }                                                            │
└───────────────────────────────────────────────────────────────┘
    │
    │ StrategyParameters + ConstraintSpec (mandatory propagation)
    ▼
┌───────────────────────────────────────────────────────────────┐
│  STAGE 3: Constrained Output Generator                        │
│  ─────────────────────────────────────                        │
│  Input: Message + Strategy + Constraints                      │
│  Processing: Structured request to text generation service    │
│  Output: Constrained response adhering to specifications      │
│                                                               │
│  "I can hear that you're feeling anxious about tomorrow,      │
│   and those feelings are completely valid. Let's take a       │
│   moment together—would you like to try a grounding           │
│   exercise to help center yourself?"                          │
└───────────────────────────────────────────────────────────────┘
    │
    ▼
Response to User + EmotionMetadata stored for longitudinal analysis
```

---

## 8. Technical Validation

### System Latency Performance:

| Component | Latency | Requirement |
|-----------|---------|-------------|
| Stage 1: Emotion Signal Processing | <200ms | Real-time interaction |
| Stage 2: Strategy Controller | <5ms | Negligible overhead |
| Stage 3: Constrained Generation | ~800-1000ms | Acceptable for conversational use |
| Total Pipeline | <1.5s | Suitable for real-time conversation |

### System State Transitions:

| From State | To State | Trigger Condition |
|------------|----------|-------------------|
| NORMAL | ELEVATED | riskScore >= 20 |
| ELEVATED | HIGH_ALERT | riskScore >= 40 |
| HIGH_ALERT | CRITICAL | riskScore >= 60 |
| Any | NORMAL | stability confirmed, riskScore < 20 |

### Constraint Enforcement Validation:

| Constraint Type | Enforcement Mechanism | Validation Method |
|-----------------|----------------------|-------------------|
| Required elements | Mandatory prompt sections | Output inspection |
| Prohibited patterns | Negative constraints in prompt | Pattern matching |
| Safety enforcement | Explicit safety rules in prompt | Rule compliance check |
| Escalation actions | State-triggered additions | Action verification |

---

## 9. Claims

### Independent Claim 1: Multi-Stage Response Regulation System

A computer-implemented conversational response regulation system comprising:

**(a)** an emotion signal processor configured to receive natural language input and produce a structured emotion metadata object comprising a signal classification, a confidence value, a severity indicator, and a category classification;

**(b)** a response strategy controller configured to receive the emotion metadata object and produce strategy parameters comprising an approach identifier, constraint specifications, and escalation indicators, wherein the strategy parameters are derived from the emotion metadata through deterministic mapping logic with severity-based modification;

**(c)** a constrained output generator configured to receive the user input, the emotion metadata object, and the strategy parameters, and to produce a response output constrained by the strategy parameters and constraint specifications;

wherein the emotion metadata object propagates through all stages as mandatory input, ensuring that response generation is governed by the detected emotional signal and derived constraints.

### Dependent Claim 1.1: Severity-Based Modification

The system of Claim 1, wherein the response strategy controller implements severity-based modification comprising:
- detection of high-severity negative emotional signals triggering elevated constraint intensity;
- prepending of safety-related techniques to the technique list;
- setting of escalation flags for downstream processing.

### Dependent Claim 1.2: Structured Constraint Specification

The system of Claim 1, wherein the constraint specification comprises:
- a required elements list specifying mandatory response characteristics;
- a prohibited elements list specifying content patterns to avoid;
- a safety enforcement flag activating safety rules;
- an escalation flag triggering resource provision.

### Dependent Claim 1.3: Structured Output Request

The system of Claim 1, wherein the constrained output generator constructs a structured generation request comprising:
- a role definition section;
- an emotional context section incorporating the emotion metadata;
- a strategy directive section incorporating the strategy parameters;
- a constraint enforcement section incorporating the constraint specification;
- a safety rules section.

### Independent Claim 2: Longitudinal State Accumulation

A computer-implemented method for modifying conversational system behavior based on accumulated emotional state, comprising:

**(a)** collecting and storing emotion metadata objects from multiple user interactions with associated timestamps;

**(b)** computing aggregate metrics from the accumulated emotion metadata, the metrics comprising:
- an emotion distribution representing the frequency of each emotion signal classification;
- a positivity ratio representing the proportion of positive emotional signals;
- a stability score representing the emotional consistency over the accumulation period;
- a trajectory indicator representing the direction of emotional pattern change;

**(c)** generating warning flags when computed metrics exceed defined thresholds;

**(d)** modifying the response strategy controller behavior based on the computed metrics and warning flags;

wherein the accumulated state causes runtime behavior modification, such that system responses are influenced by historical patterns in addition to current input.

### Dependent Claim 2.1: Warning Generation

The method of Claim 2, wherein warning flags are generated based on:
- persistent negativity: positivity ratio below threshold for minimum signal count;
- high volatility: stability score below threshold;
- trajectory decline: negative trajectory delta exceeding threshold.

### Dependent Claim 2.2: Behavior Modification

The method of Claim 2, wherein response strategy controller behavior modification comprises:
- adjusting strategy selection based on trajectory indicator;
- increasing response intensity based on warning flags;
- triggering proactive system responses based on pattern detection.

### Independent Claim 3: Crisis State Machine

A computer-implemented crisis handling method for conversational systems, comprising:

**(a)** maintaining a current system state from a defined set of states comprising NORMAL, ELEVATED, HIGH_ALERT, and CRITICAL;

**(b)** evaluating multiple input signals to compute a risk score, the signals comprising:
- emotion-based signals derived from current emotion metadata severity and category;
- linguistic signals derived from crisis pattern detection in user input;
- longitudinal signals derived from accumulated state warning flags;
- session signals derived from current session negativity ratio;

**(c)** determining state transitions based on risk score thresholds;

**(d)** triggering state-specific actions based on the current state, the actions comprising response modification and escalation actions;

wherein the crisis handling is implemented as a finite state machine with defined states, transition rules, and state-specific behaviors.

### Dependent Claim 3.1: Multi-Signal Risk Scoring

The method of Claim 3, wherein the risk score is computed by weighted combination of:
- emotion severity signal (weight: 25 for high-severity negative);
- linguistic crisis signal (weight: 35 for crisis keyword detection);
- longitudinal warning signal (weight: 20 for crisis pattern warning);
- trajectory decline signal (weight: 15 for severe decline).

### Dependent Claim 3.2: State-Specific Actions

The method of Claim 3, wherein state-specific actions comprise:
- ELEVATED state: enhanced validation in response;
- HIGH_ALERT state: safety prioritization and support mention;
- CRITICAL state: crisis response mode with resource provision and session flagging.

### Independent Claim 4: Emotion Metadata Propagation Protocol

A computer-implemented method for ensuring emotion-aware processing in multi-stage conversational systems, comprising:

**(a)** defining a structured emotion metadata schema comprising signal classification, confidence value, severity indicator, category, and timestamp;

**(b)** producing an emotion metadata object at the first stage of processing based on user input analysis;

**(c)** propagating the emotion metadata object as mandatory input to each subsequent processing stage;

**(d)** utilizing the emotion metadata object at each stage to inform stage-specific processing decisions;

**(e)** persisting the emotion metadata object with the interaction record for longitudinal accumulation;

wherein the emotion metadata propagation ensures consistent emotional context across all processing stages and enables longitudinal analysis.

---

## 10. Technical Effect Statement (Patent Eligibility)

### Compliance with India Patents Act Section 3(k):

This invention is **not** a mathematical method, algorithm, or computer program *per se*. It is a **computer-implemented system** that produces concrete technical effects:

1. **Technical Problem:** Conversational systems produce contextually inappropriate responses because they lack emotion-aware constraint enforcement.

2. **Technical Solution:** A multi-stage architecture with mandatory emotion metadata propagation and severity-based constraint enforcement.

3. **Technical Effect:** Responses are demonstrably constrained by emotional context, reducing inappropriate outputs measured by constraint compliance rate.

### Compliance with USPTO Alice Test:

**Step 1:** The claims are directed to a specific technical improvement in conversational systems, not an abstract idea.

**Step 2A Prong 1:** Even if emotional processing involves mental concepts, the claims integrate them into a practical, technical implementation.

**Step 2A Prong 2:** The claims provide meaningful limitations:
- Specific multi-stage architecture with defined data flow
- Mandatory metadata propagation requirements
- Deterministic control logic with defined mappings
- State machine with defined transitions

**Step 2B:** The claims recite inventive concepts:
- The specific combination of stages with data dependencies
- The severity-based modification logic
- The multi-signal risk scoring for state transitions

### Compliance with EPO Technical Effect Doctrine:

The invention produces technical effects beyond the normal operation of a computer:

1. **Improved Data Processing:** Multi-stage architecture with metadata propagation improves processing accuracy.

2. **Constraint Enforcement:** The system enforces output constraints based on input analysis, a technical function.

3. **State-Based Control:** The crisis state machine implements technical control logic.

4. **Longitudinal Behavior Modification:** Accumulated state alters runtime behavior, a technical system characteristic.

---

## 11. Declaration

We, the undersigned inventors, hereby declare that:

1. The above information is true and complete to the best of our knowledge.

2. We believe we are the original inventors of the subject matter described herein.

3. We acknowledge VIT's Intellectual Property Rights policies and procedures.

4. The invention describes a **computer-implemented response regulation system** with:
   - Multi-stage processing architecture with defined data dependencies
   - Emotion metadata propagation protocol
   - Severity-based response constraint enforcement
   - Longitudinal state accumulation affecting runtime behavior
   - Crisis state machine with defined state transitions

5. We have reframed the invention to focus on **control architecture and system behavior** rather than psychological methods, model architectures, or performance metrics.

6. The claims protect the **technical integration and control logic**, not the individual components (emotion classification, text generation) which are acknowledged as existing in prior art.

| Inventor Name | Designation | Signature | Date |
|---------------|-------------|-----------|------|
| **Oshim Pathan** | B.Tech Student / Primary Inventor | _________________ | 08.02.2026 |
| | | | |

---

## 12. Appendix: Patent-Safe Language Guide

### Terms TO USE (Technical Control Language):

| Use This | Instead Of |
|----------|-----------|
| Emotion signal | Detected emotion |
| Signal classification | Emotion prediction |
| Response strategy controller | Therapeutic mapping algorithm |
| Constrained output generator | LLM with therapeutic prompting |
| Constraint specification | Therapeutic rules |
| State machine | Crisis intervention protocol |
| Severity indicator | Distress level |
| Accumulated state | Patient history |
| Runtime behavior modification | Personalized therapy |

### Terms TO AVOID (Psychological/Medical Language):

| Avoid | Reason |
|-------|--------|
| Therapy, therapeutic, treatment | Medical claims → Section 3(k) rejection |
| CBT, DBT, Person-Centered | Psychological methods → not patentable |
| Diagnosis, clinical, patient | Medical practice → regulatory issues |
| BERT, GPT, Gemini, HuggingFace | Model-specific → easily designed around |
| Accuracy, F1-score, precision | Performance metrics → not claim-worthy |
| Mental health, depression, anxiety | Medical conditions → scope limitation |

---

**END OF EXAMINER-SAFE PATENT DISCLOSURE**
