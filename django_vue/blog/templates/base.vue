{% comment %}
MUST SET vue_element CONTEXT VARIABLE
The context vue_element names the element in the html. Any vue code should extend this to be dry
{% endcomment %}

{% block globalfunctions %}
{% endblock globalfunctions %}

new Vue({
  delimiters: ['[[', ']]'],
  el: '#{{ vue_element }}',
  {% block vuescript %}
  {% endblock vuescript %}
})