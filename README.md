# James O'Hagan

### Healthcare IT Systems | Interoperability | Quality & Reliability Engineering

I am a healthcare IT systems and software quality professional with 20+ years of experience supporting mission-critical federal and Department of Defense healthcare applications.

My background spans enterprise clinical systems, production support, HL7 integrations, middleware, databases, application infrastructure, performance analysis, release validation, and cross-team troubleshooting. Much of my career involved following complex healthcare transactions across application, interface, database, infrastructure, and network boundaries to determine whether systems were functioning correctly and reliably.

I am now applying that systems background to modern healthcare interoperability, integration quality, and reliability engineering.

---

## Current Focus

My current technical work centers on:

- **HL7 v2 and MLLP**
- **FHIR R4 and healthcare APIs**
- **Mirth Connect**
- **Patient identity and cross-system reconciliation**
- **Healthcare integration testing**
- **Python and pytest automation**
- **PostgreSQL and SQL validation**
- **API-to-database consistency testing**
- **Failure, recovery, replay, and reliability testing**
- **Docker-based test environments**
- **Performance and release-quality validation**
- **Playwright browser automation**

The goal is not simply to test individual screens or endpoints, but to validate whether healthcare transactions remain correct across complete system boundaries.

---

# Featured Engineering Work

## 🏥 Healthcare IT Operations & Interoperability Lab

[View Repository](https://github.com/jtohagan716/health-it-operations-interoperability-lab)

A hands-on healthcare interoperability environment built to validate clinical transactions across EHR, interface-engine, API, database, and transport boundaries.

### Current validated capabilities

- OpenEMR clinical application environment
- FHIR Patient API access and validation
- HL7 v2.5.1 `ADT^A04` messaging
- MLLP transport
- Mirth Connect interface processing
- PostgreSQL integration audit persistence
- HL7 `MSH-10` / ACK `MSA-2` transaction reconciliation
- FHIR-to-HL7 patient identity reconciliation
- Automated Mirth ACK testing
- Automated database persistence validation
- Unique transaction generation for integration tests
- Controlled downstream dependency failure testing
- HL7 `AE` validation during persistence failure
- Verification that failed transactions are not falsely recorded as persisted
- Dependency restoration and recovery validation
- Source-controlled and sanitized Mirth channel configuration

### Example reliability scenario

```text
HEALTHY

ADT^A04
   ↓
Mirth Connect
   ↓
PostgreSQL persistence
   ↓
AA acknowledgment
   ↓
Transaction reconciled
```

```text
DOWNSTREAM FAILURE

ADT^A04
   ↓
Mirth Connect remains available
   ↓
PostgreSQL unavailable
   ↓
Database Writer fails
   ↓
AE acknowledgment
   ↓
Failed transaction absent from audit database
```

```text
RECOVERY

PostgreSQL restored
   ↓
New ADT^A04
   ↓
Persistence succeeds
   ↓
AA acknowledgment
   ↓
Recovery transaction verified
```

This project is being expanded into additional patient-identity, laboratory, FHIR, clinical application, reliability, and eventually DICOM/PACS workflows.

---

## 🔬 SDET Reliability Framework

[View Repository](https://github.com/jtohagan716/sdet-reliability-framework)

A reliability-focused software quality engineering framework designed to go beyond simple functional pass/fail testing.

Areas covered include:

- API validation
- API contract testing
- Automated regression testing
- PostgreSQL-backed behavior
- API-to-database consistency
- Query-plan and index validation
- Retry and idempotency behavior
- Queue and asynchronous-processing reliability
- Performance baselines
- p95 / p99 latency analysis
- Lightweight load testing
- Observability
- OpenTelemetry
- Prometheus
- Grafana
- Jaeger
- Postman / Newman
- Playwright
- Docker
- GitHub Actions
- Release-quality gates

The project focuses on answering a broader engineering question:

> **Did the system merely respond, or did the complete transaction behave correctly and reliably?**

---

## 🌐 Playwright Automation Engineering Lab

[View Repository](https://github.com/jtohagan716/playwright-automation-engineering-lab)

Browser automation work focused on maintainable Playwright and TypeScript testing patterns, including reusable abstractions, authentication flows, UI validation, and scalable test design.

This complements the API, interoperability, database, and reliability testing demonstrated in my other projects.

---

# Healthcare Systems Background

My production experience includes work with technologies and environments such as:

```text
AHLTA / CHCS
HL7
Oracle
BEA Tuxedo
IIS / .NET application infrastructure
eGate integration
Windows Server
LoadRunner
SQL / database diagnostics
Enterprise application failover
Production incident troubleshooting
Release and regression validation
Performance analysis
Clinical application support
```

That work required collaboration across development, database, infrastructure, network, operations, and healthcare application teams.

The modern projects on this profile are intended to extend that experience into current interoperability and quality-engineering technologies rather than replace the systems knowledge developed over my career.

---

# Engineering Perspective

The problems that interest me most sit between systems.

For an integration transaction, I want to be able to answer:

```text
What entered the system?
        ↓
Which patient and transaction does it represent?
        ↓
Where was it routed?
        ↓
Did the downstream operation actually occur?
        ↓
What acknowledgment was returned?
        ↓
Does the response agree with persisted system state?
        ↓
What happens when a dependency fails?
        ↓
Can the system recover cleanly?
```

That systems-level approach is the common thread between my healthcare IT background and my current interoperability and reliability work.

---

# Professional Direction

I am particularly interested in opportunities involving:

- Healthcare Interoperability
- Healthcare Integration Engineering
- Interface Engineering
- Healthcare Integration QA
- Application Integration
- Clinical Application Support
- Healthcare Systems Quality
- SDET / Reliability Engineering
- EHR Integration
- HL7 / FHIR Validation
- Application Reliability and Release Validation

I am especially interested in roles where deep healthcare systems experience can be combined with modern interoperability, automation, and reliability engineering.

---

## Core Technologies

**Healthcare & Interoperability**  
HL7 v2 · FHIR · MLLP · Mirth Connect · OpenEMR · Patient Identity · Clinical Workflows

**Quality & Automation**  
Python · pytest · Playwright · TypeScript · Postman/Newman · LoadRunner · JMeter

**Data & Middleware**  
PostgreSQL · Oracle · SQL · BEA Tuxedo · eGate

**Systems & Reliability**  
Docker · Git · GitHub Actions · IIS · Windows Server · Performance Analysis · Observability · Failure & Recovery Testing

---

### Current Engineering Goal

Build public, reproducible evidence of modern healthcare interoperability and reliability engineering capability while applying the production systems knowledge developed through more than two decades supporting enterprise healthcare technology.
