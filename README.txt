regex:
search:
\b(src|href)="([^"]*)"\b

change:
$1="{% static '$2' %}"