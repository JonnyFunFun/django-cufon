from django.test import TestCase
from django.template.loader import get_template_from_string
from django.template import Context, TemplateSyntaxError
import re


class TestHeadTags(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_cufon_script_tag(self):
        template = get_template_from_string(u"""
            {% load cufon %}
            {% cufon-scripts %}
        """)
        c = Context()
        html = template.render(c)
        self.assertTrue('cufon-yui.js' in html)


class TestCufonTags(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_cufon_text_basic(self):
        template = get_template_from_string(u"""
            {% load cufon %}
            {% cufon-scripts %}
            {% cufon "Test" "Arial" %}
        """)
        c = Context()
        html = template.render(c)
        self.assertTrue('">Test</span>' in html)
        self.assertTrue("Cufon.replace" in html)

    def test_cufon_args_need_quotes(self):
        self.assertRaises(TemplateSyntaxError, get_template_from_string, """
                {% load cufon %}
                {% cufon Test Arial %}
            """)