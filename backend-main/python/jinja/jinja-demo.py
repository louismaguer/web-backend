from jinja2 import Template

data = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 22}
]

template_str = """
{% for person in people %}
{{ person.name }} is {{ person['age'] }} years old.
{% endfor %}
"""

template = Template(template_str)
output = template.render(people=data)

print(output)
