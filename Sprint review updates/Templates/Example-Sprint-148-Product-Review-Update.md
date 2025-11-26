# Example: Sprint 148 Product Review Update

This is an example output generated using the Sprint-Update-Template-Product-Review.md template, based on the Sprint Planning Meeting notes for Sprint 148.

---

# 🙏 Nov 25 Update

# Sprint Update 148

## **Sprint #148: Nov 24, 2025 - Dec 5, 2025**

* **New initiative in delivery: Personalizing Churn Save offers based on account profile:**  
  * Goal: Balance logo retention and MRR retention  
  * Previous approach (Launch plan / Free+overages) saved logos but MRR saved dropped ~30% MoM  
  * This initiative aims at balancing logo churn with MRR churn  
  * We will be personalizing the churn save offer depending on the customer's plan, tenure as well as reason for cancellation, and will be offering them the most suitable plan so that we are not offering the cheapest plan to them in the first go  
  * Approach: Personalized retention for Starter plan customers based on tenure and subscription type  
  * Decision tree includes:  
    * Offer 1 (in cancellation flow): coupon or annual discount  
    * If declined: allow cancellation, then  
    * Offer 2 (in-app before expiry): next-cheapest plan shown via banner  
  * We kicked off development for only Starter plan personalization this sprint  
  * Sprint goal: "Begin decision tree development"  
  * Architecture spike initiated to determine service ownership and domain boundaries  
  * If successful, we will extend this to Business plan customers as well as iterate with more behavioural triggers

* **Technical Architecture Work:**  
  * Decision: Use current subscription start date for tenure calculation (clearer UX, simpler implementation)  
  * Preference to keep decision logic in backend; need to respect MS API product checkout domain boundaries  
  * Investigating integration with personalization framework  
  * Clarifying backend vs frontend responsibilities and dependencies

* **Team Updates:**  
  * Marcel officially joined the team  
  * Priya off Thu–Fri this sprint  
  * Marcel OOO second week  
  * Some managers on hackathon; engineers focusing on engineering work

## **Next Steps**

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

## **Links**

* Sprint Planning Notes: [https://notes.granola.ai/t/0781e851-f8e2-4db4-a63e-95925c502c99](https://notes.granola.ai/t/0781e851-f8e2-4db4-a63e-95925c502c99)

