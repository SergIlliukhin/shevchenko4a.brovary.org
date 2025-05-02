---
layout: home
title: Головна
coverImage: /wp-content/uploads/2009/09/heading.jpg
---

# {{ site.title }}

{{ site.description }}

## Сторінки

{% for page in site.pages %}
{% if page.title %}
- [{{ page.title }}]({{ page.url | relative_url }})
{% endif %}
{% endfor %}

## Публікації

{% for post in site.posts %}
- [{{ post.title }}]({{ post.url | relative_url }}) - {{ post.date | date: "%d.%m.%Y" }}
{% endfor %}