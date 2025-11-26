**[Feature] Price alignment for detached customers**

:information_source: **Why We Built It**
We found substantial ARR leakage across legacy and discounted pricing structures. A review revealed customers with extreme customizations (e.g., 4 seats at $0, 500 API calls for $2), making simple % increases impossible. Because of this, increasing prices requires a phased strategy and account-by-account reasoning for complex cases.

:gear: **How It Works**

* Wave 1 (Dec–Jan): Business Monthly v4 → v7 Migration
  * Fully automated upgrade from v4 → v7
  * Projected +$233,676 ARR
* Wave 2 (Late Q1): Detached Customers (Custom Pricing)
  * Renewal-based uplifts using a segmented, Finance-approved model
* Wave 3 (Q2+): AM-Attached Customers
  * AM team fully owns uplift decisions, customer communication, and approval
  * R&D provides tools, data, and technical execution if required

:date: **Rollout Plan**

* Dec 1 – Communications launched  
* Jan 1 – Begin migration  
* Jan 31 – Complete migration + results review
* Late Q1 – Execute detached customer price uplifts
* Starting Q2 – AM team begins applying uplifts to AM-attached customers

:female-technologist: **Meet the makers**

* Product: @yurii.losinets
* Design: @evgeni.maliukov
* Engineering: @aleks.dyadichkina
* PMM: @kaitlyn.walsh

:bar_chart: **Learn more:**

* [PRD](https://docs.google.com/document/d/1RCugCrrvzSu7fSpLy0ahMwsYel5F8UmXvhfZ-ooX1RY/edit?tab=t.0)
* [Jira](https://pandadoc.atlassian.net/browse/PD-XXXXX)

cc @supportteam @ams @csms

