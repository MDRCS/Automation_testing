from unittest import TestCase

from TDD_Coding.blog import Blog
from TDD_Coding.post import Post


class BlogTest(TestCase):

    def test_create_post(self):
        b = Blog('Coding', 'mdrahali')
        p = Post('how works kub8', 'kub8 orchestration tool')
        b.create_post('how works kub8', 'kub8 orchestration tool')

        self.assertEqual(p.title, b.posts[0].title)

