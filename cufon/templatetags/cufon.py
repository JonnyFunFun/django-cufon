# -*- coding: utf-8 -*-
from django.conf import settings
from django.template import TemplateSyntaxError
from django import template
import random, string

register = template.Library()


class CufonTextNode(template.Node):
    def __init__(self, text, font):
        self._text = text
        self._font = font

    def render(self, context):
        element_id = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(12))
        return """
            <span id="%(el_id)s">%(text)s</span>
            <script type="text/javascript">
                Cufon.replace(document.getElementById("%(el_id)s"), {fontFamily: '%(font)s'});
            </script>
        """ % {'el_id': element_id, 'text': self._text, 'font': self._font}


@register.tag(name="cufon")
def do_cufon_text(parser, token):
    """
    You need to pass in the text and font you wish to be rendered with Cufon.

    Usage::
        {% include cufon %}
        {% cufon "My Super Text" "SuperFont" %}

    Be sure to use {% cufon-scripts %} in your HEAD before using this.
    """
    try:
        tag_name, text, desired_font = token.split_contents()
    except ValueError:
        raise TemplateSyntaxError("%r tag requires exactly two arguments (text, font)" % token.contents.split()[0])
    for arg in (text, desired_font, ):
        if not (arg[0] == arg[-1] and arg[0] in ('"', "'")):
            raise template.TemplateSyntaxError("%r tags argument should be in quotes" % tag_name)
    return CufonTextNode(text[1:-1], desired_font[1:-1])


class CufonScriptIncludeNode(template.Node):
    def render(self, context):
        return """
                <script type="text/javascript" src="%s/cufon/cufon-yui.js"></script>
            """ % settings.STATIC_URL.rstrip('/')


@register.tag(name="cufon-scripts")
def include_cufon_javascript(parser, token):
    """
    Includes the required Cufon JavaScript

    Usage::
        {% include cufon %}
        {% cufon-scripts %}
        [... include your fonts ...]

    Be sure to use this in HEAD and be sure to include your Cufon fonts after this line
    """
    return CufonScriptIncludeNode()