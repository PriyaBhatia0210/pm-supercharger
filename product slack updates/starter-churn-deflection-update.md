**[Feature] Starter Plan Cost-Value based Churn Deflection**

***TL;DR***

We're launching a **personalized churn deflection flow** for Starter plan customers who cite cost/value as their cancellation reason. By tailoring offers based on contract type (Annual/Monthly) and customer tenure, we aim to maintain our ~15% save rate while improving MRR retention through strategic downgrades and discounts.

:checkered_flag: ***What's changing?***

* **Target Segment**: Starter plan customers only who select "cost_value" as cancellation reason (29.3% of all churners)
* **Personalized Offer Logic**:
  * **Annual Starter (all tenures)**: 25% discount on Starter Annual → Launch Annual (post-cancellation)
  * **Monthly Starter (0-3 months)**: Launch Monthly → Free eSign (post-cancellation)
  * **Monthly Starter (3-11 months)**: Starter Annual → Launch Annual (post-cancellation)
  * **Monthly Starter (12+ months)**: Starter Annual with 25% discount → Launch Annual (post-cancellation)
* **Two-stage approach**: In-flow offers during cancellation + post-cancellation banners until account expiry

:flags: ***Why we're doing this:***

* **82% of churn dollars** happen in-product, with Starter plan representing a high-impact segment
* **Current state**: All Starter churners see the same Launch offer, resulting in 15% save rate but lower MRR retention
* **Key learning**: Launch was successful in preventing logo churn but not dollar churn - Starter MRR churn increased 32% MoM in September
* **One-size-fits-all doesn't work**: Annual customers (higher commitment) and new customers (0-3 months) need different offers
* **Opportunity**: Personalization allows us to retain higher MRR through targeted downgrades vs. steep discounts

:traffic_light: ***How we're rolling out:***

* **Test Duration**: 30 days
* **Scope**: Starter plan + cost_value cancellation reason only
* **Success Metric**: Maintain save rate at ~15% while improving MRR saved per saved customer

:female-construction-worker: ***What we're monitoring:***

* Save rate (target: maintain ~15%)
* MRR saved per saved customer (target: improve vs. current Launch-only approach)
* Conversion rate by offer type (discount vs. downgrade)
* MRR retention by customer segment (Annual vs. Monthly, by tenure)
* Post-cancellation banner acceptance rate

:roller_coaster: ***Guardrails***

* MVP scope limited to Starter plan + cost_value reason only
* Feature-flagged for controlled rollout
* Out of scope: Other cancellation reasons, other plan tiers, customers without payment method, customers with active support escalations

:handshake: ***How you can help:***

* **Support / CS / AM**: Share feedback on customer responses to personalized offers
* **Everyone**: Report any issues or unexpected behavior in the cancellation flow

:documentportraitfilled: ***More details:***

* [PRD](https://docs.google.com/document/d/1YMhBxyLDfSG6N7ByjhrBIdzxjixPVe2pYgTMHaBuPV0/edit?tab=t.0)

Huge thanks to @priya.bhatia @alona.zaleska @teamspirit Let's go! :green_heart: :muscle:

cc. @supportteam @csms @ams
