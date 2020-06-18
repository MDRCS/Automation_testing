from unittest import TestCase
from unittest.mock import patch
from TDD_Coding import app
from TDD_Coding.blog import Blog


class AppTest(TestCase):

    def test_print_blogs(self):
        b = Blog('Test', 'mdrahali')
        app.blogs = {'Test': b}
        app.print_blogs()
        # patch function allows us to copy a function is behaviour and test the result if it's the same or not
        with patch('builtins.print') as mocked_print:
            app.print_blogs()
            mocked_print.assert_called_with('- blog Test by mdrahali')
