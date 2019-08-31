from unittest import TestCase
from unittest.mock import Mock, patch
from hello import Hello
import random


# refer to https://realpython.com/python-mock-library
class TestHello(TestCase):
    def test_greet_with_mock(self):
        mock = Mock()
        mock.return_value = "hey, I am mock."
        Hello.greet = mock
        self.assertEqual(Hello.greet(), "hey, I am mock.")

    def test_track_call(self):
        """ mock is very flexible """
        mock = Mock()
        Hello.greet = mock
        Hello.greet("John")
        self.assertTrue(mock.called)
        print("test_track_call:",mock.mock_calls)
        mock.assert_called_with("John")
        mock.assert_called_once_with("John")

    def test_mock_with_spec(self):
        """ spec ensures mock to track class method """
        mock = Mock()
        mock.deprecated_method() # this doesn't raise exception, which is bad

        mock = Mock(spec=Hello)
        with self.assertRaises(AttributeError):
            mock.deprecated_method()

    @patch("hello.Hello.greet")  # func must be on path. "Hello.great" doesn't work since import has no effect.
    def test_greet_with_patch(self, mock_result):
        mock_result.return_value = "it's mocked"
        self.assertEqual(Hello.greet("John"), "it's mocked")

    @patch("hello.Hello.greet")
    def test_greet_with_patch2(self, mock_result):
        mock_result.side_effect = ["mock", "you"]
        self.assertEqual(Hello.greet("John"), "mock")
        self.assertEqual(Hello.greet("John"), "you")

    @patch("hello.Hello.greet", return_value="mocked again") # you can put return_value or side_effect in decorator
    def test_greet_with_patch3(self, mock_call):
        self.assertEqual(Hello.greet("John"), "mocked again")

    def test_greet_with_patch_context(self):
        """ use with can avoid multiple decorators """
        with patch('hello.Hello.greet') as mock_greet:
            mock_greet.return_value = "mocking"
            self.assertEqual(Hello.greet("John"), "mocking")

    @patch("hello.Hello.guess_a_number")
    def test_guess_a_number(self, mock_result):
        mock_result.return_value = 777
        self.assertEqual(Hello.guess_a_number(), 777)

    @patch("random.randint")
    def test_mock_randint(self, mock_result):
        # note it is a common mistake to patch the local random.randint instead of the one in hello module !!!
        mock_result.return_value = 777
        # we didn't patch that one
        self.assertNotEqual(Hello.guess_a_number(), 777)
        # we patched this local one
        self.assertEqual(random.randint(0, 10), 777)

    @patch("hello.randint")
    def test_mock_randint2(self, mock_result):
        # this is the right way to patch
        mock_result.return_value = 777
        self.assertEqual(Hello.guess_a_number(), 777)
