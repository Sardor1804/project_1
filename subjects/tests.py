from django.test import TestCase
from django.urls import reverse


class UrlsTests(TestCase):
    def test_ai_teacher_reverse_works(self):
        self.assertEqual(reverse('subjects:ai_teacher'), '/ai-teacher/')

    def test_ai_teacher_english_reverse_works(self):
        self.assertEqual(reverse('subjects:ai_teacher_english'), '/ai-teacher-english/')
