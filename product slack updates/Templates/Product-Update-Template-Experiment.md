# Product Update Template - Experiment

Template for experiment updates.

**[{type}] {title}**

:question: **Why We Built It**
{why_built}

:bulb: **Hypothesis**
{hypothesis}

:gear: **How It Works**

{how_it_works}

:bar_chart: **Objective{% if objectives|length > 1 %}s{% endif %}**

{objectives}

:date: **Experiment details**

{experiment_details}

{% if links %}
:eyes: **Learn more**

{links}
{% endif %}

:supergirl: :superman: **Meet the makers**
{team_members}
{% if channel_mention %}
Please reach out if you have any questions to {channel_mention} :mooncake:
{% endif %}
{% if stakeholders %}
cc: {stakeholders}
{% endif %}

