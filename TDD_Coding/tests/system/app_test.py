from unittest import TestCase
from unittest.mock import patch
from TDD_Coding import app
from TDD_Coding.blog import Blog
from TDD_Coding.post import Post


class AppTest(TestCase):

    def test_menu_input_selection(self):
        with patch('builtins.input') as mocked_input:
            app.menu()
            mocked_input.assert_called_with(app.MENU_PROMPT)

    def test_menu_call_print_blogs(self):
        with patch('TDD_Coding.app.print_blogs') as mocked_print_blogs:
            with patch('builtins.input', return_value='q'):
                app.menu()
                mocked_print_blogs.assert_called_with()

    def test_print_blogs(self):
        b = Blog('Test', 'mdrahali')
        app.blogs = {'Test': b}
        app.print_blogs()
        # patch function allows us to copy a function is behaviour and test the result if it's the same or not
        with patch('builtins.print') as mocked_print:
            app.print_blogs()
            mocked_print.assert_called_with('- blog Test by mdrahali')

    def test_create_blog_input(self):
        with patch('builtins.input') as mocked_input:
            # side_effect func help us insert those values in the
            # two input that we have
            mocked_input.side_effect = ('Test', 'Test Author')
            app.ask_create_blog()
            self.assertIsNotNone(app.blogs.get('Test'))

    def test_read_bog(self):
        blog = Blog('Test', 'mdrahali')
        blog.create_post('test', 'test content')
        app.blogs = {'Test': blog}

        with patch('builtins.input', return_value='Test'):
            with patch('TDD_Coding.app.print_posts') as mocked_print:
                app.ask_read_blog()

                mocked_print.assert_called_with(blog)

    def test_print_posts(self):
        blog = Blog('Test', 'mdrahali')
        blog.create_post('test', 'test content')
        app.blogs = {'Test': blog}

        with patch('TDD_Coding.app.print_post') as mocked_print_post:
            app.print_posts(blog)
            mocked_print_post.assert_called_with(blog.posts[0])

    def test_print_post(self):
        post = Post('test', 'test content')

        with patch('builtins.print') as mocked_print:
            app.print_post(post)

            mocked_print.assert_called_with(app.POST_TEMPLATE.format(post.title, post.content))

    def test_create_post(self):
        blog = Blog('Test', 'mdrahali')
        app.blogs = {'Test': blog}

        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('Test', 'Test', 'Test Content')
            app.ask_create_post()
            self.assertEqual(app.blogs.get('Test').posts[0].title, 'Test')
            self.assertEqual(app.blogs.get('Test').posts[0].content, 'Test Content')
