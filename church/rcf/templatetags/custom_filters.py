from django import template

register = template.Library()

@register.filter(name='add_class')
def add_class(field, css_class):
    """
    Add a CSS class to a form field widget.
    Usage in template: {{ form.field_name|add_class:"class-name" }}
    """
    return field.as_widget(attrs={"class": css_class})
