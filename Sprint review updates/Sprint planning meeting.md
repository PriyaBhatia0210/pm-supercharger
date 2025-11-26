I can’t attach files here, but you can copy this Markdown and save it as [meeting.md](http://meeting.md/):

# **\[Sprint planning\] Team Spirit \- Growth Monetization**

Date: 2025-11-24 18:30 Owner: Priya Bhatia (Senior PM, Growth, PandaDoc) Participants: spirit, Marcel Vienny, Ines Freitas

## **Project Overview: Personalized Churn Deflection Flow**

* Goal: Balance logo retention and MRR retention  
  * Previous approach (Launch plan / Free+overages) saved logos but MRR saved dropped \~30% MoM  
* Approach:  
  * Personalized retention for Starter plan customers based on tenure and subscription type  
  * Decision tree:  
    * Offer 1 (in cancellation flow): coupon or annual discount  
    * If declined: allow cancellation, then  
    * Offer 2 (in-app before expiry): next-cheapest plan shown via banner

## **Technical Architecture Discussion**

* Location of logic:  
  * Preference to keep decision logic in backend; need to respect MS API product checkout domain boundaries  
* Tenure data source:  
  * Considered org creation date  
  * Decision: use current subscription start date (clearer UX, simpler implementation)  
* Open questions / spike scope:  
  * Service ownership and domain boundaries  
  * Possible integration with personalization framework  
  * Backend vs frontend responsibilities and dependencies

## **Sprint Planning Decisions**

* Sprint goal: “Begin decision tree development”  
* Availability:  
  * Priya off Thu–Fri  
  * Marcel OOO second week  
  * Some managers on hackathon; engineers focusing on engineering work  
* Notes:  
  * Existing technical debt tickets available while spike proceeds  
  * Marcel officially joins; extend planning by \~10 minutes on alternate Mondays if needed

## **Next Steps / Action Items**

* Marcel:  
  * Lead architecture spike  
  * Consult Dima on domain ownership  
  * Investigate personalization service options  
  * Create and add spike ticket to epic  
* Team:  
  * Continue technical work and tests during spike  
* Priya:  
  * Post sprint goal  
  * 1:1 sync with Marcel; schedule intro 1:1s

## **Clarifications from Discussion**

* Offer 2 appears in-app after cancellation and before expiry (not sequentially inside the cancellation flow)  
* Starter monthly path considers tenure from current subscription start date  
* Decision logic likely to live in backend long-term; first iteration may be pragmatic to ship

## **Links**

* Notes: [https://notes.granola.ai/t/0781e851-f8e2-4db4-a63e-95925c502c99](https://notes.granola.ai/t/0781e851-f8e2-4db4-a63e-95925c502c99)

## **Transcript (abridged reference)**

* Team welcomed Marcel; discussed hackathon participation and PTO  
* Reviewed churn decision tree and clarified when and where offers show  
* Debated data sources and where the logic should live  
* Agreed on a spike to determine architecture and ownership  
* Set sprint goal and immediate next steps

