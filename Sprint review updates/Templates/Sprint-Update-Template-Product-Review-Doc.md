# Sprint Update Template - Product Review Updates

Use this template to generate Product Review Updates from Sprint Planning Meeting notes and other relevant documents.

## Template Structure

```
# [Emoji] [Date] Update

# Sprint Update [Sprint Number]

## **Sprint #[Sprint Number]: [Start Date] - [End Date]**

* **[Initiative/Feature Name 1]:**  
  * [Status update - completed, in progress, or planned]
  * [Key details, metrics, or results if available]
  * [Next steps or blockers if relevant]
  
* **[Initiative/Feature Name 2]:**  
  * [Status update]
  * [Key details, metrics, or results if available]
  * [Next steps or blockers if relevant]
```

## Information Extraction Guide

### From Sprint Planning Meeting Notes

**Sprint Number and Dates:**
- Look for: "Sprint #[number]" or "Sprint goal" section
- Extract: Sprint number, start date, end date
- Format: `## **Sprint #[NUMBER]: [START DATE] - [END DATE]**`

**Sprint Goal:**
- Look for: "Sprint goal" or "Sprint Planning Decisions" section
- Use: As context for what the sprint is focused on

**Key Initiatives/Projects:**
- Look for: "Project Overview" section
- Extract: Project name, goals, approach
- Format: As bullet points under initiative name

**Status Indicators:**
- "New initiative in planning" → Use for planning phase
- "New initiative in delivery" → Use for active development
- "Completed" or "Shipped" → Use for finished work
- "In progress" → Use for ongoing work

**Metrics and Results:**
- Look for: Numbers, percentages, links to dashboards
- Extract: Key metrics, test results, performance data
- Include: Links to dashboards or reports when available

**Team Updates:**
- Look for: "Availability" or "Team" sections
- Extract: PTO, team building, special events
- Format: As a bullet point if relevant

**Action Items:**
- Look for: "Next Steps / Action Items" section
- Extract: Key action items that impact sprint work
- Format: As context for what's coming up

### From Other Information Sources

**From PRDs:**
- Extract: Feature descriptions, goals, hypotheses
- Use: To provide context for initiatives
- Format: As background or approach details

**From Metrics Dashboards:**
- Extract: Key metrics, test results, performance indicators
- Use: To add quantitative updates
- Format: Include numbers with context and links

**From Other Meeting Notes:**
- Extract: Decisions, blockers, dependencies
- Use: To provide additional context
- Format: As relevant bullet points

## Example Output

```
# 🙏 Nov 25 Update

# Sprint Update 148

## **Sprint #148: Nov 24, 2025 - Dec 5, 2025**

* **Self-Serve API Plan:**  
  * API plan is all set to go live.  
  * Marketing team is hooking up the plan trial to dev portal links.  
* **New initiative in delivery: Personalizing Churn Save offers based on account profile:**  
  * We were successful in saving logo churn with the launch and fake door pay per doc test.   
  * However, we are seeing a drop in MRR saved in the cancellation flow.   
  * This initiative aims at balancing logo churn with MRR churn.   
  * We will be personalizing the churn save offer depending on the customer's plan, tenure as well as reason for cancellation, and will be offering them the most suitable plan so that we are not offering the cheapest plan to them in the first go.  
  * We kicked off development for only Starter plan personalization this sprint.   
  * If successful, we will extend this to Business plan customers as well as iterate with more behavioural triggers.
```

## Tips

1. **Use appropriate emojis** for the update header (e.g., 🙏, 🦃, 🎉, 🤸)
2. **Keep bullet points concise** but informative
3. **Include metrics** when available (percentages, numbers, links)
4. **Group related updates** under the same initiative
5. **Use status indicators** to show progress (planning, delivery, completed)
6. **Add context** from multiple sources when it adds value
7. **Include links** to dashboards, PRDs, or other relevant documents

## Common Status Phrases

- "New initiative in planning:" - Just starting to plan
- "New initiative in delivery:" - Actively being developed
- "Completed" or "Shipped" - Finished work
- "In progress" - Ongoing work
- "Ready for release" - Completed and ready to launch
- "Exploratory testing" - Testing phase
- "Bugs identified and being fixed" - Issues found, working on fixes

