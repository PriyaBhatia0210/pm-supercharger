# Product Update Template - Iteration

Template for iteration updates (e.g., Iteration 2, Iteration 3).

**[{iteration_number}: {title}]**

{% if previous_signals %}
**Signals from {previous_iteration} (Final Report from Data team WIP):**

{previous_signals}
{% endif %}

**So what's new?**

{whats_new}

{% if why_now %}
**Why now?**

{why_now}
{% endif %}

{% if experiment_design %}
**Experiment Design**

{experiment_design}
{% endif %}

{% if next_steps %}
**Next Steps**

{next_steps}
{% endif %}

Please let me know any questions.

Meet the makers: {team_members}

{% if stakeholders %}
cc; {stakeholders}
{% endif %}

