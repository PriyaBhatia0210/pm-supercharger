**[Feature] Personalized Churn Deflection Flow**

:information_source: **Why We Built It**
Balance logo retention and MRR retention. Previous approach (Launch plan / Free+overages) saved logos but MRR saved dropped ~30% MoM. We're implementing personalized retention for Starter plan customers based on tenure and subscription type.

:gear: **How It Works**

* Decision tree approach:
  * Offer 1 (in cancellation flow): coupon or annual discount  
  * If declined: allow cancellation, then  
  * Offer 2 (in-app before expiry): next-cheapest plan shown via banner
* Preference to keep decision logic in backend; need to respect MS API product checkout domain boundaries
* Use current subscription start date for tenure calculation (clearer UX, simpler implementation)

:date: **Timeline**

* Sprint goal: "Begin decision tree development"
* Architecture spike to determine service ownership and domain boundaries
* Possible integration with personalization framework

:female-technologist: **Meet the makers**

@priya.bhatia @marcel.vienny @ines.freitas

cc @supportteam @csms

