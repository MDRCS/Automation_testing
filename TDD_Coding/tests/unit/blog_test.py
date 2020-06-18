from unittest import TestCase
from TDD_Coding.blog import Blog
from TDD_Coding.post import Post


class BlogTest(TestCase):
    def test_create_blog(self):
        b = Blog('Coding', 'mdrahali')

        self.assertEqual('Coding', b.title)
        self.assertEqual('mdrahali', b.author)
        self.assertListEqual([], b.posts)

