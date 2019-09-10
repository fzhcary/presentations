from unittest import TestCase
from unittest.mock import Mock, patch
from hello import Hello
import random


# refer to https://realpython.com/python-mock-library
class TestHello(TestCase):
    def test_greet_with_mock(self):
        # test mock function return value
        self.assertEqual(Hello().greet("John"), "Hello, John!")
        mock = Mock()
        mock.return_value = "hey, I am mock."
        Hello.greet = mock
        self.assertEqual(Hello().greet("John"), "hey, I am mock.")

    def test_track_call(self):
        # test track calls to a function
        mock = Mock()
        Hello.greet = mock
        Hello.greet("John")
        self.assertTrue(mock.called)
        mock.assert_called_with("John")
        mock.assert_called_once_with("John")

    def test_mock_without_spec(self):
        # the deprecated_method is Hello class is removed but the unit test still passes without spec
        Hello = Mock()
        Hello.deprecated_method()
        self.assertTrue(Hello.deprecated_method.called)

    def test_mock_with_spec(self):
        """ spec ensures mock to track class method """
        obj = Hello()
        mock = Mock(spec=obj)
        with self.assertRaises(AttributeError):
            Hello.deprecated_method()

        self.assertEqual(Hello.greet("John"), "hey, I am mock.")

    @patch("hello.Hello.greet")  # func must be on path. "Hello.great" doesn't work since import has no effect.
    def test_greet_with_patch(self, mock_result):
        # test patch the return value
        mock_result.return_value = "hey, I am mock."
        self.assertEqual(Hello.greet("John"), "hey, I am mock.")

    @patch("hello.Hello.greet")
    def test_greet_with_patch2(self, mock_result):
        # test patch with side effect
        mock_result.side_effect = ["mock", "you"]
        self.assertEqual(Hello.greet("John"), "mock")
        self.assertEqual(Hello.greet("John"), "you")

    @patch("hello.Hello.greet", return_value="mocked again") # you can put return_value or side_effect in decorator
    def test_greet_with_patch3(self, mock_call):
        # another way to patch return value
        self.assertEqual(Hello.greet("John"), "mocked again")

    def test_greet_with_patch_context(self):
        """ use context manager to avoid multiple decorators """
        with patch('hello.Hello.greet') as mock_greet:
            mock_greet.return_value = "mocking"
            self.assertEqual(Hello.greet("John"), "mocking")

    @patch("hello.randint")
    def test_mock_randint(self, mock_result):
        # this is the right way to patch
        mock_result.return_value = 777
        self.assertEqual(Hello.guess_a_number(), 777)

    @patch("random.randint")
    def test_mock_randint2(self, mock_result):
        # want to mock function from another module, but mock local one instead -- common mistake !!!
        mock_result.return_value = 777
        self.assertNotEqual(Hello.guess_a_number(), 777)
        self.assertEqual(random.randint(0, 10), 777)


