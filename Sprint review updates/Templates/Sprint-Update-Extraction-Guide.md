# Sprint Update Extraction Guide

This guide explains how to extract information from various sources to generate Product Review Updates and Growth Sprint Presentation slides.

## Overview

The templating system supports multiple information sources:
- Sprint Planning Meeting notes
- PRDs (Product Requirements Documents)
- Metrics dashboards and reports
- Other meeting notes and documents

## Source Type: Sprint Planning Meeting Notes

### File Structure
Sprint Planning Meeting notes typically contain:
- Meeting header (date, owner, participants)
- Project Overview
- Technical Architecture Discussion
- Sprint Planning Decisions
- Next Steps / Action Items
- Clarifications
- Links
- Transcript (optional)

### Key Fields to Extract

#### Sprint Information
**Location:** "Sprint Planning Decisions" section or meeting header
**Pattern:** Look for "Sprint #[number]" or date ranges
**Extract:**
- Sprint number
- Start date
- End date
**Use in:** Both Product Review Updates and Presentation slides

#### Sprint Goal
**Location:** "Sprint Planning Decisions" section
**Pattern:** Look for "Sprint goal:" followed by quoted text
**Extract:** The exact sprint goal statement
**Use in:** Presentation Slide 2 (What's Coming Up)

#### Project Overview
**Location:** "Project Overview" section
**Pattern:** Usually has goals, approach, decision trees
**Extract:**
- Project/initiative name
- Goals and objectives
- Approach or methodology
- Key features or components
**Use in:** Product Review Updates (initiative descriptions), Presentation (context)

#### Technical Decisions
**Location:** "Technical Architecture Discussion" section
**Pattern:** Lists of decisions, considerations, open questions
**Extract:**
- Architecture decisions
- Data source choices
- Service ownership
- Integration points
**Use in:** Product Review Updates (technical context), Presentation (focus areas)

#### Team Availability
**Location:** "Sprint Planning Decisions" → "Availability"
**Pattern:** List of team members with PTO or constraints
**Extract:**
- Team member names
- Dates of unavailability
- Special events (hackathon, team building)
**Use in:** Product Review Updates (if relevant), Presentation (context)

#### Action Items
**Location:** "Next Steps / Action Items" section
**Pattern:** Organized by owner or team member
**Extract:**
- Owner name
- Action item description
- Dependencies or related work
**Use in:** 
- Product Review Updates (next steps)
- Presentation Slide 2 (planned work)

#### Clarifications
**Location:** "Clarifications from Discussion" section
**Pattern:** Bullet points of decisions or clarifications
**Extract:**
- Key decisions made
- Important clarifications
- Edge cases or special considerations
**Use in:** Product Review Updates (context), Presentation (if relevant)

#### Links
**Location:** "Links" section
**Pattern:** List of URLs
**Extract:**
- Meeting notes links
- PRD links
- Dashboard links
- Other relevant resources
**Use in:** Both outputs (as references)

### Example Extraction

**Input (Sprint Planning Meeting):**
```
## Sprint Planning Decisions

* Sprint goal: "Begin decision tree development"
* Availability:
  * Priya off Thu–Fri
  * Marcel OOO second week
```

**Extracted:**
- Sprint Goal: "Begin decision tree development"
- Availability: Priya (Thu-Fri), Marcel (second week)

## Source Type: PRDs (Product Requirements Documents)

### Key Fields to Extract

#### Feature/Initiative Name
**Location:** Document title or main heading
**Extract:** The feature or initiative name
**Use in:** Both outputs (as initiative headers)

#### Goals and Objectives
**Location:** Usually in "Goals" or "Objectives" section
**Extract:**
- Primary goals
- Success metrics
- Target outcomes
**Use in:** Product Review Updates (initiative descriptions), Presentation (context)

#### Current State
**Location:** "Current State" or "Background" section
**Extract:**
- Baseline metrics
- Current performance
- Existing problems
**Use in:** Product Review Updates (context for why initiative exists)

#### Hypothesis
**Location:** "Hypothesis" or "Assumptions" section
**Extract:**
- Test hypotheses
- Expected outcomes
- Assumptions being validated
**Use in:** Product Review Updates (approach description)

#### Approach/Solution
**Location:** "Approach", "Solution", or "Implementation" section
**Extract:**
- How the feature works
- Key components
- User flows
**Use in:** Product Review Updates (technical details), Presentation (what was built)

#### Metrics and Success Criteria
**Location:** "Success Metrics" or "KPIs" section
**Extract:**
- Target metrics
- Success thresholds
- Measurement approach
**Use in:** Product Review Updates (when results are available)

### Example Extraction

**Input (PRD):**
```
## Hypothesis

**H1**: By personalizing save offers based on contract type and tenure, 
we can increase the Starter plan save rate from 15% to 18% while 
retaining more MRR per saved customer.
```

**Extracted:**
- Hypothesis: Personalization increases save rate from 15% to 18%
- Target: Starter plan customers
- Approach: Based on contract type and tenure

## Source Type: Metrics Dashboards and Reports

### Key Fields to Extract

#### Test Results
**Location:** Dashboard results, test summaries
**Extract:**
- Variant performance
- Control vs variant metrics
- Statistical significance
- Links to dashboards
**Use in:** Product Review Updates (results section), Presentation Slide 1 (completed work with metrics)

#### Performance Metrics
**Location:** Performance dashboards, analytics
**Extract:**
- Conversion rates
- Save rates
- Revenue metrics
- User engagement
**Use in:** Both outputs (quantitative updates)

#### Trends
**Location:** Time-series data, trend analysis
**Extract:**
- Month-over-month changes
- Direction of trends
- Period comparisons
**Use in:** Product Review Updates (context for results)

### Example Extraction

**Input (Dashboard/Report):**
```
Pure PAYG test results:
- Variant: ~30% activation rate
- Control: ~6% activation rate
- Overall: 15% higher save rate
```

**Extracted:**
- Test: Pure PAYG
- Variant performance: 30% activation
- Control performance: 6% activation
- Improvement: 15% higher save rate

## Source Type: Other Meeting Notes

### Key Fields to Extract

#### Decisions Made
**Location:** Decision logs, meeting summaries
**Extract:**
- Key decisions
- Rationale
- Impact
**Use in:** Product Review Updates (context), Presentation (if relevant)

#### Blockers and Dependencies
**Location:** Blocker sections, dependency lists
**Extract:**
- Current blockers
- Resolved blockers
- Dependencies
**Use in:** Product Review Updates (status updates), Presentation (planned work)

#### Updates from Other Teams
**Location:** Cross-functional meeting notes
**Extract:**
- Related work from other teams
- Integration points
- Coordination needs
**Use in:** Product Review Updates (if relevant to your team)

## Combining Multiple Sources

### Best Practices

1. **Prioritize Sprint Planning Meeting** - This is the primary source for sprint-specific information
2. **Supplement with PRDs** - Use for detailed feature descriptions and context
3. **Add metrics from dashboards** - Include quantitative results when available
4. **Include relevant context** - Pull from other sources only when it adds value
5. **Maintain consistency** - Ensure information from different sources doesn't contradict

### Example: Multi-Source Extraction

**Sprint Planning Meeting:**
- Sprint goal: "Begin decision tree development"
- Action item: "Lead architecture spike"

**PRD:**
- Initiative: "Personalized Churn Deflection Flow"
- Goal: "Balance logo retention and MRR retention"
- Approach: "Personalized retention based on tenure and subscription type"

**Dashboard:**
- Previous test: 15% save rate with Launch plan
- MRR saved dropped ~30% MoM

**Combined Output:**
```
* **New initiative in delivery: Personalizing Churn Save offers based on account profile:**
  * We were successful in saving logo churn with the launch and fake door pay per doc test.
  * However, we are seeing a drop in MRR saved in the cancellation flow (~30% MoM).
  * This initiative aims at balancing logo churn with MRR churn.
  * We will be personalizing the churn save offer depending on the customer's plan, tenure as well as reason for cancellation.
  * We kicked off development for only Starter plan personalization this sprint.
```

## Field Mapping Reference

### Product Review Updates Mapping

| Update Section | Source Field | Location |
|---------------|-------------|----------|
| Sprint number | Sprint number | Sprint Planning Meeting |
| Sprint dates | Start/End dates | Sprint Planning Meeting |
| Initiative name | Project Overview | Sprint Planning Meeting or PRD |
| Status | Action items, Sprint goal | Sprint Planning Meeting |
| Metrics | Dashboard results | Metrics dashboards |
| Context | Project Overview, PRD | Sprint Planning Meeting, PRD |
| Next steps | Action Items | Sprint Planning Meeting |

### Growth Sprint Presentation Mapping

| Slide Section | Source Field | Location |
|--------------|-------------|----------|
| Completed work | Action items (completed) | Sprint Planning Meeting |
| Deliverables | Shipped features | Sprint Planning Meeting, PRD |
| Metrics | Dashboard results | Metrics dashboards |
| Sprint goal | Sprint goal | Sprint Planning Meeting |
| Planned work | Action Items, Next Steps | Sprint Planning Meeting |
| Focus areas | Technical Architecture | Sprint Planning Meeting |
| Demo content | Completed features | PRD, Sprint Planning Meeting |

## Usage Instructions

### Step 1: Gather Sources
Collect all relevant documents:
- Sprint Planning Meeting notes
- Related PRDs
- Metrics dashboards/reports
- Other relevant meeting notes

### Step 2: Extract Key Information
Use this guide to extract:
- Sprint information (number, dates, goal)
- Initiative details
- Status and progress
- Metrics and results
- Action items and next steps

### Step 3: Generate Updates
Use the templates:
- `Sprint-Update-Template-Product-Review.md` for Product Review Updates
- `Sprint-Update-Template-Growth-Presentation.md` for Presentation slides

### Step 4: Review and Refine
- Ensure information is accurate
- Check for consistency across sources
- Add appropriate context
- Include relevant links

## Tips for Effective Extraction

1. **Look for patterns** - Similar information appears in similar places across documents
2. **Cross-reference** - Verify information across multiple sources when possible
3. **Prioritize recent information** - Sprint Planning Meeting is usually most current
4. **Extract numbers** - Metrics and percentages are valuable for updates
5. **Capture links** - Include dashboard links, PRD links, and other resources
6. **Note status changes** - Track progression from planning → delivery → completed
7. **Include context** - Don't just extract facts, include why they matter

