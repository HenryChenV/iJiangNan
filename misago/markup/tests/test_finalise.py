# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from misago.markup.finalise import finalise_markup


class QuoteTests(TestCase):
    def test_finalise_markup(self):
        """quote header is replaced"""
        test_text = '''
<p>Lorem ipsum.</p>
<aside class="quote-block">
<div class="quote-heading"></div>
<blockquote class="quote-body">
<p>Dolor met</p>
<aside class="quote-block">
<div class="quote-heading"><a href="/users/bob-1/">@Bob</a></div>
<blockquote class="quote-body">
<p>Dolor met</p>
</blockquote>
</aside>
</blockquote>
</aside>
<p>Lorem ipsum dolor.</p>
'''.strip()

        expected_result = '''
<p>Lorem ipsum.</p>
<aside class="quote-block">
<div class="quote-heading">Quoted message:</div>
<blockquote class="quote-body">
<p>Dolor met</p>
<aside class="quote-block">
<div class="quote-heading"><a href="/users/bob-1/">@Bob</a> has written:</div>
<blockquote class="quote-body">
<p>Dolor met</p>
</blockquote>
</aside>
</blockquote>
</aside>
<p>Lorem ipsum dolor.</p>
'''.strip()

        self.assertEqual(expected_result, finalise_markup(test_text))

    def test_finalise_minified_markup(self):
        """header is replaced in minified post"""
        test_text = '''
<p>Lorem ipsum.</p><aside class="quote-block"><div class="quote-heading"></div><blockquote class="quote-body"><p>Dolor met</p><aside class="quote-block"><div class="quote-heading"><a href="/users/bob-1/">@Bob</a></div><blockquote class="quote-body"><p>Dolor met</p></blockquote></aside></blockquote></aside><p>Lorem ipsum dolor.</p>
'''.strip()

        expected_result = '''
<p>Lorem ipsum.</p><aside class="quote-block"><div class="quote-heading">Quoted message:</div><blockquote class="quote-body"><p>Dolor met</p><aside class="quote-block"><div class="quote-heading"><a href="/users/bob-1/">@Bob</a> has written:</div><blockquote class="quote-body"><p>Dolor met</p></blockquote></aside></blockquote></aside><p>Lorem ipsum dolor.</p>
'''.strip()

        self.assertEqual(expected_result, finalise_markup(test_text))
