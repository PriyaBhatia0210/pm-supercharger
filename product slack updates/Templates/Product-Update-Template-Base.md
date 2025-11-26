# Product Update Template - Base

This is the base template for generating product update Slack messages. Use type-specific templates for different update types.

## Template Structure

**{title}**

{emoji_why} **Why We Built It**
{why_built}

{% if hypothesis %}
{emoji_hypothesis} **Hypothesis**
{hypothesis}
{% endif %}

{emoji_how} **How It Works**
{how_it_works}

{% if objectives %}
{emoji_objectives} **Objective{% if objectives|length > 1 %}s{% endif %}**
{objectives}
{% endif %}

{% if timeline %}
{emoji_timeline} **{% if update_type == 'rollout' %}Rollout Plan{% elif update_type == 'experiment' %}Experiment details{% else %}Timeline{% endif %}**
{timeline}
{% endif %}

{% if monitoring %}
{emoji_monitoring} **What we're monitoring:**
{monitoring}
{% endif %}

{% if guardrails %}
{emoji_guardrails} **Guardrails**
{guardrails}
{% endif %}

{% if how_to_help %}
{emoji_help} **How you can help:**
{how_to_help}
{% endif %}

{emoji_makers} **Meet the makers**
{team_members}
{% if channel_mention %}
Please reach out if you have any questions to {channel_mention} {emoji_team}
{% endif %}

{% if links %}
{emoji_learn} **Learn more**
{links}
{% endif %}

{% if stakeholders %}
cc: {stakeholders}
{% endif %}

## Emoji Mapping Guide

- **Why We Built It**: :information_source: or :question: or :rocket:
- **Hypothesis**: :bulb:
- **How It Works**: :gear:
- **Objectives/Metrics**: :bar_chart: or :chart_with_upwards_trend:
- **Timeline/Experiment Details**: :date:
- **Rollout Plan**: :date: or :traffic_light:
- **Monitoring**: :female-construction-worker: or :bar_chart:
- **Guardrails**: :roller_coaster:
- **How to Help**: :handshake:
- **Meet the Makers**: :supergirl: :superman: or :extreme-teamwork: or :female-technologist:
- **Learn More**: :eyes: or :mag: or :documentportraitfilled:
- **Team Emoji**: :mooncake: or :green_heart: :muscle: (varies by team)

## Variable Reference

- `{title}` - Feature/experiment name with type tag (e.g., "[Experiment] Feature Name")
- `{why_built}` - Why we built it section content
- `{hypothesis}` - Hypothesis (for experiments)
- `{how_it_works}` - How it works section content
- `{objectives}` - Objectives/success metrics (bullet list)
- `{timeline}` - Timeline/rollout plan (bullet list)
- `{monitoring}` - What we're monitoring (bullet list)
- `{guardrails}` - Guardrails/monitoring (bullet list)
- `{how_to_help}` - How you can help (bullet list)
- `{team_members}` - Formatted team member tags (e.g., "@teammooncake @username")
- `{channel_mention}` - Channel mention (e.g., "#team-mooncake")
- `{emoji_team}` - Team-specific emoji
- `{links}` - Learn more links (formatted list)
- `{stakeholders}` - Formatted stakeholder CCs (e.g., "@supportteam @ams")
- `{update_type}` - Type of update (experiment, rollout, feature, iteration)
- `{feature_flags}` - Feature flags if applicable
- `{tldr}` - TL;DR section (for feature releases)

