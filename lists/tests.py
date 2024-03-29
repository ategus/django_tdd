from django.urls import resolve
from django.test import TestCase
from lists.views import home_page
from django.http import HttpRequest 
from django.http import HttpResponse
from django.template.loader import render_to_string

class HomePageTest(TestCase):
    
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expexted_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(), expexted_html)