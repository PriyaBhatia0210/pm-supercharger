# Product Update Template - Feature Release

Template for feature release updates.

**[{{ type }}] {{ title }}**

{% if tldr %}
***TL;DR***

{{ tldr }}
{% endif %}

{% if whats_changing %}
:checkered_flag: ***What's changing?***

{{ whats_changing }}
{% endif %}

{% if feature_flags %}
Feature Flags: {{ feature_flags }}
{% endif %}

:flags: ***Why we're doing this:***

{{ why_built }}

{% if rollout_details %}
:traffic_light: ***How we're rolling out:***

{{ rollout_details }}
{% endif %}

{% if monitoring %}
:female-construction-worker: ***What we're monitoring:***

{{ monitoring }}
{% endif %}

{% if guardrails %}
:roller_coaster: ***Guardrails***

{{ guardrails }}
{% endif %}

{% if how_to_help %}
:handshake: ***How you can help:***

{{ how_to_help }}
{% endif %}

:documentportraitfilled: ***More details:***

{{ links }}

Huge thanks to {{ team_members }} Let's go! :green_heart: :muscle:
{% if stakeholders %}
cc. {{ stakeholders }}
{% endif %}

