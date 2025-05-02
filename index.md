---
layout: home
title: Головна
coverImage: /wp-content/uploads/2009/09/heading.jpg
---

# {{ site.title }}

{{ site.description }}

## Навігація

{% for page in site.pages %}
{% if page.title %}
- [{{ page.title }}]({{ page.url | relative_url }})
{% endif %}
{% endfor %}