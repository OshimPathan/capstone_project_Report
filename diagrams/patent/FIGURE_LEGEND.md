# REBIRTH Patent Figures - Reference Numeral Legend

## FIGURE 1: System Architecture
**File:** FIG1_system_architecture.png

| Reference | Description |
|-----------|-------------|
| **100** | Mobile Client Tier - User-facing application layer |
| 101 | User Interface Module - Main UI controller |
| 102 | Chat Interface - Conversational interaction screen |
| 103 | Analytics Display - Longitudinal emotion visualization |
| 104 | Profile Manager - User settings and preferences |
| **200** | Backend Server Tier - Application logic layer |
| 201 | API Gateway - RESTful endpoint router |
| 202 | Authentication Module - JWT token verification |
| 203 | Chat Controller - Message processing coordinator |
| **210** | EGRG Pipeline - Emotion-Guided Response Generation system |
| 211 | Stage 1: Emotion Detection - BERT-based classification |
| 212 | Stage 2: Therapeutic Mapping - TRM algorithm execution |
| 213 | Stage 3: Prompt Generation - EGP protocol processing |
| 204 | Emotion Service - Emotion analysis coordinator |
| 205 | Decision Service - Response strategy selector |
| **300** | External Services Tier - Third-party integrations |
| 301 | BERT Inference API - HuggingFace emotion model |
| 302 | LLM Generation API - Google Gemini response generator |
| 303 | Database Service - MongoDB Atlas persistence |

---

## FIGURE 2: Processing Pipeline (EGRG Algorithm)
**File:** FIG2_processing_pipeline.png

| Reference | Description |
|-----------|-------------|
| **400** | User Input Stage - Natural language message reception |
| 401 | Natural Language Message - Raw user text input |
| **410** | Stage 1: Emotion Detection - Classification phase |
| 411 | BERT Classifier - Transformer-based emotion model |
| 412 | Probability Computation - Softmax probability calculation |
| 413 | Metadata Enrichment - Additional emotion attributes |
| **420** | Emotion Output - Classification results |
| 421 | Primary Emotion Label - Highest probability emotion |
| 422 | Confidence Score - Classification certainty percentage |
| 423 | Category Classification - Positive/negative/neutral |
| 424 | Severity Level - Low/medium/high intensity |
| **430** | Stage 2: Therapeutic Mapping - TRM algorithm phase |
| 431 | Strategy Lookup Table - Emotion-to-strategy mappings |
| 432 | Approach Selection - Therapeutic methodology choice |
| 433 | Tone Determination - Response voice and warmth setting |
| **440** | Stage 3: Prompt Construction - EGP algorithm phase |
| 441 | Context Integration - User history and session context |
| 442 | Therapeutic Instructions - LLM behavioral constraints |
| 443 | Crisis Protocol Check - CIP activation evaluation |
| **450** | Response Generation - LLM processing phase |
| 451 | LLM Processing - Gemini response generation |
| 452 | Response Validation - Output quality verification |
| **460** | Output Stage - Final response delivery |
| 461 | Therapeutic Response - Emotion-aware AI response |

---

## FIGURE 3: Database Schema
**File:** FIG3_database_schema.png

| Reference | Description |
|-----------|-------------|
| **USER_500** | User Entity - Primary user account record |
| id_501 | Primary key identifier |
| name_502 | User display name |
| email_503 | Authentication email address |
| password_504 | Bcrypt-hashed password |
| onboarding_505 | Onboarding questionnaire responses |
| goals_506 | User-defined therapeutic goals array |
| createdAt_507 | Account creation timestamp |
| **SESSION_510** | Chat Session Entity - Conversation container |
| id_511 | Session primary key |
| user_512 | Foreign key to USER_500 |
| title_513 | Session display title |
| messagesCount_514 | Total message counter |
| lastMessageAt_515 | Last activity timestamp |
| archived_516 | Archive status flag |
| **BUCKET_520** | Message Bucket Entity - Bucketed storage pattern |
| id_521 | Bucket primary key |
| session_522 | Foreign key to SESSION_510 |
| bucketIndex_523 | Bucket sequence number |
| count_524 | Messages in bucket |
| messages_525 | Embedded message array |
| **MESSAGE_530** | Message Entity - Individual message record |
| role_531 | Sender role (user/assistant) |
| text_532 | Message text content |
| emotionData_533 | Embedded emotion analysis |
| createdAt_534 | Message timestamp |
| **EMOTION_540** | Emotion Data Entity - Classification results |
| emotion_541 | Primary detected emotion |
| confidence_542 | Classification confidence score |
| category_543 | Emotion valence category |
| severity_544 | Emotion intensity level |
| responseStrategy_545 | TRM algorithm output |
| allEmotions_546 | Full probability distribution |

---

## FIGURE 4: Message Flow Sequence
**File:** FIG4_message_flow.png

| Reference | Description |
|-----------|-------------|
| **600** | User Device - End-user mobile device |
| **601** | Mobile App - Flutter application instance |
| **602** | API Server - Express.js backend server |
| **603** | BERT Service - Emotion classification service |
| **604** | TRM Module - Therapeutic Response Mapping |
| **605** | EGP Module - Emotion-Guided Prompting |
| **606** | LLM Service - Gemini response generator |
| **607** | Database - MongoDB persistence layer |
| 610 | Input message text - User types message |
| 611 | POST /api/chat/message - API request |
| 612 | Authenticate token - JWT verification |
| 613 | Request emotion classification - BERT call |
| 614 | Return emotion probabilities - Classification result |
| 615 | Compute emotion metadata - Enrichment step |
| 616 | Request therapeutic strategy - TRM invocation |
| 617 | Return TRM mapping - Strategy response |
| 618 | Request prompt construction - EGP invocation |
| 619 | Return EGP prompt - Constructed prompt |
| 620 | Generate AI response - LLM call |
| 621 | Return generated text - AI response |
| 622 | Store message + metadata - Persistence |
| 623 | Confirm persistence - Storage acknowledgment |
| 624 | Return response + emotionData - API response |
| 625 | Render response UI - Display processing |
| 626 | Display to user - Final presentation |

---

## FIGURE 5: Technology Stack
**File:** FIG5_technology_stack.png

| Reference | Description |
|-----------|-------------|
| **700** | Presentation Layer - Client-side technologies |
| 701 | Flutter Framework - Cross-platform UI framework |
| 702 | Dart Runtime - Programming language runtime |
| 703 | Provider State Management - Reactive state management |
| 704 | HTTP Client Module - Network communication |
| **710** | Application Layer - Server-side technologies |
| 711 | Node.js Runtime - JavaScript server runtime |
| 712 | Express.js Framework - Web application framework |
| 713 | JWT Authentication - Token-based security |
| 714 | Mongoose ODM - MongoDB object modeling |
| **720** | Security Layer - Protection mechanisms |
| 721 | Helmet Security Headers - HTTP header protection |
| 722 | CORS Configuration - Cross-origin security |
| 723 | Rate Limiting Module - Request throttling |
| 724 | Bcrypt Password Hashing - Credential protection |
| **730** | AI/ML Processing Layer - Intelligence components |
| 731 | BERT Emotion Classifier - Transformer model |
| 732 | Gemini LLM Generator - Response generation |
| 733 | TRM Algorithm Module - Therapeutic mapping |
| 734 | EGP Algorithm Module - Prompt construction |
| 735 | CIP Crisis Protocol - Crisis intervention |
| **740** | Data Persistence Layer - Storage systems |
| 741 | MongoDB Atlas Cluster - Cloud database |
| 742 | Local Secure Storage - Device-side storage |
| **750** | Cloud Infrastructure - Deployment platforms |
| 751 | Vercel Serverless - Backend hosting |
| 752 | HuggingFace Inference - ML model hosting |
| 753 | Google Cloud AI - LLM API provider |

---

## FIGURE 6: Analytics System (LEA Algorithm)
**File:** FIG6_analytics_system.png

| Reference | Description |
|-----------|-------------|
| **800** | Data Collection Stage - Input gathering |
| 801 | User Message Input - Raw conversational data |
| 802 | Emotion Classification - Per-message analysis |
| 803 | Timestamped Storage - Temporal data recording |
| **810** | LEA Analytics Engine - Core analysis system |
| **811** | Metric Computation Subsystem - Statistical analysis |
| 812 | Emotion Distribution Calculator - Frequency analysis |
| 813 | Positivity Ratio Analyzer - Valence ratio computation |
| 814 | Stability Score Generator - Volatility measurement |
| 815 | Daily Trend Aggregator - Temporal pattern grouping |
| **820** | Pattern Detection Subsystem - Behavioral analysis |
| 821 | Dominant Emotion Detector - Primary emotion identification |
| 822 | Persistence Analyzer - Emotion duration tracking |
| 823 | Shift Detection Module - Change point detection |
| **830** | Early Warning System - Alert generation |
| 831 | High Volatility Alert - Instability warning |
| 832 | Negative Dominance Alert - Prolonged negativity warning |
| 833 | Crisis Detection Trigger - CIP activation signal |
| **840** | Visualization Output - User-facing displays |
| 841 | Emotion Trend Charts - Time-series visualization |
| 842 | Wellness Score Display - Aggregate health metric |
| 843 | Progress Tracking View - Longitudinal progress |

---

## Patent Drawing Standards Compliance

These figures conform to:
- **37 CFR 1.84** - USPTO drawing standards
- **Rule 11 PCT** - International patent drawing requirements
- **Indian Patent Rules** - Form 2 drawing specifications

### Drawing Characteristics:
- Black and white only (no color/grayscale shading)
- Clear reference numerals (100-series numbering)
- Each element uniquely identified
- Clean line drawings suitable for reproduction
- 2x scale for high-resolution printing

### Usage Instructions:
1. Include all 6 figures in patent application
2. Reference numerals in claims should match this legend
3. Brief Description of Drawings section should enumerate each figure
4. Detailed Description should explain each reference numeral
