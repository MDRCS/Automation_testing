from unittest import TestCase
from TDD_Coding.post import Post


class PostTest(TestCase):

    def test_create_post(self):
        p = Post('test', 'Test content')

        self.assertEqual('test', p.title)
        self.assertEqual('Test content', p.content)

    def test_json(self):
        p = Post('test', 'Test content')
        expected = {'title': p.title, 'content': p.content}

        self.assertDictEqual(expected, p.json())
