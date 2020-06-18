from unittest import TestCase

from TDD_Coding.blog import Blog
from TDD_Coding.post import Post


class BlogTest(TestCase):

    def test_create_post(self):
        b = Blog('Coding', 'mdrahali')
        p = Post('how works kub8', 'kub8 orchestration tool')
        b.create_post('how works kub8', 'kub8 orchestration tool')

        self.assertEqual(p.title, b.posts[0].title)

    def test_json(self):
        b = Blog('Coding', 'mdrahali')
        b.create_post('how works kub8', 'kub8 orchestration tool')
        expected = {
                    'title': b.title,
                    'author': b.author,
                    'posts':
                        [
                            {
                                'title': b.posts[0].title,
                                'content': b.posts[0].content
                            }
                        ]
                    }
        self.assertDictEqual(b.json(), expected)
