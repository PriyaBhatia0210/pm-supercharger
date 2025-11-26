# Growth Sprint Presentation - Team Spirit
## Sprint 148 Review

---

# Slide 1: What Was Done This Sprint - Team Spirit

## Sprint #148: Nov 24, 2025 - Dec 5, 2025

### Completed Work

* **Self-Serve API Plan**
  * API plan finalized and ready to go live
  * Marketing team integrating plan trial with dev portal links

* **Personalized Churn Deflection - Planning & Kickoff**
  * Kicked off development for Starter plan personalization initiative
  * Initiated architecture spike to determine service ownership and domain boundaries
  * Sprint goal defined and posted: "Begin decision tree development"

* **Team Onboarding & Integration**
  * Marcel officially joined Team Spirit
  * Team planning process adjusted to accommodate new team member
  * Planning extended by ~10 minutes on alternate Mondays as needed

* **Technical Architecture Decisions**
  * Decided to use current subscription start date for tenure calculation (clearer UX, simpler implementation)
  * Determined preference to keep decision logic in backend
  * Identified need to respect MS API product checkout domain boundaries

### Key Deliverables

* Self-Serve API Plan ready for launch
* Architecture spike ticket created and added to epic
* Sprint goal posted: "Begin decision tree development"
* Technical architecture approach documented
* Team integration completed

---

# Slide 2: What's Coming Up Next Sprint - Team Spirit

## Sprint #149: Dec 8, 2025 - Dec 19, 2025

### Sprint Goal

Begin decision tree development for personalized churn deflection

### Planned Work

* **Personalized Churn Deflection - Architecture & Development**
  * Continue architecture spike to determine domain boundaries and service ownership
  * Consult with Dima on domain ownership decisions
  * Investigate personalization service integration options
  * Begin decision tree development based on spike findings
  * Clarify backend vs frontend responsibilities and dependencies

* **Team Coordination**
  * Continue technical work and tests during spike period
  * Leverage existing technical debt tickets while spike proceeds
  * 1:1 syncs with Marcel; schedule intro 1:1s

### Focus Areas

* Architecture and service ownership decisions
* Integration with personalization framework
* Backend vs frontend responsibilities
* Decision tree implementation for Starter plan customers
* Tenure-based personalization logic (using current subscription start date)

### Context

**Initiative Goal:** Balance logo retention and MRR retention
- Previous approach (Launch plan / Free+overages) saved logos but MRR saved dropped ~30% MoM
- New approach: Personalized retention for Starter plan customers based on tenure and subscription type
- Decision tree flow:
  - Offer 1 (in cancellation flow): coupon or annual discount
  - If declined: allow cancellation, then
  - Offer 2 (in-app before expiry): next-cheapest plan shown via banner

---

# Slide 3: Demo - Team Spirit

## Personalized Churn Deflection Flow - Architecture Overview

### What We're Showing

Architecture approach and decision tree design for personalized churn deflection

### Key Highlights

* **Decision Tree Flow:**
  - Offer 1: Coupon or annual discount in cancellation flow
  - Offer 2: Next-cheapest plan banner in-app after cancellation (before expiry)
  
* **Personalization Logic:**
  - Based on customer plan (Starter focus for MVP)
  - Based on tenure (using current subscription start date)
  - Based on cancellation reason
  
* **Technical Approach:**
  - Backend decision logic (preferred)
  - Respects MS API product checkout domain boundaries
  - Integration with personalization framework (under investigation)

* **MVP Scope:**
  - Starter plan customers only
  - If successful, extend to Business plan customers
  - Future iterations with more behavioral triggers

### Demo Link/Details

* Sprint Planning Notes: [https://notes.granola.ai/t/0781e851-f8e2-4db4-a63e-95925c502c99](https://notes.granola.ai/t/0781e851-f8e2-4db4-a63e-95925c502c99)
* Architecture spike ticket (in epic)

